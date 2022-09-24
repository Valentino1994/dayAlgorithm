//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/24.
//

import Foundation

func solution(_ queries:[[Int]]) -> Int {
    
    // the biggest array is 1000
    // the itmes[0] is a size of buffer and items[1] is a number of items
    var everyArray = Array(repeating: [0, 0], count: 1001)
    
    for query in queries {
        let arrayIndex = query[0]
        let arrayItems = query[1]
        
        print(2^2)
        let sizeOfbuffer = everyArray[arrayIndex][0]^2
        let sumItems = everyArray[arrayIndex][1] + arrayItems
        
        
        if everyArray[arrayIndex][0] == 0 {
            everyArray[arrayIndex][0] = howManyTwo(arrayItems)
            everyArray[arrayIndex][1] = arrayItems
            continue
        }
        
        if sumItems > sizeOfbuffer {
            
        }
    }
    
    return -1
}

func howManyTwo(_ number: Int) -> Int {
    var copyNumber = number
    var result = 0
    
    while copyNumber > 2 {
        result += 1
        copyNumber /= 2
    }
    
    return result + 1
}

let queries = [[1, 12]]
solution(queries)
