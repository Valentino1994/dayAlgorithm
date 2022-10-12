//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/12.
//

import Foundation

var start = readLine()!.map { String($0) }
var target = readLine()!.map { String($0) }

var answer = 0

while true {
    
    if target.count == start.count {
        if target == start {
            answer = 1
        }
        break
    }
    
    if target[target.count - 1] == "A" {
        target.removeLast()
    } else {
        target.removeLast()
        target = target.reversed()
    }
}


print(answer)
