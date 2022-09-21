//
//  my.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/21.
//

import Foundation

let N = Int(readLine()!)!
var fieled = [[Int]]()
var minRange = 100
var maxRange = 1

for i in 0..<N {
    fieled.append(readLine()!.split(separator: " ").map { Int(String($0))! })
    minRange = min(minRange, fieled[i].min()!)
    maxRange = max(maxRange, fieled[i].max()!)
}

var answer = 0

let dr = [-1, 0, 1, 0]
let dc = [0, 1, 0, -1]

for now in minRange - 1...maxRange {
    var copyFieled = fieled
    var result = 0
    for i in 0..<N {
        for j in 0..<N {
            if copyFieled[i][j] > now {
                result += 1
                var stack = [[i, j]]
                copyFieled[i][j] = 0
                
                while !stack.isEmpty {
                    let node = stack.removeFirst()
                    fieled[node[0]][node[1]] = 0
                    for i in 0..<4 {
                        let newR = node[0] + dr[i]
                        let newC = node[1] + dc[i]
                        
                        if (0..<N).contains(newR) && (0..<N).contains(newC) && copyFieled[newR][newC] > now {
                            stack.append([newR, newC])
                        }
                    }
                }
            }
        }
    }
    
    answer = max(answer, result)
}

print(answer)
