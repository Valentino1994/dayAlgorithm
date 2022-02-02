function solution(id_list, report, k) {
    const answer = new Array(id_list.length);
    answer.fill(0);
    report_result = {};

    id_list.map((user) => {
        report_result[user] = []
    });

    report.map((info) => {
        const [user_id, reported_id] = info.split(' ');
        if (!report_result[reported_id].includes(user_id)) {
            report_result[reported_id].push(user_id);
        };
    });

    for (const key in report_result) {
        if (report_result[key].length >= k) {
            report_result[key].map((user) => {
                answer[id_list.indexOf(user)] += 1;
            })
        }
    }

    return answer;
}


let id_list = ["muzi", "frodo", "apeach", "neo"];
let report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"];
let k = 2
console.log(solution(id_list, report, k));