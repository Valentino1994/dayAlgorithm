//
//  main.swift
//  SwiftAlgorithm
//
//  Created by Geunil Park on 2022/04/11.
//

import Foundation

var dwarfs = [Int]()

for _ in 1...9 {
    if let item = readLine(){
            dwarfs.append(Int(item)!)
        }
    }

var sum = 0
for n in dwarfs {
    sum += n
}

dwarfs.sort()

var x = 0
var y = 0
for_loop:
    for i in 0..<9 {
        for j in 0..<9 {
            if (sum - dwarfs[i] - dwarfs[j] == 100) {
                x = i
                y = j
                break for_loop
            }
        }
    }

for i in 0..<9 {
    if (i != x && i != y) {
        print(dwarfs[i])
    }
}
