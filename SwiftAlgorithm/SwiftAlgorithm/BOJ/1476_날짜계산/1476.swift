//
//  main.swift
//  SwiftAlgorithm
//
//  Created by Geunil Park on 2022/04/13.
//

import Foundation

let nums = readLine()!.components(separatedBy: " ")

var x = Int(nums[0])! - 1
var y = Int(nums[1])! - 1
var z = Int(nums[2])! - 1

var answer = 0
while true {
    if (answer % 15 == x && answer % 28 == y && answer % 19 == z) {
        break
    } else {
        answer += 1
    }
}
print(answer + 1)


