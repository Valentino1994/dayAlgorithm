let players = ["mumu", "soe", "poe", "kai", "mine"];
let callings = ["kai", "kai", "mine", "mine"];

function makeLine(players) {
    let rankingMap = new Map();
    for (i=0; i < players.length; i++) {
        rankingMap.set(i, players[i]);
    };
    return rankingMap;
}

function solution(players, callings) {
    let nowLine = makeLine(players);
    console.log(nowLine);

    return players;
}

solution(players, callings);