//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/03.
//

import Foundation

let FSGUD = readLine()!.split(separator: " ").map { Int(String($0))! }
let F = FSGUD[0], S = FSGUD[1], G = FSGUD[2], U = FSGUD[3], D = FSGUD[4]

var visited = Array(repeating: -1, count: F+1)
visited[S] = 0

var stack = [S]
var stackIndex = 0

while stackIndex < stack.count {
    
    let nowNode = stack[stackIndex]
    let left = nowNode + U
    let right = nowNode - D
    
    if (1...F).contains(left) && visited[left] == -1 {
        stack.append(left)
        visited[left] = visited[nowNode] + 1
    }
    
    if (1...F).contains(right) && visited[right] == -1 {
        stack.append(right)
        visited[right] = visited[nowNode] + 1
    }
    
    stackIndex += 1
}

print(visited[G] == -1 ? "use the stairs" : "\(visited[G])")
