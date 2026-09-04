#!/usr/bin/env bash
#
# compile.sh — render a Marp markdown deck to PDF.
#
# Why this is not just `marp --pdf`:
#   1. The marp-cli bundled here (v4.2.3) ships a puppeteer-core that cannot
#      drive the installed Chrome 146 — it crashes at launch with
#      "TargetCloseError: Target closed", so `marp --pdf` fails.
#   2. .marprc.yml sets `allowLocalFiles: true`, which forces marp to spawn a
#      browser even for plain HTML output (and hits the same crash).
#
# Strategy that works: generate the HTML with marp from a scratch directory
# (so ./.marprc.yml is NOT auto-loaded and no browser is spawned), then let
# Chrome print that HTML to PDF directly — Chrome works fine when we drive it
# ourselves. Marp's print CSS paginates one slide per page.
#
# Usage:
#   ./compile.sh                       # builds Physical_AI_SDK_v2.md
#   ./compile.sh some_deck.md          # builds a specific deck
#   CHROME_PATH=/path/to/chrome ./compile.sh deck.md   # override browser

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT="${1:-aig_models_collab.md}"

# Resolve input to an absolute path (relative paths are relative to this dir).
case "$INPUT" in
  /*) SRC="$INPUT" ;;
  *)  SRC="$HERE/$INPUT" ;;
esac
[[ -f "$SRC" ]] || { echo "error: markdown not found: $SRC" >&2; exit 1; }

BASE="${SRC%.md}"
HTML="${BASE}.render.html"
PDF="${BASE}.pdf"

MARP="$HERE/node_modules/.bin/marp"
[[ -x "$MARP" ]] || MARP="marp"   # fall back to a marp on PATH

# --- locate a Chrome / Chromium / Edge binary --------------------------------
find_chrome() {
  local c
  for c in \
    "${CHROME_PATH:-}" \
    "$HOME"/.cache/puppeteer/chrome/*/chrome-linux64/chrome \
    /usr/bin/google-chrome /usr/bin/google-chrome-stable \
    /usr/bin/chromium /usr/bin/chromium-browser \
    /usr/bin/microsoft-edge /snap/bin/chromium; do
    [[ -n "$c" && -x "$c" ]] && { echo "$c"; return 0; }
  done
  return 1
}
CHROME="$(find_chrome)" || {
  echo "error: no Chrome/Chromium/Edge found. Set CHROME_PATH=/path/to/chrome" >&2
  exit 1
}

echo "[compile] deck  : $SRC"
echo "[compile] marp  : $MARP"
echo "[compile] chrome: $CHROME"

# --- 1. markdown -> HTML -----------------------------------------------------
# Run from /tmp so the deck's .marprc.yml (allowLocalFiles:true) is not loaded,
# which would otherwise force a browser and crash. Relative assets (e.g. the
# footer logo) still resolve because marp keeps them relative to the deck dir.
( cd /tmp && "$MARP" --html "$SRC" -o "$HTML" )

# Marp wraps code/headings in a JS-driven "marp-pre" auto-scaling custom element.
# That JS does not finalize during Chrome's headless --print-to-pdf, so scaled
# code blocks collapse to blank white boxes. Strip the auto-scaling hooks so the
# <pre> renders as plain HTML (syntax highlighting is preserved).
sed -i 's/ is="marp-pre"//g; s/ data-auto-scaling="[^"]*"//g' "$HTML"

# --- 2. HTML -> PDF via Chrome ----------------------------------------------
# Chrome's own headless print works even though marp's puppeteer cannot.
# The dbus/UPower warnings Chrome prints here are harmless.
"$CHROME" --headless --no-sandbox --disable-gpu --disable-dev-shm-usage \
  --no-pdf-header-footer \
  --allow-file-access-from-files \
  --print-to-pdf="$PDF" "file://$HTML" 2>/dev/null

rm -f "$HTML"
echo "[compile] wrote : $PDF"
