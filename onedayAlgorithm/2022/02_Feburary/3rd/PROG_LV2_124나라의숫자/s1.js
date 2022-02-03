function solution(n) {
    var answer = '';
    while (n) {
        if (n % 3 === 1) {
            answer = '1' + answer
            n = parseInt(n/3)
        } else if (n % 3 == 2) {
            answer = '2' + answer
            n = parseInt(n/3)
        } else {
            answer = '4' + answer
            n = parseInt(n/3) - 1
            console.log(n)
        }
    }
    return answer;
}

console.log(solution(n))