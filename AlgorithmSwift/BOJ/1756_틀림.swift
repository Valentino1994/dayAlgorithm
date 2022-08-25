//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/25.
//

import Foundation

let DN: [Int] = readLine()!.split(separator: " ").compactMap({ Int(String($0)) })
var oven: [Int] = readLine()!.split(separator: " ").compactMap({ Int(String($0)) })
let pizzas: [Int] = readLine()!.split(separator: " ").compactMap({ Int(String($0)) })

// oven을 거꾸로 보면서 반복문을 한번만 돌릴 수 있도록 하자.
var ovenDepth: Int = DN[0] - 1

var now: Int = oven[0]

for i in 1..<oven.count {
    if oven[i] > now {
        oven[i] = now
    } else {
        now = oven[i]
    }
}

//print(oven)

for pizza in pizzas {

    while ovenDepth > 0 {
        if oven[ovenDepth] >= pizza {
            break
        }
        else {
            ovenDepth -= 1
        }
    }
    
}

if ovenDepth == 0 {
    print(ovenDepth)
} else {
    print(ovenDepth+1)
}

