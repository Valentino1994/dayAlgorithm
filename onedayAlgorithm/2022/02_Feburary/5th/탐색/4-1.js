const fs = require('fs');
const stdin = (process.platform === 'linux'
            ? fs.readFileSync('/dev/stdin').toString()
            : 
`5
R R R U D D
`
).split('\n');

const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

let n = parseInt(input());
let commands = input().split(' ');

let r = 0;
let c = 0;

const com = {'R': [0, 1], 'L': [0, -1], 'U': [-1, 0], 'D': [1, 0]}

for (let command of commands) {
    dr = com[command][0]
    dc = com[command][1]

    if (r + dr < 0 || c + dc < 0 || r + dr > n || c + dc > n) continue;
    
    r = r + dr
    c = c + dc
}

console.log(r + 1, c + 1);