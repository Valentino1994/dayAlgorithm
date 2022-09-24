//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/24.
//

import Foundation

func solution(_ wall:[String]) -> [[Int]] {
    
    print(wall)
    
    var que = [[wall.count-1, 0]]
    
    while !que.isEmpty {
        let nowHold = que.removeFirst()
        print(nowHold)
    }
    
    return []
}

let wall = ["H.H", ]
