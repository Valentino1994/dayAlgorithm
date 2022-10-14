//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/14.
//

import Foundation

func prim(graph: [[Int]], startNode: Int) -> Int {

    var S = [Int]()
    let nodes = graph.count
    // 0. 초기화
    var d = Array(repeating: 987654321, count: nodes)
    d[startNode] = 0
    
    // 방문한 곳은 또 가지 않는다.
    var visited = Array(repeating: 0, count: nodes)
    while S.count < nodes {
        // u는 현재 노드의 거리 중에 가장 짧은 가중치를 가진 노드를 찾는다.
        let u = extraMin(d: d)
        S.append(u)
        visited[u] = 1
        // 그 가중치를 가진 노드와 연결된 노드를 돌면서
        for i in 0..<graph[u].count {
            let nodeIndex = i
            let nodeEdge = graph[u][i]
            
            if nodeEdge != 0 {
                // 방문하지 않은 노드이고 현재 가중치가 node에 저장된 가중치보다 작으면 바꿔준다.
                if visited[nodeIndex] == 0 && nodeEdge < d[nodeIndex] {
                    d[nodeIndex] = nodeEdge
                }
            }
        }
    }
    
    func extraMin(d: [Int]) -> Int {
        var result = 987654321
        var now = -1
        for i in 0..<d.count {
            if visited[i] == 0 {
                if d[i] < result {
                    result = d[i]
                    now = i
                }
            }
        }
        
        return now
    }
    
    return d.reduce(0, +)
}

let VE = readLine()!.split(separator: " ").map{ Int(String($0))! }
let V = VE[0], E = VE[1]

var graph = Array(repeating: Array(repeating: 0, count: V), count: V)
//
for _ in 0..<E {
    let FromToWeight = readLine()!.split(separator: " ").map{ Int(String($0))! }
    let From = FromToWeight[0] - 1, To = FromToWeight[1] - 1, Weight = FromToWeight[2]
    
    graph[From][To] = Weight
    graph[To][From] = Weight
    
}

print(prim(graph: graph, startNode: 0))
