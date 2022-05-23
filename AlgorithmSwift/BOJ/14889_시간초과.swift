import Foundation

var N: Int = Int(readLine()!)!
var Matrix: [[Int]] = []

for _ in 0..<N {
    Matrix.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

var visited: [Bool] = Array(repeating: false, count: N)
var result: [[Int]] = []

func dfs(depth: Int, temp: [Int]) {
    var temp: [Int] = temp
    var flag: Bool = false
    if depth == Int(N/2) {
        for arr in result {
            if arr == temp.sorted(by: <) {
                flag = true
                break
            }
        }
        if flag {
            return
        }
        result.append(temp)
        return
    }
    
    for i in 0..<N {
        if !visited[i] {
            visited[i] = true
            temp.append(i)
            dfs(depth: depth + 1, temp: temp)
            visited[i] = false
            temp.removeLast()
        }
    }
}

dfs(depth: 0, temp: [])

func calc(arr: [Int]) -> Int {
    var result: Int = 0
    var opposite: [Int] = []
    
    for i in 0..<N {
        if !arr.contains(i) {
            opposite.append(i)
        }
    }
    
    var a: Int = 0
    var b: Int = 0
    
    for i in 0..<arr.count {
        for j in 0..<arr.count {
            if i != j {
                a += Matrix[arr[i]][arr[j]]
                b += Matrix[opposite[i]][opposite[j]]
            }
        }
    }
    
    result = abs(a - b)
    
    return result
}

var answer: Int = 987654321

for arr in result {
    answer = min(answer, calc(arr: arr))
    if answer == 0 {
        break
    }
}

print(answer)
