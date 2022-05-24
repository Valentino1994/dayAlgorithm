//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/23.
//

import Foundation

let NM: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
let N: Int = NM[0]
let M: Int = NM[1]
var tree = Array(repeating: [], count: N+1)
var visited = Array(repeating: false, count: N+1)

for _ in 0..<M {
    let temp: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    tree[temp[0]].append(temp[1])
    tree[temp[1]].append(temp[0])
}

func dfs(node: Int) {
    for it in tree[node] {
        let item: Int = it as! Int
        if !visited[item] {
            visited[item] = true
            dfs(node: item)
        }
    }
}

var answer: Int = 0
for i in 1..<N {
    if !visited[i] {
        visited[i] = true
        answer += 1
        dfs(node: i)
    }
}

print(answer)
