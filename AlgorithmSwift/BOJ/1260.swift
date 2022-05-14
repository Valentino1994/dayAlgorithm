//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/14.
//

import Foundation

let NMV: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
var info: [[Int]] = []

var N: Int = NMV[0]
var M: Int = NMV[1]
var V: Int = NMV[2]

for _ in 0..<M {
    let now: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
    info.append(now)
}

var temp: [[Int]] = Array(repeating: [], count: N+1)

for i in 0..<info.count {
    let parent: Int = info[i][0]
    let child: Int = info[i][1]
    
    temp[parent].append(child)
    temp[child].append(parent)
}

var tree: [[Int]] = temp.map({$0.sorted(by: <)})

var dfs_visited: [Bool] = Array(repeating: false, count: N + 1)
var dfs_stack: [Int] = [V]

func dfs(node: Int) {
    
    if dfs_visited[node] {
        return
    }
    
    dfs_visited[node] = true
    
    for i in 0..<tree[node].count {
        let now: Int = tree[node][i]
        
        if !dfs_visited[now] {
            dfs_stack.append(now)
            dfs(node: now)
        }
    }
}

dfs(node: V)

var bfs_visited: [Bool] = Array(repeating: false, count: N + 1)
var bfs_stack: [Int] = [V]
var bfs_index: Int = 0
bfs_visited[V] = true

while bfs_index < bfs_stack.count {
    
    let now: Int = bfs_stack[bfs_index]
    
    let node: [Int] = tree[now]

    for i in 0..<node.count {
        let n = node[i]
        if !bfs_visited[n] {
            bfs_stack.append(n)
            bfs_visited[n] = true
        }
    }
    bfs_index += 1
}

print(dfs_stack.map { String($0) }.joined(separator: " "))
print(bfs_stack.map { String($0) }.joined(separator: " "))
