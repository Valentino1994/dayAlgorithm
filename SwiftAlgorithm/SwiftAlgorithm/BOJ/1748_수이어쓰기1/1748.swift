//
//  main.swift
//  SwiftAlgorithm
//
//  Created by Geunil Park on 2022/04/20.
//

import Foundation

var num = readLine()!

var answer:Int = 0
var nums_digit:Int = String(num).count - 1
var maximum_nums:Int = pow(10, nums_digit)

print(Int(num)! % Int(maximum_nums))
