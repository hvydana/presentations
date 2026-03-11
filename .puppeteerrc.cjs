const {join} = require('path');
const os = require('os');

/**
 * @type {import("puppeteer").Configuration}
 */
module.exports = {
  executablePath: join(os.homedir(), '.cache/puppeteer/chrome/linux-146.0.7680.31/chrome-linux64/chrome'),
  args: [
    '--no-sandbox',
    '--disable-setuid-sandbox',
    '--disable-dev-shm-usage',
    '--disable-gpu'
  ]
};
