import Foundation

let arr = readLine()!.split(separator: " ").map{Int(String($0))!}
let n = arr[0]
let m = arr[1]

var visited = Array(repeating: false, count: n + 1)
var depth = 0
var result: [Int] = []

func dfs(_ depth: Int){
    if depth == m {
        print(result.map{String($0)}.joined(separator: " "))
        return
    }
    for i in 1...n{
        if result.count == 0 {
            result.append(i)
            dfs(depth + 1)
            result.removeLast()
        }
        
        else if result[result.count-1] <= i {
            result.append(i)
            dfs(depth + 1)
            result.removeLast()
        }
    }
}

dfs(depth)
