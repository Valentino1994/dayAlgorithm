//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/01.
//

import Foundation

func solution(_ arr:[Int]) -> Int {
    
    var arr = arr.map { Array(String($0)).sorted(by: <) }
    var arr2 = arr.map { $0.map{ String($0) }.joined() }
    
    return Set(arr2).count
}

let arr = [112, 1814, 121, 1481, 1184]
print(solution(arr))

