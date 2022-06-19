//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/06/19.
//

import Foundation

public func solution(_ M: Int, _ N: Int) -> String {
    let dx = [-1, 0, 1, 0]
    let dy = [0, 1, 0, -1]
    var visited = Array(repeating: Array(repeating: false, count: M), count: N)
    var result = 1
    visited[r][c] = true
    var curD = d
    var curR = r
    var curC = c
    var cnt = 0
    while true{
        //방향전환
        curD -= 1
        if curD == -1 {curD = 3}//북 -> 서
        
        var nx = curR + dx[curD]
        var ny = curC + dy[curD]
        if !visited[nx][ny] && arr[nx][ny] != 1{//청소안했고, 벽이아니라면
            visited[nx][ny] = true
            curR = nx
            curC = ny
            result += 1
            cnt = 0
            continue
        }else{//청소를했거나 벽이면 왼쪽회전만 할테니까 회전수를 늘림
            cnt += 1
        }
        if cnt == 4{
            cnt = 0
            nx = curR - dx[curD]
            ny = curC - dy[curD]
            if arr[nx][ny] != 1{
                curR = nx
                curC = ny
            }else{
                break
            }
        }
    }
    return result
}
var M: Int = 13
var N: Int = 3

print(solution(M, N))

