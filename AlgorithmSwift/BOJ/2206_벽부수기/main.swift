//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/26.
//

import Foundation

let NM = readLine()!.split(separator: " ").map { Int(String($0))! }
var wall = [[Int]]()

for _ in 0..<NM[0] {
    wall.append(String(readLine()!).map { Int(String($0))! })
}

var nowPath = [[0, 0]]
var path = [0]
// 상 우 하 좌
let dr = [-1, 0, 1, 0]
let dc = [0, 1, 0, -1]

var answer = 987654321
var visited = Array(repeating: Array(repeating: 0, count: NM[1]), count: NM[0])
visited[0][0] = 1

func dfs(nowPath: [[Int]], path: [Int]) {
    
    var copyNowPath = nowPath
    var copyPath = path
    
    let nowPosition = nowPath[nowPath.count - 1]
    
    if nowPath.count > answer {
        return
    }
    
    if visited[NM[0]-1][NM[1]-1] == 1 {
        answer = min(answer, nowPath.count)
        return
    }
    
    for i in 0..<4 {
        let newR = nowPosition[0] + dr[i]
        let newC = nowPosition[1] + dc[i]
        
        // 벽을 넘지 않았다면
        if (0..<NM[0]).contains(newR) && (0..<NM[1]).contains(newC) {
            // 다음이 벽이라면
            if wall[newR][newC] == 1 {
                // 벽인데 path에 이미 벽이 포함되어 있다면 return
                if path.contains(1) {
                    continue
                } else if visited[newR][newC] == 0 {
                    copyNowPath.append([newR, newC])
                    copyPath.append(1)
                    visited[newR][newC] = 1
                    dfs(nowPath: copyNowPath, path: copyPath)
                    visited[newR][newC] = 0
                    copyNowPath.removeLast()
                    copyPath.removeLast()
                }
            } else if visited[newR][newC] == 0 {
                copyNowPath.append([newR, newC])
                copyPath.append(0)
                visited[newR][newC] = 1
                dfs(nowPath: copyNowPath, path: copyPath)
                visited[newR][newC] = 0
                copyNowPath.removeLast()
                copyPath.removeLast()
            }
        }
    }
}

dfs(nowPath: nowPath, path: path)
print(answer == 987654321 ? -1 : answer)
