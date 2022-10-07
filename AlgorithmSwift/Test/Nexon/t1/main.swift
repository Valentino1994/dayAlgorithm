//
//  t1.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/07.
//

import Foundation

func minNum(samDaily: Int, kellyDaily: Int, difference: Int) -> Int {
    // Write your code here
    var copySamDaily = samDaily + difference
    var copyKellyDaily = kellyDaily
    
    var answer = 1
    
    while copySamDaily >= copyKellyDaily {
        answer += 1
        
        copySamDaily += samDaily
        copyKellyDaily += kellyDaily
    }
    
    return answer
}
let samDaily = 3
let kellyDaily = 5
let difference = 1

print(minNum(samDaily: samDaily, kellyDaily: kellyDaily, difference: difference))
