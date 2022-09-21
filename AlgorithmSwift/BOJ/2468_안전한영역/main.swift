func bfs(fieled: [[Int]], N: Int, now: Int) -> Int {
    var fieled = fieled
    var result = 0
    
    for i in 0..<N {
        for j in 0..<N {
            if fieled[i][j] > now {
                result += 1
                
                var stack = [[i, j]]
                fieled[i][j] = 0
                
                while !stack.isEmpty {
                    let node = stack.removeFirst()
                    let dr = [-1, 0, 1, 0]
                    let dc = [0, 1, 0, -1]
                    
                    for i in 0..<4 {
                        let newR = node[0] + dr[i]
                        let newC = node[1] + dc[i]
                        
                        if (0..<N).contains(newR) && (0..<N).contains(newC) && fieled[newR][newC] > now {
                            fieled[newR][newC] = 0
                            stack.append([newR, newC])
                        }
                    }
                }
            }
        }
    }
    
    return result
}

let N = Int(readLine()!)!
var fieled = [[Int]]()

for _ in 0..<N {
    fieled.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

var answer = 0

for i in 0...100 {
    let xfieled = fieled
    
    let nums = bfs(fieled: xfieled, N: N, now: i)
    if answer < nums {
        answer = nums
    }
}

print(answer == 0 ? 1 : answer)
