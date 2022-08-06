//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/02.
//

import Foundation

func solution(_ info:[String], _ query:[String]) -> [Int] {
    var result = [Int]()

    let languageQueries: [String] = ["cpp", "java", "python", "-"]
    let jobQueries: [String] = ["backend", "frontend", "-"]
    let carrerQueries: [String] = ["junior", "senior", "-"]
    let foodQueries: [String] = ["pizza", "chicken", "-"]
    
    var queryDictionary = [String: [Int]]()
    
    for languageQuery in languageQueries {
        for jobQuery in jobQueries {
            for carrerQuery in carrerQueries {
                for foodQuery in foodQueries {
                    let queryKey = languageQuery + jobQuery + carrerQuery + foodQuery
                    queryDictionary[queryKey] = []
                }
            }
        }
    }
    
    for candidate in info {
        let candidateInfo = candidate.split(separator: " ")
        
        let candidateLanguages = [candidateInfo[0], "-"]
        let candidateJobs = [candidateInfo[1], "-"]
        let candidateCareeres = [candidateInfo[2], "-"]
        let candidateFoods = [candidateInfo[3], "-"]
        
        for candidateLanguage in candidateLanguages {
            for candidateJob in candidateJobs {
                for candidateCareer in candidateCareeres {
                    for candidateFood in candidateFoods {
                        let key = candidateLanguage + candidateJob + candidateCareer + candidateFood
                        queryDictionary[String(key)]!.append(Int(candidateInfo[4])!)
                    }
                }
            }
        }
    }
    
    for demand in query {
        let demandInfo = demand.replacingOccurrences(of: "and", with: " ").split(separator: " ")
        let key = demandInfo[0] + demandInfo[1] + demandInfo[2] + demandInfo[3]
        let temp = binarySearch(array: queryDictionary[String(key)]!.sorted { $0 < $1 }, target: Int(demandInfo[4])!)
        result.append(temp)
    }
    
    return result
}

func binarySearch(array: [Int], target: Int) -> Int {
    var low = 0
    var high = array.count - 1
    guard array[high] >= target else { return 0 }
    guard array[low] < target else { return array.count }
    while low <= high {
        var mid = (low + high) / 2
        let guess = array[mid]
        if guess == target {
            while mid > 0 && array[mid-1] == guess {
                mid -= 1
            }
            return array.count - mid
        } else if guess > target {
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    return array.count - low
}

let info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

let query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))
