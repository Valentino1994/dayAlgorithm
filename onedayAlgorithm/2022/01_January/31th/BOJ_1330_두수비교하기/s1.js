const fs = require("fs");
const stdin = (process.platform === 'linux' 
            ? fs.readFileSync('/dev/stdin').toString()
            : 
            `1 2`
            ).split('\n');

const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

const [a, b] = input().split(' ').map(Number);

if (a > b) {
    console.log(">")
} else if (a < b) {
    console.log("<")
} else {
    console.log("==")
}