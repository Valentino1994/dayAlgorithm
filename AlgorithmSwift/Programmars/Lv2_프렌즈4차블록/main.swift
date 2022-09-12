//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/05.
//

import Foundation

func solution(_ m:Int, _ n:Int, _ board:[String]) -> Int {
    
    // 2차원 배열의 string으로 바꿔줌
    var board = board.map{ Array($0) }
    
    print(type(of: board))
    // 2차원 배열을 돌건데 배열을 아래로 내리고 나서 또 돌려야 함으로 while문을 돌림.
    while true {
        
        for i in 0..<m {
            for j in 0..<n {
                if (board[i][j] == board[i][j+1]) && (board[i][j+1] == board[i+1][j]) && (board[i+1][j] == board[i+1][j+1]) {
                    
                }
            }
        }
    }
    
    
    print(board)
    
    return 0
}


let m = 4
let n = 5
let board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

print(solution(m, n, board))
