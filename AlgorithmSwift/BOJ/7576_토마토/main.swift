//
//  File.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/11/25.
//

import Foundation

let NM = readLine()!.split(separator: " ").map { Int(String($0))! }
let N = NM[0], M = NM[1]
var tomatoCase: [[Int]] = []
for _ in 0..<M {
    let tomatoRow = readLine()!.split(separator: " ").map { Int(String($0))! }
    tomatoCase.append(tomatoRow)
}

var queue: [[Int]] = []
for i in 0..<M {
    for j in 0..<N {
        if tomatoCase[i][j] == 1 {
            queue.append([i, j])
        }
    }
}

func bfs() {
    let dr: [Int] = [-1, 0, 1, 0]
    let dc: [Int] = [0, 1, 0, -1]
    
    var queueIndex: Int = 0
    while queueIndex < queue.count {
        let nowTomato = queue[queueIndex]
        let r = nowTomato[0], c = nowTomato[1]
        for i in 0..<4 {
            let nr = r + dr[i], nc = c + dc[i]
            if (0..<M).contains(nr) && (0..<N).contains(nc) && tomatoCase[nr][nc] == 0 {
                tomatoCase[nr][nc] = tomatoCase[r][c] + 1
                queue.append([nr, nc])
            }
        }
        queueIndex += 1
    }
    
    return
}

func checkCase() -> Int {
    var result = -1
    for i in 0..<M {
        for j in 0..<N {
            if tomatoCase[i][j] == 0 {
                return -1
            }
            result = max(result, tomatoCase[i][j])
        }
    }
    return result-1
}

bfs()
let answer = checkCase()

print(answer)
