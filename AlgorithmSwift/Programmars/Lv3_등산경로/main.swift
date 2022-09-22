//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/22.
//

import Foundation

func solution(_ n:Int, _ paths:[[Int]], _ gates:[Int], _ summits:[Int]) -> [Int] {
    
    var intensity = 987654321
    let summits = summits.map { $0 - 1 }
    let gates = gates.map { $0 - 1 }
    var graph = Array(repeating: Array(repeating: 0, count: n), count: n)
    var visited = Array(repeating: 0, count: n)
    
    for path in paths {
        let i = path[0]-1, j = path[1]-1, w = path[2]
        // 양방향 그래프를 그려준다.
        graph[i][j] = w
        graph[j][i] = w
    }
    
    for gate in gates {
        dfs(nowRoute: [gate], nowIntensities: [], checkSummit: false, visited: visited)
    }
    
    func dfs(nowRoute: [Int], nowIntensities: [Int], checkSummit: Bool, visited: [Int]) {
        
        // 다시 출구가 나왔으면 return 조건임
        if nowRoute.count > 1 && gates.contains(nowRoute.last!) {
            // intensity를 갱신한 후 순회 끝냄
            
            if checkSummit {
                print("-----")
                print(nowRoute)
                print(nowIntensities)
                let nowIntensity = nowIntensities.max()!
                intensity = min(intensity, nowIntensity)
            }
            return
        }
        var visited = visited
        // 종료조건이 아니라면 돌아봐야함
        var copyRoute = nowRoute
        var copyIntensities = nowIntensities
        var copyCheckSummit = checkSummit
        var justMadeTrueSummit = false
        // 현재 node에서 갈 수 있는 모든 경로를 간다.
        // i는 node의 번호
        for i in 0..<graph[nowRoute.last!].count {
            if visited[i] == 0 && graph[nowRoute.last!][i] != 0 {
                copyIntensities.append(graph[nowRoute.last!][i])
                copyRoute.append(i)
                if summits.contains(i) {
                    if copyCheckSummit {
                        return
                    }
                    copyCheckSummit = true
                    justMadeTrueSummit = true
                }
                visited[i] = 1
                dfs(nowRoute: copyRoute, nowIntensities: copyIntensities, checkSummit: copyCheckSummit, visited: visited)
                visited[i] = 0
                copyRoute.removeLast()
                copyIntensities.removeLast()
                if justMadeTrueSummit {
                    copyCheckSummit = false
                }
            }
        }
    }
    
    print(intensity)
    print(graph)
    
    return []
}

let n = 6
let paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
let gates = [1, 3]
let summits = [5]


let n1 = 7
let paths1 = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
let gates1 = [1]
let summits1 = [2, 3, 4]

//solution(n, paths, gates, summits)
solution(n1, paths1, gates1, summits1)
