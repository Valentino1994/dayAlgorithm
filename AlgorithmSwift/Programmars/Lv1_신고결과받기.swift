//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/07/29.
//

import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    var reportedDictionary = [String: [String]]()
    var emailingDictionary = [String: Int]()
    var result = [Int]()
    
    // report를 돌아보면서
    Set(report).forEach {
        let info = $0.split(separator: " ").map { String($0) }
        let reporting_id = info[0], reported_id = info[1]

        // set에 넣으면 중복된 애는 어차피 안들어감.
        if let _ = reportedDictionary[reported_id]{
            reportedDictionary[reported_id]!.append(reporting_id)
        } else {
            reportedDictionary[reported_id] = [reporting_id]
        }
    }
    
    // info를 보면서 value에 k개 이상의 Set이 생겼다면 email 숫자를 더해줌
    for info in reportedDictionary {
        let value = info.1
        
        if value.count >= k {
            for id in value {
                if let _ = emailingDictionary[id] {
                    emailingDictionary[id]! += 1
                } else {
                    emailingDictionary[id] = 1
                }
            }
        }
    }
    
    for id in id_list {
        if let _ = emailingDictionary[id] {
            result.append(emailingDictionary[id]!)
        } else {
            result.append(0)
        }
    }
    
    return result
}

let id_list = ["muzi", "frodo", "apeach", "neo"]
let report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
let k = 2

print(solution(id_list, report, k))


//랭커 코드
//import Foundation
//
//func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
//    var reported: [String: Int] = [:]
//    var user: [String: [String]] = [:]
//    // 여기 Set을 해주면 중복 신고를 제거할 수 있음
//    for r in Set(report) {
//        let splited = r.split(separator: " ").map { String($0) }
//        user[splited[0]] = (user[splited[0]] ?? []) + [splited[1]]
//        reported[splited[1]] = (reported[splited[1]] ?? 0) + 1
//    }
//    // reduce 좀 더 읽어보기.
//    return id_list.map { id in
//        return (user[id] ?? []).reduce(0) {
//            $0 + ((reported[$1] ?? 0) >= k ? 1 : 0)
//        }
//    }
//}
