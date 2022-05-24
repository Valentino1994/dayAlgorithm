//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/24.
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

var queue: [Int] = [1]
var index: Int = 0
var answer: Int = 0

func bfs(node: Int) {
    var queue: [Int] = [node]
    var index: Int = 0
    while index < queue.count {
        
        let now: Int = queue[index]
        
        for it in tree[now] {
            let item: Int = it as! Int
            if !visited[item] {
                visited[item] = true
                queue.append(item)
            }
        }
        index += 1
    }
}

for i in 1...N {
    if !visited[i] {
        answer += 1
        visited[i] = true
        bfs(node: i)
    }
}

print(answer)
