//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/13.
//

import Foundation

func prim2(graph: [[[Int]]], r: Int) {
    
    var copyGraph = graph
    var tree = [[Int]]()
    var d = Array(repeating: 987654321, count: copyGraph.count)
    d[r] = 0
    
    var visited = Array(repeating: 0, count: graph.count)
    
    var deletedIndex = 0
    
    while deletedIndex < copyGraph.count {
        let u = deleteMin()
        for nodeInfo in u {
            let nowNode = nodeInfo[0]
            let nowEdge = nodeInfo[1]
            if visited[nowNode] == 0 && nowEdge < d[nowNode] {
                d[nowNode] = nowEdge
                tree.append(nodeInfo)
            }
        }
    }
    
    // d의 index와 copyGraph의 index가 같지 않음.
    func deleteMin() -> [[Int]] {
        var temp = 987654321
        var result = 0
        for i in 0..<copyGraph.count {
            if visited[i] == 0 {
                if d[i] < temp {
                    temp = d[i]
                    result = i
                }
            }
        }
        visited[result] = 1
        // 삭제 됐다 치고...
        deletedIndex += 1
        return copyGraph[result]
    }
    
    print(d)
    print(tree)
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

prim2(graph: graph, r: 0)
