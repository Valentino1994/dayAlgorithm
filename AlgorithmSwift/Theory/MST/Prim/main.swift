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
    
    var visited = Array(repeating: 0, count: nodes)
    
    while S.count < nodes {
        let u = extraMin(d: d)
        S.append(u)
        visited[u] = 1
        
        for nodeInfo in graph[u] {
            let nodeIndex = nodeInfo[0]
            let nodeEdge = nodeInfo[1]
            
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


// 1. 현재 정점을 기준으로 갈 수 있는 모든 노드에 각 노드의 가중치를 넣고 저장해둔다.

// 2. 저장된 값 중 최소값의 노드를 꺼낸다.

// 3. 현재 노드에서 갈 수 있는 모든 곳을 본다.

// 4. 모든 곳을 보면서 현재 노드에 저장된 값보다 지금 노드에서 가는 가중치의 값이 더 적다면 이 가중치로 바꿔준다.

// 5.

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
