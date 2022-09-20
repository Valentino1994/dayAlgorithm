//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/20.
//

import Foundation

let N = Int(readLine()!)!

var graph = [[Int]]()

for _ in 0..<N {
    graph.append(readLine()!.split(separator: " ").map{ Int(String($0))! })
}

var result = ""

for i in 0..<N {
    var visited = Array(repeating: 0, count: N)
    var stack = [Int]()
    
    for j in 0..<graph[i].count {
        if graph[i][j] == 1 {
            stack.append(j)
        }
    }
    
    while !stack.isEmpty {
        let node = stack.removeFirst()
        visited[node] = 1
        for k in 0..<graph[node].count {
            if graph[node][k] == 1 && visited[k] == 0 {
                stack.append(k)
            }
        }
    }
    
    result += visited.map{ String($0) }.joined(separator: " ")
    result += "\n"
}

result.removeLast()

print(result)
