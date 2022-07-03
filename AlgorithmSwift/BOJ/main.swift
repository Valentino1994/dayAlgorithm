//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/06/27.
//

import Foundation

let t = readLine()!.split(separator: " ").map{Int(String($0))!}
let (n,m) = (t[0],t[1])

var arr = [[Int]]()

for _ in 0..<n {
    arr.append(Array(readLine()!).map{Int(String($0))!})
}

var ans = 0

func dfs() {
    //모든 경우의 수는 2^(n*m)
    for i in 0..<(1 << (n*m)) {
        //i는 0 ~ 1111....1111
        var total = 0
        for row in 0..<n {
            //한 조각의 합
            var rowSum = 0
            for col in 0..<m {
                let idx = row * m + col
                if i & (1 << idx) != 0 {
                    //해당부분이 1 이라면 (가로) rowSum 조각에 편입하고 계산
                    rowSum = rowSum * 10 + arr[row][col]
                } else {
                    //해당부분이 0 이라면 (세로) rowSum 초기화
                    total += rowSum
                    rowSum = 0
                }
            }
            total += rowSum
        }
        
        for col in 0..<m {
            var colSum = 0
            for row in 0..<n {
                let idx = row * m + col
                if i & (1 << idx) == 0 {
                    colSum = colSum * 10 + arr[row][col]
                } else {
                    total += colSum
                    colSum = 0
                }
            }
            total += colSum
        }
        ans = max(ans, total)
    }
    
}

dfs()
print(ans)
