//
//  t3.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/07.
//

import Foundation

func getMinimumHealth(initial_players: [Int], new_players: [Int], rank: Int) -> Int {
    var answer = 0
    
    var nowPlayers = initial_players.sorted(by: >)
    answer += nowPlayers[rank-1]
    
    for new_player in new_players {
        nowPlayers.append(new_player)
        nowPlayers = nowPlayers.sorted(by: >)
        answer += nowPlayers[rank-1]
    }
    
    return answer
}

let initial_players = [1, 1, 3]
let new_players = [2, 2, 4]
let rank = 2

print(getMinimumHealth(initial_players: initial_players, new_players: new_players, rank: rank))
