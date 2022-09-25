//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/23.
//

import Foundation

let N = Int(readLine()!)!
let appleNums = Int(readLine()!)!

var board = Array(repeating: Array(repeating: 0, count: N), count: N)
board[0][0] = 1

for _ in 0..<appleNums {
    let temp = readLine()!.split(separator: " ").map { Int(String($0))! }
    board[temp[0]-1][temp[1]-1] = 9
}

let snakeCommmandNums = Int(readLine()!)!
var snakeCommandSeconds = [Int]()
var snakeCommandDirections = [String]()

for _ in 0..<snakeCommmandNums {
    let temp = readLine()!.split(separator: " ").map { String($0) }
    snakeCommandSeconds.append(Int(temp[0])!)
    snakeCommandDirections.append(temp[1])
}

var answer = 0
var commandIndex = 0

// 0:Up, 1:Right, 2:Down, 3:Left
var nowDirection = 1
let direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

var snake = [[0, 0]]

while true {
    
    if snakeCommandSeconds.contains(answer) {
        nowDirection = changeDirection(now: nowDirection, command: snakeCommandDirections[commandIndex])
    }
    
    let head = snake[0]
    
    let newR = head[0] + direction[nowDirection].0
    let newC = head[1] + direction[nowDirection].1
    
    // 벽 체크, 뱀인지 체크
    if !(0..<N).contains(newR) || !(0..<N).contains(newC) || snake.contains([newR, newC]) {
        answer += 1
        break
    }
    
    // 머리에 추가
    snake.insert([newR, newC], at: 0)
    
    // The 9 is an apple
    if board[newR][newC] == 9 {
        board[newR][newC] = 0
        // 사과면 추가된 채로 넘어감
    } else {
        // 사과가 아니면 꼬리를 잘라줌
        let temp = snake[snake.count-1]
        board[temp[0]][temp[1]] = 0
        snake.removeLast()
    }
    
    answer += 1
}

func changeDirection(now: Int, command: String) -> Int {
    
    var result = now
    
    // D는 오른쪽
    if command == "D" {
        if result == 3{
            result = 0
        } else {
            result += 1
        }
    } else {
        if result == 0 {
            result = 3
        } else {
            result -= 1
        }
    }
    commandIndex += 1
    return result
}

print(answer)


