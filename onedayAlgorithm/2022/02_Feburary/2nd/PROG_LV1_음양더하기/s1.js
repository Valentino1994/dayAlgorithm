function solution(absolutes, signs) {
    let answer = 0;
    
    for (let i = 0; i < absolutes.length; i++) {
        if (signs[i] === true) {
            answer = answer - absolutes[i]
        } else {
            answer = answer + absolutes[i]
        };
    };
    return answer;
}

let absolutes = [4,7,12];
let signs = [true,false,true];

console.log(solution(absolutes, signs));