//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/15.
//

import Foundation

var N: Int = Int(readLine()!)!
var visited: [Bool] = Array(repeating: false, count: N+1)
var table: [[Int]] = [[-1, -1]]

for _ in 0..<N {
    table.append(readLine()!.split(separator: " ").map{ Int(String($0))! })
}

var result: Int = 0

func findMaximum(index: Int, profit: Int) {
    let day_need: Int = table[index][0]
    let profit_expected: Int = table[index][1]
    
    if index + day_need > N+1 {
        result = max(result, profit)
        return
    } else if index + day_need == N+1{
        result = max(result, profit + profit_expected)
        return
    }
    
    for i in (index+day_need)...N {
        if !visited[i] {
            visited[i] = true
            findMaximum(index: i, profit: profit+profit_expected)
            visited[i] = false
        }
    }
    return
}

findMaximum(index: 1, profit: 0)

print(result)
