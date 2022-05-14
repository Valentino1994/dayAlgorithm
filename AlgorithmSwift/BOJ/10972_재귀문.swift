//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/14.
//

import Foundation

func permute(_ nums: [Int], _ targetNum: Int) -> [[Int]] {
    var result = [[Int]]()
    var visited = [Bool](repeating: false, count: nums.count)
    
    func permutation(_ nowPermute: [Int]) {
        if nowPermute.count == targetNum {
            result.append(nowPermute)
            return
        }
        for i in 0..<nums.count {
            if visited[i] == true {
                continue
            }
            else {
                visited[i] = true
                permutation(nowPermute + [nums[i]])
                visited[i] = false
            }
        }
    }
    permutation([])
    
    return result
}

var N = Int(readLine()!)!
var targetNumber: [Int] = readLine()!.split(separator: " ").map {Int(String($0))! }

var numbers: [Int] = []
for i in 1...(N) {
    numbers.append(i)
}

var permuted_array = permute(numbers, numbers.count)

var answer: Int = 0
for i in 0..<permuted_array.count {
    if permuted_array[i] == targetNumber {
        answer = i
        break
    }
}

if answer == permuted_array.count-1 {
    print(-1)
} else {
    print(permuted_array[answer + 1].map{ String($0) }.joined(separator: " "))
}

