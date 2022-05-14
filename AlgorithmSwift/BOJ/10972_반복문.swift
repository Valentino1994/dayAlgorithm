//
//  10972_반복문.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/14.
//

import Foundation

let n = Int(readLine()!)!
var nArray = readLine()!.split(separator: " ").map {Int(String($0))!}


if Array(1...n).reversed() == nArray {
    print("-1")
} else {
    outerLoop: for i in (0..<n).reversed() {
        if nArray[i-1] < nArray[i] {
            for j in (0..<n).reversed() {
                if nArray[i-1] < nArray[j] {
                
                    nArray.swapAt(i-1, j)
                    nArray = nArray[...(i-1)] + nArray[i...].reversed()
                    
                    print(nArray.map{String($0)}.joined(separator: " "))
                    break outerLoop
                }
            }
        }
    }
}
