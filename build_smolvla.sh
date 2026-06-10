#!/usr/bin/env bash
input=SmolVLA_improvements
export CHROME_PATH=/home/AMD/hvydana/.cache/puppeteer/chrome/linux-146.0.7680.31/chrome-linux64/chrome
export CHROME_NO_SANDBOX=true
marp "$input.md" --allow-local-files --pdf -o "$input.pdf"