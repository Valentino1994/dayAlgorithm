//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/01.
//

import Foundation

func solution(_ compressed:String) -> String {
    var answer = ""
    
    let compressed = Array(compressed)
    
    var stack = [String]()
    
    for str in compressed {
        
        if str == "(" {
            stack.append("*")
            continue
        }
        
        if str.isNumber {
            if !stack.isEmpty && stack[stack.count-1].allSatisfy({ $0.isNumber }) {
                stack[stack.count-1] = stack[stack.count-1] + String(str)
                continue
            }
            stack.append(String(str))
            continue
        }
        
        // 닫는 괄호라면 가장 위의 문자열과 그 문자열 아래의 숫자를 곱해줌
        if str == ")" {
            if stack.count > 1 && stack[stack.count-1].allSatisfy({ $0.isLetter }) {
                let nowStr = stack.removeLast()
                let nowTemp = stack.removeLast()
                let nowInt = stack.removeLast()
                stack.append(String(repeating: nowStr, count: Int(nowInt)!))
                // 계산된 문자열을 stack에 넣었을 때
                if stack.count > 2 {
                    if stack[stack.count-1].allSatisfy({ $0.isLetter }) && stack[stack.count-2].allSatisfy({ $0.isLetter }) {
                        let endOfStack = stack.removeLast()
                        stack[stack.count-1] = stack[stack.count-1] + endOfStack
                    }
                }
            }
            // String이라면
        } else if str.isLetter {
            if stack.isEmpty {
                stack.append(String(str))
            }
            else if !stack.isEmpty {
                if stack[stack.count-1].allSatisfy({ $0.isLetter }) {
                    stack[stack.count-1] = stack[stack.count-1] + String(str)
                } else {
                    stack.append(String(str))
                }
            }
        }
    }
    
    while !stack.isEmpty {
        var now = stack.removeFirst()
        if now.allSatisfy({ $0.isLetter }) {
            answer += now
        }
    }
    
    return answer
}

let compressed = "p"
print(solution(compressed))
