//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/15.
//

import Foundation

var N: Int = Int(readLine()!)!
var timeTable: [Int] = []
var valueTable: [Int] = []
var DP: [Int] = Array(repeating: 0, count: N + 1)

for _ in 0..<N {
    let data: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
    timeTable.append(data[0])
    valueTable.append(data[1])
}

var maxValue: Int = 0

for i in (0...N-1).reversed() {
    let time: Int = timeTable[i] + i
    if time <= N {
        DP[i] = max(valueTable[i] + DP[time], maxValue)
        maxValue = DP[i]
    } else {
        DP[i] = maxValue
    }
}

print(maxValue)
