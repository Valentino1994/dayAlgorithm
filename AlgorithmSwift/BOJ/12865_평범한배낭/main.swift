//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/26.
//

import Foundation

let NK = readLine()!.split(separator: " ").map { Int(String($0))! }
let N = NK[0], K = NK[1]
var things = [[Int]]()

for _ in 0..<N {
    let thing = readLine()!.split(separator: " ").map { Int(String($0))! }
    things.append(thing)
}

var dp = Array(repeating: Array(repeating: 0, count: K+1), count: N+1)

for i in 1...N {
    for j in 1...K {
        if things[i-1][0] <= j {
            dp[i][j] = max(things[i-1][1] + dp[i-1][j - things[i-1][0]], dp[i-1][j])
        } else {
            dp[i][j] = dp[i-1][j]
        }
    }
}

print(dp[N][K])

