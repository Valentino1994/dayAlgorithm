//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/26.
//

import Foundation

let NK: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
let elder: Int = NK[0]
let younger: Int = NK[1]

var maxIndex: Int = younger > elder ? younger + 1 : elder + 1
var minValue: Int = 987654321
var minCount: Int = 987654321
var minRoute: [Int] = Array(repeating: 0, count: 100001)
var index: Int = 0
var visited: [Bool] = Array(repeating: false, count: 100001)

func dfs(count: Int, nowValue: Int, nowRoute: [Int]) {
    // 백트래킹
    if nowValue > minValue || nowRoute.count > minRoute.count {
        return
    }
    
    if nowValue == younger {
        minCount = min(minCount, count)
        minValue = nowValue
        minRoute = nowRoute
        return
    }
    
    var next: Int = 0
    for i in 0..<3 {
        
        if i == 0 {
            next = nowValue - 1
        } else if i == 1 {
            next = nowValue + 1
        } else {
            next = nowValue * 2
        }
        
        if next < 0 || next > 100000 || visited[next] == true {
            continue
        }
        visited[next] = true
        dfs(count: count + 1, nowValue: next, nowRoute: nowRoute + [next])
        visited[next] = false
    }
}

dfs(count: 0, nowValue: elder, nowRoute: [elder])

print(minCount)
print(minRoute)




