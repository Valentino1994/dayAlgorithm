
import Foundation


func permute(_ nums: [Int], _ targetNum: Int) -> [[Int]] {
    var result = [[Int]]()
    var visited = [Bool](repeating: false, count: nums.count)
    
    func permutation(_ nowPermute: [Int]) {
        if nowPermute.count == targetNum {
            if nowPermute.sorted() == nowPermute {
                result.append(nowPermute)
                return
            } else {
                return
            }
        }
        for i in 0..<nums.count {
            if visited[i] == true {
                continue
            }
            else {
                visited[i] = true
                permutation(nowPermute + [nums[i]])
                visited[i] = false
            }
        }
    }
    permutation([])
    
    return result
}

var arr:Array = [1]

let input = readLine()!.components(separatedBy: " ")
var N = Int(input[0])!
var M = Int(input[1])!

let underFive = 2...N
for i in underFive {
    arr.append(i)
}

var answer = permute(arr, M)

answer.forEach {
    let stringArray = $0.map { String($0) }
    let ans = stringArray.joined(separator: " ")
    print(ans)
}
