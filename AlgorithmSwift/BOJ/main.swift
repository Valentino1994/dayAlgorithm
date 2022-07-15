//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/07/15.
//

import Foundation

guard let N = readLine(), let N = Int(N) else { fatalError() }

var DP: [Int] = Array(repeating: 5000, count: 5001)

DP[3] = 1
DP[4] = 5000
DP[5] = 1

if N > 5 {
    for i in 6...N {
        if DP[i-3] == 5000 && DP[i-5] == 5000 {
            DP[i] = 5000
        }
        else {
            DP[i] = min(DP[i-3]+1, DP[i-5]+1)
        }
    }
}

if DP[N] == 5000  {
    print(-1)
} else {
    print(DP[N])
}
