#!/usr/bin/env bash
input=Physical_AI_SDK_v1.md
export CHROME_PATH=/home/AMD/hvydana/.cache/puppeteer/chrome/linux-146.0.7680.31/chrome-linux64/chrome
export CHROME_NO_SANDBOX=true
marp "$input" --allow-local-files --pdf -o "${input%.md}.pdf"