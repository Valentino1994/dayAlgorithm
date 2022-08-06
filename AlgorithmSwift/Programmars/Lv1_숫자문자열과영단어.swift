//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/01.
//

import Foundation

func solution(_ s:String) -> Int {
    var result = s
    let numberDictionary = ["one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"]
    
    for number in numberDictionary {
        result = result.replacingOccurrences(of: number.key, with: number.value)
    }
    
    return Int(result)!
}

let s = "one4seveneight"
print(solution(s))
