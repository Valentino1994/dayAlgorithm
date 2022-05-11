import Foundation

let NK: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
let N: Int = NK[0]
let K: Int = NK[1]

var result: Int = 987654321
var cnt: Int = 0

var visited = Array(repeating: false, count: 100001)
var stack: [Int] = [N]
visited[N] = true

func bfs(now: Int, cnt: Int) {
    let now: Int = now
    
    if cnt > result {
        return
    }
    
    if now == K {
        result = min(result, cnt)
        return
    }
    
    if now - 1 > 0 && !visited[now - 1] {
        visited[now - 1] = true
        bfs(now: now - 1, cnt: cnt + 1)
        visited[now - 1] = false
    }
    if now + 1 <= K && !visited[now + 1] {
        visited[now + 1] = true
        bfs(now: now + 1, cnt: cnt + 1)
        visited[now + 1] = false
    }
    if now * 2 <= K && !visited[now * 2] {
        visited[now * 2] = true
        bfs(now: now * 2, cnt: cnt + 1)
        visited[now * 2] = false
    }
    return
}

bfs(now: N, cnt: 0)
print(result)
