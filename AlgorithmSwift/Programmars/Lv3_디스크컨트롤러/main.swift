//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/19.
//

import Foundation

func solution(_ jobs:[[Int]]) -> Int {
    var sortedJobs = jobs.sorted{ $0[1] < $1[1] }
    var currentTime = 0, answer = 0

    while !sortedJobs.isEmpty {
        var flag = false
        
        for i in 0 ..< sortedJobs.count {
            if sortedJobs[i][0] <= currentTime {
                currentTime += sortedJobs[i][1]
                answer += currentTime - sortedJobs[i][0]
                sortedJobs.remove(at: i)
                flag = true
                break
            }
        }

        if !flag {
            currentTime = sortedJobs.min { a, b in a[0] < b[0] }![0]
        }
    }

    return answer / jobs.count
}
