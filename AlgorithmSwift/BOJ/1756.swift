//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/25.
//

import Foundation

let input = readLine()!.split(separator : " " ).map{Int(String($0))!}
let D = input[0], N = input[1]

let list = readLine()!.split(separator : " " ).map{Int(String($0))!}
var sorted = [Int]()
var a = list[0]
var count = 1

for i in 1..<D {
    if list[i] >= a {
        count += 1
    }else {
        (0..<count).forEach{ _ in
            sorted.append(a)
        }
        a = list[i]
        count = 1
    }
}
if sorted.count != list.count {
    (0..<count).forEach{ _ in
        sorted.append(a)
    }
}
//print(sorted)

let target = readLine()!.split(separator : " " ).map{Int(String($0))!}

var r = sorted.count-1
for q in target {
    
    var l = 0
    while l<=r {
        let mid = (r+l)/2
        
        if sorted[mid] < q {
            r = mid-1
        }else {
            l = mid+1
        }
    }
    if r == -1 {
        r = -2
        break
    }
    r -= 1
}

print(r == -2 ? 0 : r+2 )
