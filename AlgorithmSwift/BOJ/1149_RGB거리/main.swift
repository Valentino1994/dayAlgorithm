//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/28.
//

import Foundation

let N = Int(readLine()!)!
var streets = [[Int]]()

for _ in 0..<N {
    streets.append(readLine()!.split(separator: " ").map{ Int(String($0))! })
}

for i in 1..<N {
    for j in 0..<3 {
        var temp = [Int]()
        for k in 0..<3 {
            if j != k {
                temp.append(streets[i-1][k])
            }
        }
        streets[i][j] = streets[i][j] + temp.min()!
    }
}

print(streets[N-1].min()!)
