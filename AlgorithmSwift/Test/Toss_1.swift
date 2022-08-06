//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/06.
//

import Foundation

func solution(_ messages:[[String]]) -> [String] {
    var result = [String]()
    
    var nowDate = ""
    var nowTime = ""
    var nowUser = ""
    
    for message in messages {
        let dateInfo = message[0].split(separator: "T")
        let userInfo = message[1]
        let messageInfo = message[2] == "" ? "<삭제된 메시지>" : message[2]
        
        let day = String(dateInfo[0])
        let timeInfo = dateInfo[1].map{ String($0) }
        let time = timeInfo[0..<timeInfo.count-3].joined()
        
        // 첫 메세지인 경우
        if nowDate == "" {
            result.append("[\(userInfo)]")
            result.append(messageInfo)
            nowDate = day
            nowTime = time
            nowUser = userInfo
            continue
            
        // 날짜가 바뀐 경우
        } else if nowDate != day {
            result.append("(\(nowTime))")
            result.append("-- \(day) --")
            result.append("[\(userInfo)]")
            result.append(messageInfo)
            nowDate = day
            nowTime = time
            nowUser = userInfo
            continue
            
        // 사람이 바뀌었을 경우 -> 이전 시간을 찍고 현재 사람을 찍음
        } else if nowUser != userInfo {
            result.append("(\(nowTime))")
            result.append("[\(userInfo)]")
            result.append(messageInfo)
            nowTime = time
            nowUser = userInfo
            continue
            
        // 시간이 바뀌었을 경우 -> 이전 시간을 찍고 사람을 찍고 메세지를 찍음
        } else if nowTime != time {
            result.append("(\(nowTime))")
            result.append("[\(userInfo)]")
            result.append(messageInfo)
            nowTime = time
            continue
            
        // 날짜도 안바뀌고 사람도 안바뀌고 시간도 안바뀌었을 경우
        } else {
            result.append(messageInfo)
            continue
        }
    
    }
    // 마지막 현재시간을 넣어줌
    result.append("(\(nowTime))")
    return result
}

let messages = [["2022-06-24T23:57:42", "정원", "민탁님"]]
print(solution(messages))
