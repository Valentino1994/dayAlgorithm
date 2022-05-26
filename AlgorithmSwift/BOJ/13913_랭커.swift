//
//  13913_랭커.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/26.
//

import Foundation

let inp = readLine()!.split(separator: " " ).map{Int(String($0))!}
let N = inp[0], K = inp[1]
let MX = 100000
var dp = Array(repeating: -1, count: MX+1)
dp[N] = 0
var queue = [N]
var q = 0
while queue.count > q {
    let f = queue[q]
    q += 1
    
    if f == K {
        var ans = [K]
        var k = K
        while k != N {
            ans.append(dp[k])
            k = dp[k]
        }
        var str = ""
        ans.reversed().forEach {
            str += String($0) + " "
        }
        str.removeLast()
        print(ans.count-1)
        print(str)
        break
    }
    
    let list = [f+1, f-1, f*2]
    list.forEach {
        if (0...MX).contains($0), dp[$0] == -1 {
            dp[$0] = f
            queue.append($0)
        }
    }
}
