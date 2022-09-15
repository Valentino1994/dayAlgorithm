import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let k = input[0]
let n = input[1]
var lengths: [Int] = []

(0..<k).forEach { _ in
    lengths.append(Int(readLine()!)!)
}

var start = 1
// 랜선의 최고 길이를 구한다.
var end = lengths.max()!
var maxLength = 0

while start <= end {
    
    let mid = (start + end) / 2
    // mid로 나누어 떨어지는 몫 => 해당하는 길이로 자른 랜선의 개수
    // reduce로 개수 모두 합쳐줌
    let lineCount = lengths.map { $0 / mid }.reduce(0, +)
    
    // n개가 넘더라도 완수 조건이기 때문에 max를 수정함.
    if lineCount >= n {
        maxLength = max(maxLength, mid)
    }
    
    // 랜선의 길이를 늘리거나 줄임
    if lineCount < n {
        end = mid - 1
    } else {
        start = mid + 1
    }
}

print(maxLength)
