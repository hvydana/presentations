#!/usr/bin/env python3
"""
Download and extract text from all non-login URLs in all_urls.txt.
Each URL gets its own file in scraped_docs/<slug>.txt
"""

import gzip
import io
import os
import re
import sys
import time
import urllib.request
import urllib.error
from html.parser import HTMLParser
from urllib.parse import urlparse

URLS_FILE   = "all_urls.txt"
OUTPUT_DIR  = "scraped_docs"
DELAY_SEC   = 2.0          # polite delay between requests
TIMEOUT_SEC = 20

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection":      "keep-alive",
    "Cache-Control":   "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest":  "document",
    "Sec-Fetch-Mode":  "navigate",
    "Sec-Fetch-Site":  "none",
    "Sec-Fetch-User":  "?1",
}

# Tags whose text content we completely skip
SKIP_TAGS = {
    "script", "style", "noscript", "head", "meta", "link",
    "nav", "footer", "header", "aside", "form", "button",
    "svg", "path", "iframe", "img",
}

# Inline tags — don't insert a newline for them
INLINE_TAGS = {
    "a", "b", "i", "em", "strong", "span", "code", "abbr",
    "cite", "q", "small", "sub", "sup", "time", "u",
}


class TextExtractor(HTMLParser):
    """HTML → clean readable text."""

    def __init__(self):
        super().__init__()
        self._skip_depth = 0
        self._skip_tag   = None
        self._parts      = []
        self._in_block   = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if self._skip_depth > 0:
            self._skip_depth += 1
            return
        if tag in SKIP_TAGS:
            self._skip_depth = 1
            self._skip_tag   = tag
            return
        if tag in ("p", "br", "li", "tr", "div", "blockquote",
                   "h1", "h2", "h3", "h4", "h5", "h6",
                   "article", "section", "main", "table", "thead", "tbody"):
            self._parts.append("\n")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self._skip_depth > 0:
            self._skip_depth -= 1
            return
        if tag in ("p", "li", "tr", "h1", "h2", "h3",
                   "h4", "h5", "h6", "blockquote"):
            self._parts.append("\n")

    def handle_data(self, data):
        if self._skip_depth > 0:
            return
        text = data.strip()
        if text:
            self._parts.append(text + " ")

    def handle_entityref(self, name):
        import html
        self.handle_data(html.unescape(f"&{name};"))

    def handle_charref(self, name):
        import html
        self.handle_data(html.unescape(f"&#{name};"))

    def get_text(self):
        raw = "".join(self._parts)
        # Collapse blank lines
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        # Collapse multiple spaces
        raw = re.sub(r"[ \t]{2,}", " ", raw)
        return raw.strip()


# ─── helpers ──────────────────────────────────────────────────────────────────

def parse_urls(filepath):
    """
    Parse all_urls.txt.
    Returns list of (url, label, skip) tuples.
    Lines starting with # are comments; [LOGIN] or [PAYWALL] entries are skipped.
    """
    entries = []
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("|", 1)
            url   = parts[0].strip()
            label = parts[1].strip() if len(parts) > 1 else url
            skip  = "[LOGIN]" in label or "[PAYWALL]" in label
            if url.startswith("http"):
                entries.append((url, label, skip))
    # De-duplicate by URL while preserving order
    seen = set()
    deduped = []
    for entry in entries:
        if entry[0] not in seen:
            seen.add(entry[0])
            deduped.append(entry)
    return deduped


def url_to_slug(url):
    parsed = urlparse(url)
    slug   = re.sub(r"[^\w\-]", "_", (parsed.netloc + parsed.path).strip("/"))
    return slug[:120]


def fetch(url):
    """Download URL, decompress if needed, return (html_str, error_str)."""
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
            raw = resp.read()
            enc = resp.getheader("Content-Encoding", "")
            ct  = resp.getheader("Content-Type", "")

            # Decompress
            if enc == "gzip" or raw[:2] == b"\x1f\x8b":
                try:
                    raw = gzip.decompress(raw)
                except Exception:
                    pass
            elif enc == "deflate":
                import zlib
                try:
                    raw = zlib.decompress(raw)
                except Exception:
                    raw = zlib.decompress(raw, -15)

            # Detect charset
            charset = "utf-8"
            m = re.search(r"charset=[\"']?([\w-]+)", ct, re.I)
            if m:
                charset = m.group(1)
            else:
                m = re.search(rb"charset=[\"']?([\w-]+)", raw[:2000], re.I)
                if m:
                    charset = m.group(1).decode()

            return raw.decode(charset, errors="replace"), None

    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code} {e.reason}"
    except urllib.error.URLError as e:
        return None, f"URLError: {e.reason}"
    except Exception as e:
        return None, f"Error: {e}"


def extract_text(html):
    parser = TextExtractor()
    parser.feed(html)
    return parser.get_text()


def word_count(text):
    return len(text.split())


# ─── main ─────────────────────────────────────────────────────────────────────

def main():
    if not os.path.exists(URLS_FILE):
        print(f"ERROR: {URLS_FILE} not found.", file=sys.stderr)
        sys.exit(1)

    entries = parse_urls(URLS_FILE)
    total   = len(entries)
    print(f"Loaded {total} unique URLs  (login-walled ones will be skipped)\n")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    skipped = 0
    success = 0
    failed  = 0

    for i, (url, label, skip) in enumerate(entries, 1):
        slug    = url_to_slug(url)
        outpath = os.path.join(OUTPUT_DIR, f"{slug}.txt")

        print(f"[{i:02d}/{total}] {label}")
        print(f"         {url}")

        if skip:
            print(f"  → SKIPPED (requires login/paywall)\n")
            skipped += 1
            continue

        if os.path.exists(outpath) and os.path.getsize(outpath) > 500:
            wc = word_count(open(outpath, encoding="utf-8").read())
            print(f"  → already saved ({wc:,} words) — skipping\n")
            success += 1
            continue

        html, err = fetch(url)

        if err:
            print(f"  → FAILED: {err}")
            with open(outpath, "w", encoding="utf-8") as f:
                f.write(f"FETCH FAILED\nURL: {url}\nLabel: {label}\nError: {err}\n")
            failed += 1
        else:
            text = extract_text(html)
            wc   = word_count(text)

            if wc < 50:
                print(f"  → WARNING: only {wc} words extracted (possible JS-heavy page)")

            with open(outpath, "w", encoding="utf-8") as f:
                f.write(f"SOURCE: {url}\n")
                f.write(f"LABEL:  {label}\n")
                f.write("=" * 80 + "\n\n")
                f.write(text)

            print(f"  → {wc:,} words  →  scraped_docs/{slug}.txt")
            success += 1

        print()
        if i < total and not skip:
            time.sleep(DELAY_SEC)

    print("─" * 60)
    print(f"Done.  Success: {success}  Failed: {failed}  Skipped (login): {skipped}")
    print(f"Files saved in: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
