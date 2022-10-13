//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/13.
//

import Foundation

let MNK = readLine()!.split(separator: " ").map { Int(String($0))! }
var infos = [[Int]]()

// M = R, N = C
let M = MNK[0], N = MNK[1], K = MNK[2]

for _ in 0..<K {
    infos.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

var board = Array(repeating: Array(repeating: 0, count: N), count: M)

for info in infos {
    let C1 = info[0], R1 = info[1], C2 = info[2], R2 = info[3]
    for i in R1..<R2 {
        for j in C1..<C2 {
            board[i][j] = 1
        }
    }
}

var answer = [Int]()

for i in 0..<M {
    for j in 0..<N {
        if board[i][j] == 0 {
            board[i][j] = 1
            let size = bfs(rc: [i, j])
            answer.append(size)
        }
    }
}

func bfs(rc: [Int]) -> Int {
    // 상 우 하 좌
    let dr = [-1, 0, 1, 0]
    let dc = [0, -1, 0, 1]
    
    var result = 0
    
    var queue = [rc]
    var queueIndex = 0
    
    while queueIndex < queue.count {
        let nowNode = queue[queueIndex]
        let nowR = nowNode[0]
        let nowC = nowNode[1]
        
        result += 1

        for i in 0..<4 {
            let newR = nowR + dr[i]
            let newC = nowC + dc[i]
            
            if (0..<M).contains(newR) && (0..<N).contains(newC) && board[newR][newC] == 0 {
                board[newR][newC] = 1
                queue.append([newR, newC])
            }
        }
        queueIndex += 1
    }
    return result
}

print(answer.count)
print(answer.sorted(by: <).map{ String($0) }.joined(separator: " "))
