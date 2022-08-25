//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/06.
//

import Foundation

func solution(_ plans: [String]) -> Int {
    let myPlans = plans.sorted(by: <)
    var myTimes: [[String]] = []
    
    for plan in myPlans {
        let plan = plan.split(separator: " ")
        let temp = [[calculateTime(String(plan[0])), calculateTime(String(plan[1]))]]
        myTimes.append(contentsOf: temp)
    }
    print(myPlans)
    print(myTimes)
    return 0
}

func calculateTime(_ time: String) -> String {
    let time = time.split(separator: ":")
    let minute = time[0]
    let second = time[1]
    
    return String(Int(minute)! * 60 + Int(second)!)
}

let plans = ["01:00 02:00", "00:00 01:30", "01:30 02:00", "02:00 03:30", "02:30 03:00", "00:30 01:00", "01:00 01:30", "04:30 05:00"]

//solution(plans)
