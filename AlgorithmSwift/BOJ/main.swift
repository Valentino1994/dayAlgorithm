import Foundation

let LC = readLine()!.split(separator: " ").map{ Int(String($0))! }
let char = readLine()!.split(separator: " ").map{ String($0) }.sorted(by: <)

let L = LC[0]
let C = LC[1]

var result: [String] = []
var visited = Array(repeating: false, count: C)
var answer: [String] = []
func dfs(depth: Int, start: Int) -> Void {
    
    var count: Int = 0
    var alpha: Bool = false
    
    if depth == L {
        for i in 0..<L {
            if result[i] == "a" || result[i] == "i" || result[i] == "u" || result[i] == "e" || result[i] == "o" {
                alpha = true
                continue
            } else {
                count += 1
            }
        }
        
        if alpha && count >= 2 {
            print(result.joined())
        }
        return
    }
    // 뒤로만 가야하니까
    for i in start..<C {
        if !visited[i] {
            visited[i] = true
            result.append(char[i])
            dfs(depth: depth + 1, start: i)
            visited[i] = false
            result.removeLast()
        }
    }
}

dfs(depth: 0, start: 0)


