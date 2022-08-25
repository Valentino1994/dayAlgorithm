import Foundation

var N: Int = 0, M: Int = 0
var used: [Bool] = []
var output: String = ""

func input() {
    guard let input: [Int] = readLine()?.split(separator: " ").compactMap({ Int(String($0)) }) else {
        return
    }
    N = input[0]
    M = input[1]
    used = Array(repeating: false, count: N + 1)
}

func recursionFunc(currentSelected: String, currentLength: Int) {
    if currentLength == M {
        output += currentSelected + "\n"
    }
    else {
        for number in 1...N where !used[number] {
            used[number] = true
            let selected: String
            if currentLength == 0 {
                selected = "\(number)"
            }
            else {
                selected = currentSelected + " \(number)"
            }
            recursionFunc(currentSelected: selected, currentLength: currentLength + 1)
            used[number] = false
        }
    }
}

input()
recursionFunc(currentSelected: "", currentLength: 0)
print(output)
