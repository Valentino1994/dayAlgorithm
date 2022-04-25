import Foundation

var DP: Array = [0, 1, 2, 4]

func makeTable(n: Int) {
    if DP[n] {
        return DP[n]
    }
    else {
        DP[n] = makeTable(n: n-1) + makeTable(n: n-2) + makeTable(n: n-3)
    }
}

makeTable(n: 10)

var T:int = readLine()!

for 0..<T {
    var N:int = readLine()!
    print(DP[N])
}

