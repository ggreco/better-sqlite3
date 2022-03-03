const fs = require("fs");
const path = require("path");

const modulePath = process.argv[2];

try {
    fs.unlinkSync(path.join(modulePath, "sqlite3.a"));
} catch (err) {
    try {
        fs.unlinkSync("build/Release/sqlite3.a");
    } catch (err) {
        // ignore the error
    }
}

