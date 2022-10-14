//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/14.
//

import Foundation

func krusukal(edges: [[Int]]) -> Int {
    var edges = edges
    
    func find_set(x: Int) -> Int{
        if x != p[x] {
            p[x] = find_set(x: p[x])
        }
        return x
    }
    
    func union(x: Int, y: Int) {
        p[find_set(x: y)] = find_set(x: x)
    }
    
    edges = edges.sorted(by: { $0[2] < $1[2] })
    
    var p = Array(repeating: 0, count: V+1)
    
    for i in 0..<V+1 {
        p[i] = i
    }
    
    var connected_edge = 0
    var min_cost = 0
    var index = 0
    
    while connected_edge < V {
        let s = edges[index][0], e = edges[index][1], w = edges[index][2]
        
        if find_set(x: s) != find_set(x: e) {
            union(x: s, y: e)
            connected_edge += 1
            min_cost += w
        }
        if connected_edge == V-1 {
            break
        }
        
        index += 1
    }
    
    return min_cost
}

let VE = readLine()!.split(separator: " ").map{ Int(String($0))! }
let V = VE[0], E = VE[1]
var graph = Array(repeating: Array(repeating: 0, count: V+1), count: V+1)
var edges = [[Int]]()

for _ in 0..<E {
    let FromToWeight = readLine()!.split(separator: " ").map{ Int(String($0))! }
    let From = FromToWeight[0], To = FromToWeight[1], Weight = FromToWeight[2]
    graph[From][To] = Weight
    graph[To][From] = Weight
    edges.append(FromToWeight)
}

print(krusukal(edges: edges))
