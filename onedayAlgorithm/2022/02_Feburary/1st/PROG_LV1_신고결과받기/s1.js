function solution(id_list, report, k) {
    var answer = [];
    var id_dict = {};

    for (const id of id_list) {
        id_dict[id] = [[], []]
    }

    for (let repo of report) {
        
        const tmp = repo.split(" ");
        let reporter = tmp[0]
        let respondent = tmp[1]

        if (id_dict[respondent][1].indexOf(reporter) === -1) {
            id_dict[respondent][1].push(reporter);
        }

        if (id_dict[reporter][0].indexOf(respondent) === -1) {
            id_dict[reporter][0].push(respondent);
        }
    }

    for (key in id_dict) {
        tmp = 0
        for (user of id_dict[key][0]) {
            if (id_dict[user][1].length >= k) {
                tmp += 1
            } 
        }
        answer.push(tmp)
    }
    return answer;
}

let id_list = ["muzi", "frodo", "apeach", "neo"];
let report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"];
let k = 2
console.log(solution(id_list, report, k));