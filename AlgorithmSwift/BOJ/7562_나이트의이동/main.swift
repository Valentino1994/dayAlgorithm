//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/24.
//

import Foundation

let T = Int(readLine()!)!

// 나이트의 시계 방향으로 움직임
let dr = [-2, -1, 1, 2, 2, 1, -1, -2]
let dc = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in 0..<T {
    let boardSize = Int(readLine()!)!
    let startPoint = readLine()!.split(separator: " ").map { Int(String($0))! }
    let targetPoint = readLine()!.split(separator: " ").map { Int(String($0))! }
    
    var board = Array(repeating: Array(repeating: 0, count: boardSize), count: boardSize)
    var result = 987654321
    
    var queue = [[startPoint, 0]]
    var queueIndex = 0
    board[startPoint[0]][startPoint[1]] = 1
    
    while queueIndex < queue.count {
        let nowNode = queue[queueIndex][0] as! [Int]
        let nowCnt = queue[queueIndex][1] as! Int
        
        if nowNode == targetPoint {
            result = min(result, nowCnt)
            break
        }
        
        for i in 0..<dr.count {
            let nr = nowNode[0] + dr[i], nc = nowNode[1] + dc[i]
            if (0..<boardSize).contains(nr) && (0..<boardSize).contains(nc) && board[nr][nc] == 0 {
                queue.append([[nr, nc], nowCnt + 1])
                board[nr][nc] = 1
            }
        }
        
        queueIndex += 1
    }
    
    print(result)
}



