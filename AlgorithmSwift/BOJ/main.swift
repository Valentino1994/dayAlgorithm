//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/25.
//

import Foundation

var T: Int = Int(readLine()!)!
var graph: [[Int]] = []
var visited: [Int] = []
var flag: Bool = true

for _ in 0..<T {
    let VM: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    let V: Int = VM[0]
    let M: Int = VM[1]
    
    graph = Array(repeating: [], count: V+1)
    visited = Array(repeating: 0, count: V+1)
    
    for _ in 0..<M {
        let info: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
        let parent: Int = info[0]
        let child: Int = info[1]
        
        graph[parent].append(child)
        graph[child].append(parent)
    }
    
    flag = true
    
    for i in 1..<V {
        dfs(now: 1, node: i)
    }
    
    if flag {
        print("YES")
    } else {
        print("NO")
    }
}

func dfs(now: Int, node: Int) {
    
    if visited[node] != 0 {
        return
    }
    
    visited[node] = now
    let nowNode: [Int] = graph[node]
    
    for i in 0..<nowNode.count {
        if visited[nowNode[i]] == 0 {
            if now == 1 {
                dfs(now: 2, node: nowNode[i])
            } else {
                dfs(now: 1, node: nowNode[i])
            }
        } else if visited[nowNode[i]] == now {
            flag = false
        }
    }
}
