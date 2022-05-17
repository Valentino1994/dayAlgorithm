//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/16.
//

import Foundation

var N: Int = Int(readLine()!)!
var mySet: [Bool] = Array(repeating: false, count: 21)

for _ in 0..<N {
    let commands: [String] = readLine()!.split(separator: " ").map { String($0) }
    let command: String = commands[0]
    
    if commands.count > 1 {
        let nums: Int = Int(commands[1])!
        if command == "add" {
            if !mySet[nums] {
                mySet[nums] = true
            }
            continue
        }
        else if command == "remove" {
            if mySet[nums] {
                mySet[nums] = false
            }
            continue
        }
        else if command == "check" {
            if mySet[nums] {
                print(1)
            } else {
                print(0)
            }
            continue
        }
        else if command == "toggle" {
            if !mySet[nums] {
                mySet[nums] = true
            } else {
                mySet[nums] = false
            }
            continue
        }
    } else {
        if command == "all" {
            mySet = Array(repeating: true, count: 21)
            continue
        }
        else if command == "empty" {
            mySet = Array(repeating: false, count: 21)
            continue
        }
    }
}

