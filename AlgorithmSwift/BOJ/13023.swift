//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/17.
//

import Foundation

var NM: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
let N: Int = NM[0]
let M: Int = NM[1]

// index == node의 번호
// 이 문제는 인덱스가 0부터 시작 (A == 0)
var tree: [[Int]] = Array(repeating: [], count: N)

for _ in 0..<M {
    let nodeInfo: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
    let parent: Int = nodeInfo[0]
    let child: Int = nodeInfo[1]
    
    tree[parent].append(child)
    tree[child].append(parent)
}

var visited: [Bool] = Array(repeating: false, count: N)
var answer: Int = 0

for i in 0..<N {
    if answer == 1 {
        break
    }
    
    visited[i] = true
    dfs(node: i, depth: 0)
    visited[i] = false
}

print(answer)

func dfs(node: Int, depth: Int) {
    
    if depth == 4 {
        answer = 1
        return
    }
    
    for i in 0..<tree[node].count {
        let child: Int = tree[node][i]
        
        if !visited[child] {
            visited[child] = true
            dfs(node: child, depth: depth + 1)
            visited[child] = false
        }
    }
}
