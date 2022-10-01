//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/01.
//

import Foundation

func solution(_ players:[Int]) -> Int {
    
    var players = players
    var answer = 0
    
    answer = max(answer, countSpecialMatch(nowTree: players))
    
    for i in 0..<players.count {
        if players[i] == 0 {
            players[i] = 1
            let nowTreeInfo = checkDepth(subject: players.count)
            let nowTree = makeTree(nowPlayer: players, treeNodes: nowTreeInfo[1])
            answer = max(answer, countSpecialMatch(nowTree: nowTree))
            players[i] = 0
        }
    }
    
    return answer
}

func checkDepth(subject: Int) -> [Int] {
    
    var answer = 0
    var subject = subject
    var treeNodes = 0
    
    while subject > 0 {
        treeNodes += subject
        answer += 1
        subject /= 2
    }
    
    return [answer, treeNodes]
}

func makeTree(nowPlayer: [Int], treeNodes: Int) -> [Int] {
    print(nowPlayer)
    
    var tree = Array(repeating: 0, count: treeNodes)
    
    var playerIndex = 0
    var treeIndex = treeNodes - nowPlayer.count
    
    while playerIndex < nowPlayer.count {
        tree[treeIndex] = nowPlayer[playerIndex]
        treeIndex += 1
        playerIndex += 1
    }
        
    return tree
}

func countSpecialMatch(nowTree: [Int]) -> Int {
    
    var nowTree = nowTree
    var nodeIndex = nowTree.count - 1
    var count = 0
    
    while nodeIndex >= 2 {
        let rightNode = nowTree[nodeIndex]
        let leftNode = nowTree[nodeIndex - 1]
        let parentNodeIndex = Int((nodeIndex - 2) / 2)
        
        // 둘 다 프로이면
        if (rightNode == 1 && leftNode == 1) {
            count += 1
            nowTree[parentNodeIndex] = 1
        }
        
        else if (rightNode == 0 && leftNode == 0) {
            count += 1
            nowTree[parentNodeIndex] = 0
        }
        
        // 왼쪽만 프로이면
        else if rightNode == 1 || leftNode == 0 {
            count += 1
            nowTree[parentNodeIndex] = 1
        }
        
        // 오른쪽만 프로이면
        else if rightNode == 0 || leftNode == 1 {
            count += 1
            nowTree[parentNodeIndex] = 1
        }
        
        nodeIndex -= 2
    }
    return count
}


let players = [1, 0, 0, 1, 0, 0, 1, 0]
let players1 = [0, 1, 1, 0, 0, 1, 1, 0]
print(solution(players))
print(solution(players1))
