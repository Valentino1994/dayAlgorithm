//
//  Lv2_후보키.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/29.
//
//  Practice until can solve it only for 30 minutes

import Foundation

func solution(_ relation:[[String]]) -> Int {
    let rowSize = relation.count
    let colSize = relation[0].count

    var resultSet = Set<Int>()

    for bit in 1..<(1<<colSize) {
        var combiSet = Set<String>()
        var isUnique = true

        for r in 0..<rowSize {
            var tmpStr = ""
            for c in 0..<colSize {
                if (bit & (1<<c)) != 0 {
                    tmpStr += relation[r][c]
                }
            }
            if combiSet.update(with: tmpStr) != nil { // set내에 중복 요소 존재
                isUnique = false
                break
            }
        }

        if isUnique && resultSet.filter{ ($0 & bit) == $0 }.isEmpty {
            resultSet.insert(bit)
        }
    }

    return resultSet.count
}

let relations = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relations))

