//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/31.
//

import Foundation

let N = Int(readLine()!)!
var meetings: [[Int]] = []

for _ in 0..<N {
    let temp = readLine()!.split(separator: " ").map { Int($0)! }
    meetings.append(temp)
}

func solution(meetings: [[Int]]) -> Int {
    
    var meetings = meetings
    meetings.sort{ return $0[0] < $1[0] }
    meetings.sort{ return $0[1] < $1[1] }
    var max_meetings: [[Int]] = [meetings[0]]

    for i in 1..<N {
        let prev_meeting = max_meetings[max_meetings.count-1]
        let now_meeting = meetings[i]
        
        if prev_meeting[1] > now_meeting[1]{
            max_meetings[max_meetings.count-1] = now_meeting
            continue
        }
        
        if prev_meeting[1] <= now_meeting[0]{
            max_meetings.append(now_meeting)
        }
    }
    return max_meetings.count
}


print(solution(meetings: meetings))


