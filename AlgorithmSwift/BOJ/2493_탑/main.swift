//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/28.
//

import Foundation

let N = Int(readLine()!)!
let towers = readLine()!.split(separator: " ").map { Int(String($0)) }

var towerIndex = N-1

var answer = [Int]()

while towerIndex > 0 {
    
    var razerIndex = towerIndex - 1
    
    while razerIndex > 0 {
        if towers[razerIndex]! >= towers[towerIndex]! {
            answer.append(razerIndex+1)
            break
        } else {
            razerIndex -= 1
        }
    }
    if razerIndex == 0 {
        answer.append(0)
    }
    towerIndex -= 1
}

answer.append(0)

answer = answer.reversed()

print(answer)
