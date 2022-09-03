//
//  Lv2_괄호변환.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/01.
//

import Foundation

extension String {
    func split(at index: Int) -> [String] {
        let pivot = self.index(self.startIndex, offsetBy: index)
                // 앞에서 pivot까지를 뽑아줌
        let u = self.prefix(upTo: pivot)
                // pivot에서 끝까지를 뽑아줌
        let v = self.suffix(from: pivot)

        return [String(u), String(v)]
    } 
}

func divide(_ p: String) -> [String] {
    var openCount = 0
    var closeCount = 0

    for c in p {
                // 시작점이 아닌데 openCount와 closeCount가 같아졌다면 더이상 분리할 수 없는 괄호의 index이다.
        if openCount != 0 && openCount == closeCount {
            break
        }

        if c == "(" {
            openCount += 1
        } else {
            closeCount += 1
        }
    }

    return p.split(at: openCount + closeCount)
}

func convert(_ p: String) -> String {
    return p.reduce("") { $0 + ($1 == "(" ? ")" : "(") }
}

func isCorrect(_ p: String) -> Bool {
    var count = 0

    for (index, item) in p.enumerated() {
                // 첫번째인데 닫는 괄호면 무조건 끝남
        if index == 0 && item == ")" {
            return false
        } 
                
        count += item == "(" ? 1 : -1
    }
        
        // 닫는 괄호와 여는 괄호의 짝이 맞지 않으면 count가 0이 아님으로 false, 짝이 맞으면 true가 되도록 위에서 코드를 짜뒀음.
    return count == 0
}

func solution(_ p: String) -> String {
    var answer = ""
    
    // 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if !p.isEmpty {
        // 2. 문자열 w를 두 균형잡힌 문자열 u, v로 분리합니다. 단 u는 더 이상 분리할 수 없어야합니다.
        let dividedStrings = divide(p)

        var u = dividedStrings[0]
        let v = dividedStrings[1]
        
        // 3. 문자열 u가 올바른 괄호 문자열이라면 answer에는 u를 붙이고 v에 대해서는 다시 수행합니다.
        if isCorrect(u) {
            answer += u
            answer += solution(v)
        // 4. 문자열 u가 올바른 괄호 문자열이 아닐 경우.
        } else {
            //4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
            var emptyString = "("
            //4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 붙입니다.
            emptyString += solution(v)
            //4-3. ')'를 다시 붙입니다..
            emptyString += ")"
            //4-4. u의 첫번째와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
            u.removeFirst()
            u.removeLast()
            emptyString += convert(u)
            // 4-5 생성된 문자열을 반환합니다.
            answer += emptyString
        }
    }

    return answer
}
