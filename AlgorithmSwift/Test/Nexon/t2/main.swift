//
//  t2.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/07.
//

import Foundation

func getMaximumRemovals(order: [Int], source: String, target: String) -> Int {
    var answer = 0
    
    let order = order
    var source = Array(source)
    let target = Array(target)
    
    if source.count <= target.count {
        return answer
    }
    for num in order {
        source[num-1] = "-"
        var sourceIndex = 0
        var targetIndex = 0
        
        while targetIndex < target.count {
            let nowTarget = target[targetIndex]
            var flag = false
            while sourceIndex < source.count {
                if nowTarget == source[sourceIndex] {
                    sourceIndex += 1
                    targetIndex += 1
                    flag = true
                    break
                } else {
                    sourceIndex += 1
                }
            }
            
            if !flag {
                break
            }
        }
        
        if targetIndex == target.count {
            answer += 1
        } else {
            return answer
        }
    }
    
    return answer
}

let order = [7, 1, 2, 5, 4, 3, 6]
let source = "abbabaa"
let target = "bb"

print(getMaximumRemovals(order: order, source: source, target: target))
