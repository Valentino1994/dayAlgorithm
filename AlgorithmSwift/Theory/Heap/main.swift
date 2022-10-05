//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/04.
//

import Foundation


func makeMinHeap(arr: [Int]) {
    
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
    
    globalArr = arr
}

func pop(arr: [Int]) -> Int {

    var arr = arr
    
    if arr.isEmpty {
        return 0
    }
    
    let result = arr[0]
    arr[0] = arr[arr.count - 1]
    arr.removeLast()
    
    for i in (0..<arr.count) {
        
        var parentIndex = i
        
        while parentIndex < arr.count {
            let leftIndex = 2 * parentIndex + 1
            let rightIndex = 2 * parentIndex + 2
            
            if (0..<arr.count).contains(leftIndex) && arr[parentIndex] > arr[leftIndex] {
                let temp = arr[parentIndex]
                arr[parentIndex] = arr[leftIndex]
                arr[leftIndex] = temp
                
                if arr[parentIndex] > arr[rightIndex] {
                    let temp = arr[parentIndex]
                    arr[parentIndex] = arr[rightIndex]
                    arr[rightIndex] = temp
                }
                
                parentIndex = leftIndex
                continue
            }
            
            else if (0..<arr.count).contains(rightIndex) && arr[parentIndex] > arr[rightIndex] {
                let temp = arr[parentIndex]
                arr[parentIndex] = arr[rightIndex]
                arr[rightIndex] = temp
                
                parentIndex = rightIndex
                continue
            }
            
            // 바뀌지 않았으면 바로 다음으로 넘어간다.
            break
        }
    }
    
    globalArr = arr
    return result
}

func push(element: Int){
    
    globalArr.append(element)
    makeMinHeap(arr: globalArr)
    
    return
}


var globalArr = [8, 4, 12, 3, 1, 22]
var globalArr1 = [Int]()
print(globalArr)
makeMinHeap(arr: globalArr)
print(globalArr)
print(pop(arr: globalArr))
print(pop(arr: globalArr1))
print(globalArr)
print(push(element: 5))
print(globalArr)


