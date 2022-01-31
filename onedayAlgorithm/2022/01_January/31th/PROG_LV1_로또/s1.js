var lottos = [44, 1, 0, 0, 31, 25]	
var win_nums = 	[31, 10, 45, 1, 6, 19]

function winners(number) {
    switch (number) {
        case 6: { return 1 }
        case 5: { return 2 }
        case 4: { return 3 }
        case 3: { return 4 }
        case 2: { return 5 }
        default: { return 6 }
    }
}

function solution(lottos, win_nums) {
    var answer = [];

    var N = lottos.length;

    cnt = 0;
    zero_cnt = 0;
    for (var i = 0; i < N; i ++) {
        if (win_nums.indexOf(lottos[i]) !== -1) {
            cnt += 1
        } else if (lottos[i] == 0) {
            zero_cnt += 1
        }
    };

    answer.push(winners(cnt + zero_cnt));
    answer.push(winners(cnt));

    return answer;
}

console.log(solution(lottos, win_nums));

