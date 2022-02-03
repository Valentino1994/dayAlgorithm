function solution(id_list, report, k) {
    var answer = new Array(id_list.length);
    answer.fill(0);
    report_info = {};

    for (const id of id_list) {
        report_info[id] = []
    }
    // id_list에 본인을 신고한 사람을 저장.
    report.map((repo) => {
        const [user_id, report_id] = repo.split(' ');
        if (!report_info[report_id].includes(user_id)) {
            report_info[report_id].push(user_id)
        };
    })
    // 본인을 신고한 사람들의 수가 k 이상이면 그 사람들에게 메일 숫자를 올려줌.
    for (key in report_info) {
        if (report_info[key].length >= k) {
            report_info[key].map((user) => {
                answer[id_list.indexOf(user)] += 1
            })
        }
    }
    return answer;
}

let id_list = ["muzi", "frodo", "apeach", "neo"];
let report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"];
let k = 2
console.log(solution(id_list, report, k));