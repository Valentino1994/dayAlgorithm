//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/12.
//

import Foundation

let start = readLine()!.map { String($0) }
let target = readLine()!.map { String($0) }

var answer = false

var targetABCounter = ["A": 0, "B": 0]

for t in target {
    targetABCounter[t]! += 1
}

func dfs(now: [String]) {
    
    var copyNow = now
    
    if now.count == target.count {
        if checkSameString(now: now) {
            answer = true
            return
        }
    }
    
    var nowABCounter = ["A": 0, "B": 0]
    for n in now {
        nowABCounter[n]! += 1
    }
    
    for keyNValue in nowABCounter {
        let key = keyNValue.key
        let value = keyNValue.value
        
        if key == "A" && value < targetABCounter[key]! {
            copyNow.append("A")
            dfs(now: copyNow)
            copyNow = now
        }
        else if key == "B" && value < targetABCounter[key]! {
            copyNow = copyNow.reversed()
            copyNow.append("B")
            dfs(now: copyNow)
            copyNow = now
        }
    }
}

func checkSameString(now: [String]) -> Bool {
    
    let result = true
    
    for i in 0..<target.count {
        if now[i] != target[i] {
            return false
        }
    }
    
    return result
}

dfs(now: start)
print(answer)
