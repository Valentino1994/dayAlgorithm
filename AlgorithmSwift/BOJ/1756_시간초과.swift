//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/25.
//

import Foundation

let DN: [Int] = readLine()!.split(separator: " ").compactMap({ Int(String($0)) })
let oven: [Int] = readLine()!.split(separator: " ").compactMap({ Int(String($0)) })
let pizzas: [Int] = readLine()!.split(separator: " ").compactMap({ Int(String($0)) })

var visited: [Bool] = Array(repeating: false, count: oven.count)

for pizza in pizzas {
    for i in 0..<oven.count {
        // pizza가 oven의 현재 크기보다 작고 & oven의 바닥에 도착하지 않았고 & 그 다음 칸에 pizza가 없을 경우에는 넘어간다.
        if pizza <= oven[i] && i < oven.count - 1 && !visited[i] {
            continue
        }
        
        // 위의 조건을 통과하지 못했다면 pizza가 oven의 현재 깊이의 지름보다 크기 때문에 현재 깊이보다 한 칸 위로 올라가야한다.
        // 이 때 맨 위인지 체크하고 다음 pizza로 넘어간다.
        if i > 0 {
            visited[i-1] = true
            break
        }
    }
}

var answer = -1

for i in 0..<visited.count {
    if visited[i] {
        answer = i + 1
        break
    }
}

if answer == -1 {
    print(0)
} else {
    print(answer)
}
//print(visited)
