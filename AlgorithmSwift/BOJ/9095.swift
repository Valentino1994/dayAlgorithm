import Foundation

var DP: Array = [0, 1, 2, 4]

for i in 4..<11 {
    DP.append(DP[i-1] + DP[i-2] + DP[i-3])
}

var T = Int(readLine()!)!

for j in 0..<T {
    let N:Int = Int(readLine()!)!
    print(DP[N])
}
