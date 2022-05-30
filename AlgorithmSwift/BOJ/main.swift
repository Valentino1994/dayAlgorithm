//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/30.
//

import Foundation

let N: Int = Int(readLine()!)!
var IN: [[Int]] = []

for _ in 0..<N {
    let arr: [Int] = String(readLine()!).map { Int(String($0))! }
    IN.append(arr)
}

// 상 우 하 좌
let nextR: [Int] = [-1, 0, 1, 0]
let nextC: [Int] = [0, 1, 0, -1]

func bfs(start: [Int]) -> Int {
    var stack: [[Int]] = [start]
    var index: Int = 0
    IN[start[0]][start[1]] = 0
    while index < stack.count {
        
        let r: Int = stack[index][0]
        let c: Int = stack[index][1]
        
        for i in 0..<4 {
            let nr: Int = r + nextR[i]
            let nc: Int = c + nextC[i]
            
            if (0..<N).contains(nr), (0..<N).contains(nc) {
                if IN[nr][nc] == 1 {
                    IN[nr][nc] = 0
                    stack.append([nr, nc])
                }
            }
        }
        index += 1
    }
    return stack.count
}

var answer: String = ""
var temp: [Int] = []

for i in 0..<N {
    for j in 0..<N {
        if IN[i][j] == 1 {
            temp.append(bfs(start: [i, j]))
        }
    }
}
temp = temp.sorted(by: <)
answer += String(temp.count)
answer += "\n"

for i in 0..<temp.count {
    answer += String(temp[i])
    answer += "\n"
}

print(answer)
