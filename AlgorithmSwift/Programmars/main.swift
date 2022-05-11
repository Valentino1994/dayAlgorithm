//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/11.
//
import Foundation

func solution(_ info:[String], _ query:[String]) -> [Int] {
    
    var result: [Int] = []
    
    var informations: [[String]] = []
    
    for inf in info {
        let temp = inf.split(separator: " ").map { String($0) }
        informations.append(temp)
    }
    
    for q in query {
        var temp_result: Int = 0
        let compare = q.split(separator: " ").map { String($0) }.filter { $0 != "and" }
        
        for i in 0..<informations.count {
            var flag: Bool = true
            let person: [String] = informations[i]
            for j in 0..<person.count {
                if compare[j] == "-" {
                    continue
                } else if compare[j].allSatisfy({ $0.isNumber }) {
                    if Int(compare[j])! <= Int(person[j])! {
                        continue
                    } else {
                        flag = false
                        break
                    }
                } else if compare[j] != person[j] {
                    flag = false
                    break
                }
            }
            if flag {
                temp_result += 1
            }
        }
        result.append(temp_result)
    }
    
    return result
}

//

func solution2(_ info:[String], _ query:[String]) -> [Int] {
     var result: [Int] = []
    var db: [String: [Int]] = [:]

    // 정보에대한 모든 경우의 수 입력해놓기
    for s in info {
        let infos = s.components(separatedBy: .whitespaces)
        let languages = [infos[0], "-"]
        let jobs = [infos[1], "-"]
        let careers = [infos[2], "-"]
        let soulFoods = [infos[3], "-"]
        let score = Int(infos[4])!

        // 조합
        for lang in languages {
            for job in jobs {
                for career in careers {
                    for food in soulFoods {
                        let key = "\(lang) \(job) \(career) \(food)"
                        if db.keys.contains(key) {
                            db[key]?.append(score)
                        } else {
                            db[key] = [score]
                        }
                    }
                }
            }
        }
    }

    // 딕셔너리 점수순 재정렬
    for origin in db {
        let sortValue = origin.value.sorted()
        db[origin.key] = sortValue
    }

    // 쿼리를 키로 점수배열을 가져오고 점수배열을 이진탐색으로 효율적탐색 시도
    query.forEach {
        let excuteQuery = $0.components(separatedBy: .whitespaces)

        let lang = excuteQuery[0]
        let job = excuteQuery[2]
        let career = excuteQuery[4]
        let food = excuteQuery[6]
        let score = Int(excuteQuery[7])!

        let key = "\(lang) \(job) \(career) \(food)"
        if let matchScores = db[key] {
            // 이진 탐색
            var start = 0
            var end = matchScores.count
            while start < end {
                let mid = (start + end) / 2

                if matchScores[mid] >= score {
                    end = mid
                } else {
                    start = mid + 1
                }
            }
            // print(matchScores)
            // print("start: \(start) end: \(end) score: \(score)")
            result.append(matchScores.count - start)

        } else {
            result.append(0)
        }

    }
    // print(result)
    return result
}

var info: [String] = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
var query: [String] = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))
