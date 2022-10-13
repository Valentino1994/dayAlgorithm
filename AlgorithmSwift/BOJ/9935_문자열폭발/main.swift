//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/12.
//

import Foundation

var target = readLine()!
var bombStr = readLine()!

while target != "" {
    
    let temp = target.replacingOccurrences(of: bombStr, with: "")
    
    if temp == target {
        break
    }
    
    target = temp
    print(target)
}

if target == "" {
    print("FRULA")
} else {
    print(target)
}
