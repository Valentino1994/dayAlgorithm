//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/28.
//

import Foundation

let N = Int(readLine()!)!
var board = [[String]]()

for _ in 0..<N {
    board.append(readLine()!.map{String($0)})
}

var visited = Array(repeating: Array(repeating: 0, count: N), count: N)
var answer = ""

// 상 우 하 좌
let dr = [-1, 0, 1, 0]
let dc = [0, 1, 0, -1]

func bfs(visited: [[Int]], colorBlind: Int) -> Int {
    
    var copyVisited = visited
    var result = 0
    
    for i in 0..<N {
        for j in 0..<N {
            if copyVisited[i][j] == 0 {
                result += 1
                var queue = [[i, j]]
                copyVisited[i][j] = 1
                
                var queIndex = 0
                let nowColor = board[i][j]

                while queIndex < queue.count {
                    let now = queue[queIndex]
                    let r = now[0], c = now[1]
                    
                    for i in 0..<4 {
                        let newR = r + dr[i], newC = c + dc[i]
                        if (0..<N).contains(newR) && (0..<N).contains(newC) && copyVisited[newR][newC] == 0 {
                            if colorBlind == 1 {
                                if (nowColor == "R" || nowColor == "G") && (board[newR][newC] == "R" || board[newR][newC] == "G") {
                                    copyVisited[newR][newC] = 1
                                    queue.append([newR, newC])
                                } else {
                                    if nowColor == board[newR][newC] {
                                        copyVisited[newR][newC] = 1
                                        queue.append([newR, newC])
                                    }
                                }
                            } else {
                                if nowColor == board[newR][newC] {
                                    copyVisited[newR][newC] = 1
                                    queue.append([newR, newC])
                                }
                            }
                        }
                    }
                    queIndex += 1
                }
            }
        }
    }
    
    return result
}


for i in 0..<2 {
    answer += String(bfs(visited: visited, colorBlind: i))
    answer += " "
}

answer.removeLast()

print(answer)
