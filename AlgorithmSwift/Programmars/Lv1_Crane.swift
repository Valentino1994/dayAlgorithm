import Foundation

var board: [[Int]] = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
var moves: [Int] = [1,5,3,5,1,2,1,4]

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    
    var answer  = 0
    var li:[Int] = []
    var copyBoard = board
    
    for move in moves {
        for i in 0..<board.count {
            
            let doll = copyBoard[i][move-1]
            
            if doll == 0 {
                continue
            }
            
            else {
                if li.count != 0 && doll == li[li.count-1] {
                    li.removeLast()
                    answer += 2
                    copyBoard[i][move-1] = 0
                } else {
                    li.append(doll)
                    copyBoard[i][move-1] = 0
                }
                break
            }
        }
    }
    return answer
}

print(solution(board, moves))
