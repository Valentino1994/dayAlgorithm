//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/05/08.
//

import Foundation

func solution(_ fees:[Int], _ records:[String]) -> [Int] {
    
    let basicTime = fees[0] // 180
    let basicFee = fees[1] // 5000
    let unitTime = fees[2] // 10
    let unitFee = fees[3] // 600
    
    var result: [Int] = []
    var recordDict: [Int:[Int]] = [:]
    
    for record in records {
        let temp: [String] = record.split(separator: " ").map{String($0)}
        let time: Int = calTime(time: temp[0])
        let carName: Int = Int(temp[1])!
        
        if recordDict[carName] == nil {
            recordDict[carName] = [time]
        } else {
            recordDict[carName]!.append(time)
        }
    }
    
    var tempResult: [[Int]] = []
    
    for (key, value) in recordDict {
        var tempSum: Int = 0
        var temp: [Int] = value
        if temp.count % 2 == 1 {
            temp.append(calTime(time: "23:59"))
        }
        
        var index: Int = 0
        while index < temp.count {
            tempSum += (temp[index + 1] - temp[index])
            index += 2
        }
        tempResult.append([key, calScore(time: tempSum - basicTime, basicFee: basicFee, unitTime: unitTime, unitFee: unitFee)])
    }
    
    let tempResults = tempResult.sorted(by: { $0[0] < $1[0] })
    
    for tempResult in tempResults {
        result.append(tempResult[1])
    }
    
    return result
}

func calTime(time: String) -> Int {
    var result: Int = 0
    
    let temp: [Int] = time.split(separator: ":").map { Int($0) ?? 0 }
    
    result += (temp[0] * 60)
    result += temp[1]
    
    return result
}

func calScore(time: Int, basicFee: Int, unitTime: Int, unitFee: Int) -> Int {
    var result: Int = basicFee
    
    if time > 0 {
        if time % unitTime != 0 {
            result += Int((time / unitTime + 1) * unitFee)
        } else {
            result += Int(time / unitTime * unitFee)
        }
    }
    return result
}

var fees:[Int] = [120, 0, 60, 591]
var records:[String] = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees, records))
