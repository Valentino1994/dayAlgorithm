import Foundation

let arr1 = readLine()!.split(separator: " ").map{Int(String($0))!}
let arr2 = readLine()!.split(separator: " ").map{Int(String($0))!}.sorted(by: <)
let N = arr1[0]
let M = arr1[1]

var visited = Array(repeating: false, count: N + 1)
var depth = 0
var result: [Int] = []

func dfs(_ depth: Int) {
    if depth == M {
        print(result.map{String($0)}.joined(separator: " "))
        return
    }
    
    for i in 0..<N{
        if !visited[i] {
            visited[i] = true
            result.append(arr2[i])
            dfs(depth + 1)
            visited[i] = false
            result.removeLast()
        }
    }
}

dfs(0)
