import Foundation

guard let testCase = readLine(), let testCase = Int(testCase) else { fatalError() }

for _ in 0..<testCase {
    let MNK = readLine()!.split(separator: " ").map { Int(String($0))! }
    let farm: [[Int]] = makeFarm(M: MNK[0], N: MNK[1], K: MNK[2])
    let answer = bfs(farm: farm)
    
    print(answer)
}
    
func makeFarm(M: Int, N: Int, K: Int) -> [[Int]] {
    var farm: [[Int]] = Array(repeating: Array(repeating: 0, count: N), count: M)
    
    for _ in 0..<K {
        let cabbage: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
        farm[cabbage[0]][cabbage[1]] = 1
    }
    
    return farm
}

func bfs(farm: [[Int]]) -> Int {
    
    var farm: [[Int]] = farm
    var count: Int = 0
    
    // 시계 방향
    let dr: [Int] = [-1, 0, 1, 0]
    let dc: [Int] = [0, 1, 0, -1]
    
    for i in 0..<farm.count {
        for j in 0..<farm[0].count {
            if farm[i][j] == 1 {
                var queue: [[Int]] = [[i, j]]
                
                while !queue.isEmpty {
                    let now: [Int] = queue.removeFirst()
                    
                    let nr = now[0]
                    let nc = now[1]
                    
                    for k in 0..<4 {
                        if 0..<farm.count ~= nr + dr[k] && 0..<farm[0].count ~= nc + dc[k] {
                            if farm[nr + dr[k]][nc + dc[k]] == 1 {
                                queue.append([nr + dr[k], nc + dc[k]])
                                farm[nr + dr[k]][nc + dc[k]] = 0
                            }
                        }
                    }
                }
                count += 1
            }
        }
    }
    
    return count
}
