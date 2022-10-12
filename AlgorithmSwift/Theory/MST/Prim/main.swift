//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/08.
//

import Foundation

func prim(graph: [[[Int]]], startNode: Int) {
    
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
        for nodeInfo in graph[u] {
            let nodeIndex = nodeInfo[0]
            let nodeEdge = nodeInfo[1]
            // 방문하지 않은 노드이고 현재 가중치가 node에 저장된 가중치보다 작으면 바꿔준다.
            if visited[nodeIndex] == 0 && nodeEdge < d[nodeIndex] {
                d[nodeIndex] = nodeEdge
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
    
    print(S)
    print(d)
}

// Graph를 만드는 방법

// 1. 인접 행렬
// 2. 인접 리스트
// 3. 인접 배열과 해시 테이블
let graph = [
             [[1, 8], [2, 9], [3, 11]],
             [[0, 8], [4, 10]],
             [[0, 9], [3, 11], [4, 5], [5, 12]],
             [[0, 11], [2, 13], [6, 8]],
             [[1, 10], [2, 5]],
             [[2, 12], [6, 7]],
             [[3, 8], [5, 7]]
            ]

prim(graph: graph, startNode: 0)
