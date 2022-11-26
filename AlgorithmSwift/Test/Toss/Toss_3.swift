//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/06.
//

import Foundation

func solution(_ memberCount: Int, _ infos: [[Int]]) -> Int {
    var tree = Array(repeating: [Int](), count: memberCount)
    var visited = Array(repeating: 0, count: memberCount)
    
    for info in infos {
        let parent = info[0]
        for i in 1..<info.count {
            tree[parent].append(info[i])
        }
    }
    
    for i in 0..<tree.count {
        for j in 0..<tree[i].count {
            visited[tree[i][j]] += 1
        }
    }
    
    for i in 0..<visited.count {
        if visited[i] > 1 {
            for j in 0..<tree.count {
                if tree[j].contains(i) {
                    visited[j] += 1
                }
            }
        }
    }
    
    var now = [Int]()
    
    for i in 0..<visited.count {
        if visited[i] == 0 {
            now.append(i)
        }
    }
    
    print(tree)
    print(visited)
    
    if now.count > 1 {
        return -1
    } else {
        return now[0]
    }
}

let memberCount = 10
let infos = [[0, 1, 2], [1, 6], [2, 3], [3, 9], [4, 3, 5], [6, 7, 8]]

print(solution(memberCount, infos))
