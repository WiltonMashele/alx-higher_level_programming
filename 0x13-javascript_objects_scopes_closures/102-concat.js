#!/usr/bin/node
const fs = require('fs').promises;

(async () => {
  try {
    await fs.writeFile(process.argv[4], await fs.readFile(process.argv[2], 'utf8') + await fs.readFile(process.argv[3], 'utf8'));
  } catch (e) {
    console.error(e.message);
  }
})();
