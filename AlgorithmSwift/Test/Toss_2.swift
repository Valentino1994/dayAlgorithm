//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/06.
//

import Foundation

func solution(_ commands: [String]) -> [Int] {
    
    var nayeon = [[0, 0]]
    
    for command in commands {
        
        // 나연의 현재 위치는 항상 nayeon 배열의 마지막
        let nowNayoen = nayeon[nayeon.count-1]
        
        // 나연이 오른쪽으로 가는 것은 나연의 현재위치에서 x가 한 칸 오른쪽으로 가는 것
        if command == "FORWARD" {
            
            let nextNayeon = [nowNayoen[0] + 1, nowNayoen[1]]
            nayeon.append(nextNayeon)
        
        // 나연이 왼쪽으로 가는 것은 나연의 현재위치에서 x가 한 칸 왼쪽으로 가는 것
        } else if command == "BACK" && nowNayoen[0] > 0 {
            
            let nextNayeon = [nowNayoen[0] - 1, nowNayoen[1]]
            
            // 하지만 왼쪽으로 가려고 할 때 해당 위치가 nayeon 배열에 들어있지 않다면 이동하지 않음
            if nayeon.contains(nextNayeon) {
                // 이동한다는 것은 현재 위치의 배열을 없앤다는 것임
                nayeon.removeLast()
            }
            
        // 나연이 위로 올라간다는 것은 나연의 현재 위치에서 y이 한 칸 위쪽으로 가는 것
        } else if command == "UP" {
            
            let nextNayeon = [nowNayoen[0], nowNayoen[1] + 1]
            nayeon.append(nextNayeon)
        
        // 나연이 아래로 내려간다는 것은 현재 나연의 위치에 해당하는 row값을 모두 없앤다는 것
        } else if command == "DOWN" && nowNayoen[1] > 0 {
            var index = 0
            for i in 0..<nayeon.count {
                if nayeon[i][1] == nowNayoen[1] {
                    index = i
                    break
                }
            }
            nayeon = Array(nayeon[0..<index])
        }
    }
    return nayeon[nayeon.count-1]
}

let commands = ["FORWARD", "FORWARD", "FORWARD", "UP", "FORWARD", "FORWARD", "DOWN", "BACK", "BACK", "UP", "UP", "FORWARD", "FORWARD", "UP", "FORWARD"]
print(solution(commands))
