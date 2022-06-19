//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/06/03.
//

import Foundation

let N: Int = Int(readLine()!)!
let Info: [Character] = readLine()!.map { Character(extendedGraphemeClusterLiteral: $0) }
var sequences: [Character] = []
var maxNum: Int = N
var index: Int = 0

// 부호를 파악한다.
for i in (1...N).reversed() {
    sequences.append(Info[index])
    index += i
}

var result: [Int] = Array(repeating: 0, count: N)
// 부호와 맨 윗줄을 기준으로 가능한 조합을 만든다.
func makeCombination(index: Int) -> [Int] {
    
    if index == N {
        // 아래로 내려가면서 모든 경우에 성립하는지 확인한다.
//        print(result)
        return result
    }
    
    for i in 0...10 {
        let storedNum: Int = result[index]
        result[index] = sequences[index] == "+" ? i : -i
        var temp: Int = 0
        var flag: Bool = true
        for j in 0..<index {
            temp += result[j]
            if temp > 0 && sequences[j] != "+" {
                flag = false
                break
            } else if temp < 0 && sequences[j] != "-" {
                flag = false
                break
            } else if temp == 0 && sequences[j] != "0" {
                flag = false
                break
            }
        }
        if flag {
            makeCombination(index: index + 1)
        } else {
            result[index] = storedNum
        }
    }
    return result
}
// 조합을 보고 아래로 내려오면서 모두 맞는지 확인하는 함수.

print(makeCombination(index: 0))
