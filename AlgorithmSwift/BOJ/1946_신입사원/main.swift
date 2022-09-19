//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/16.
//

import Foundation

let T: Int = Int(readLine()!)!

for _ in 0..<T {
    
    let N: Int = Int(readLine()!)!
    
    var list = [[Int]]()
    
    // insert는 또 되네...
//    for _ in 0..<N {
//        list.insert(readLine()!.split(separator: " ").map{ Int(String($0))! }, at: list.endIndex)
//    }
    
    for _ in 0..<N {
        list.append(readLine()!.split(separator: " ").map{ Int(String($0))! })
    }
    
    var testArray: [Int] = []
    for i in 0..<3 {
        testArray.append(contentsOf: (0..<3))
    }
    
//    print(testArray)
    
//    (0..<N).forEach { _ in
//        list.append(readLine()!.split(separator: " ").map{ Int(String($0))! })
//    }
    testArray.forEach { _ in
        print("hi")
    }
    
    let sortedList: [[Int]] = list.sorted(by: { $0[0] < $1[0] })
    
    var nowInterviewRank = sortedList[0]
    
    var answer: Int = 1
    
//    for i in 1..<sortedList.count {
//        if nowInterviewRank > sortedList[i][1] {
//            nowInterviewRank = sortedList[i][1]
//            answer += 1
//        }
//    }
    
    for i in 1..<sortedList.count {
        if sortedList[i][1] < nowInterviewRank[1] {
            answer += 1
            nowInterviewRank = sortedList[i]
        }
    }
    
    print(answer)
}
