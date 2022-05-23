import Foundation

let N = Int(readLine()!)!
var arr = [[Int]]()
var result = [Int]()


for _ in 0..<N {
    let x = readLine()!.components(separatedBy: " ").map{Int($0)!}
    arr.append(x)
}

func getStat(count: Int, num: [Int], index: Int) {
    var statArr = num // [1,2]
    
    for i in index..<N-count+1 {
        if count == 1 {
            statArr.append(i+1)
            
            var sum = 0
            for i in 0..<statArr.count-1 {
                for j in i+1..<statArr.count {
                    let a = statArr[i] - 1
                    let b = statArr[j] - 1
                    sum += arr[a][b] + arr[b][a]
                }
            }
            result.append(sum)
            statArr.removeLast()
        } else {
            statArr.append(i+1)
            getStat(count: count-1, num: statArr, index: i+1)
            statArr.removeLast()
        }
    }
}

getStat(count: N/2, num: [], index: 0)

var min = result.max()!
for i in 0..<result.count {
    var sub = 0
    if result[i] > result[result.count-1-i] {
        sub = result[i]-result[result.count-1-i]
        if sub == 0 {
            min = 0
            break
        } else if sub < min {
            min = sub
        }
    } else {
        sub = result[result.count-1-i]-result[i]
        if sub == 0 {
            min = 0
            break
        } else if sub < min {
            min = sub
        }
    }
}

print(min)
