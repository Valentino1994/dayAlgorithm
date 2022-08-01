//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/07/15.
//

import Foundation

guard let N = readLine(), let N = Int(N) else { fatalError() }
let numbers = readLine()!.split(separator: " " ).map{ Int(String($0))! }
guard let K = readLine(), let K = Int(K) else { fatalError() }

func answer(N: Int, K: Int) -> String {
    var result: String = ""
    
    var memo: [Int] = Array(repeating: 987654321, count: 1001)
    memo[0] = 0
    
    for number in numbers {
        memo[number] = 1
    }
    
    for i in 2...1000 {
        for j in 0..<numbers.count {
            if 0 < i - numbers[j] {
                if memo[i - numbers[j]] < K && memo[i - numbers[j]] + 1 < memo[i]{
                    memo[i] = memo[i - numbers[j]] + 1
                }
            }
        }
        if memo[i] == 987654321 {
            result = i % 2 == 0 ? "holsoon win at \(i)" : "jjaksoon win at \(i)"
            break
        }
    }
//    print(memo)
    return result
}

print(answer(N: N, K: K))
