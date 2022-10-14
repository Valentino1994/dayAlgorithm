//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/08.
//

import Foundation

typealias edge = (Int, String, String)
 
func kruskal(vertices: [String], edges: [edge]) -> [edge] {
    var mst: [edge] = []
    
    var edges = edges.sorted { $0.0 < $1.0 }
    var rank: [String: Int] = [:]
    var parent: [String: String] = [:]
    
    for vertice in vertices {
        rank.updateValue(0, forKey: vertice)
        parent.updateValue(vertice, forKey: vertice)
    }
    
    func find(_ node: String) -> String {
        if node != parent[node]! {               // 루트 노드 찾아야만 재귀 탈출
            parent[node] = find(parent[node]!)
        }
        return parent[node]!
    }
    
    func union(_ nodeV: String, _ nodeU: String) {
        let rankV = find(nodeV)
        let rankU = find(nodeU)
        
        if rankV > rankU {
            parent[rankU] = rankV
        } else {
            parent[nodeV] = nodeU
            if rankV == rankU {
                rank[nodeU]! += 1
            }
        }
    }
    
    while mst.count < (vertices.count - 1) {
        let node = edges.removeFirst()
        if find(node.1) != find(node.2) {
            union(node.1, node.2)
            mst.append(node)
        }
    }
    return mst
}

func krusukal() {
    
    func find_set(x: Int) -> Int{
        if x != p[x] {
            p[x] = find_set(x: x)
        }
        return x
    }
    
    func union(x: Int, y: Int) {
        p[find_set(x: y)] = find_set(x: x)
    }
    
    let VE = readLine()!.split(separator: " ").map{ Int(String($0))! }
    let V = VE[0], E = VE[1]
    
    var graph = Array(repeating: Array(repeating: 0, count: V), count: V)
    var edges = [[Int]]()
    
    for _ in 0..<E {
        let FromToWeight = readLine()!.split(separator: " ").map{ Int(String($0))! }
        let From = FromToWeight[0]-1, To = FromToWeight[1]-1, Weight = FromToWeight[2]
        graph[From][To] = Weight
        graph[To][From] = Weight
        edges.append(FromToWeight)
    }
    
    edges = edges.sorted(by: { $0[2] < $1[2] })
    
    var p = Array(repeating: 0, count: V)
    var connected_edge = 0
    var min_cost = 0
    
    var index = 0
    while connected_edge < V {
        let s = edges[index][0], e = edges[index][1], w = edges[index][1]
        
        if find_set(x: s) != find_set(x: e) {
            union(x: s, y: e)
            connected_edge += 1
            min_cost += w
        }
        
        index += 1
    }
}


//def find_set(x): # 루트 노드 찾기
//    if x != p[x]:
//        return find_set(p[x])
//    else:
//        return x
//
//
//def union(x, y): # 루트 노드 잇기
//    p[find_set(y)] = find_set(x) # y의 루트를 x의 루트로 지정
//
//
//
//for tc in range(1, int(input())+1):
//    V, E = map(int, input().split())
//    graph = [[0] * (V+1) for _ in range(V+1)] # 0~V
//    edges = [] # 간선정보
//
//    for i in range(E): # 인접행렬
//        s, e, w = map(int, input().split())
//        graph[s][e] = w
//        graph[e][s] = w
//        edges.append([s, e, w])
//
//    # 가중치 오름차순
//    edges.sort(key = lambda x : (x[2]))
//
//    # 부모정보 초기화
//    p = list(range(V+1))
//
//    connect_E = 0 # 연결한 엣지 수
//    min_cost = 0 # 최소 가중치
//
//    i = 0
//    while connect_E < V:
//        s, e, w = edges[i]
//
//        if find_set(s) != find_set(e): # 루트노드가 다르면
//            union(s, e)
//            connect_E += 1
//            min_cost += w
//
//        i += 1
//
//    print('#{} {}'.format(tc, min_cost))
