//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/04.
//

import Foundation

var arr = [8, 4, 12, 3, 1, 22]

func makeMinHeap(arr: [Int]) -> [Int]{
    
    var arr = arr
    
    for i in stride(from: arr.count-1, to: -1, by: -1) {

        var childIndex = i
        
        while childIndex != 0 {
            
            let parentIndex = i % 2 == 0 ? Int((childIndex - 2) / 2) : Int((childIndex - 1) / 2)
            
            if arr[parentIndex] > arr[childIndex] {
                let temp = arr[parentIndex]
                arr[parentIndex] = arr[childIndex]
                arr[childIndex] = temp
            }
            
            childIndex = parentIndex
            
        }
    }
    
    return arr
}

print(makeMinHeap(arr: arr))
