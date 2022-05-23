//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/18.
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

var N: Int = Int(readLine()!)!
var tempArr: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
var answer: Int = 0
var permutedArr: [[Int]] = permute(tempArr, tempArr.count)

for arr in permutedArr {
    var tempNum: Int = 0
    
    for i in 0..<arr.count-1 {
        tempNum += abs(arr[i] - arr[i+1])
    }
    
    if tempNum > answer {
        answer = tempNum
    }
}

print(answer)
