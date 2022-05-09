import Foundation

func solution(_ s:String) -> Int {
    if s.count <= 1 {
        return s.count
    }

    var result = s.count
    
    // String을 Character의 배열로 만드는 방법 !
    // Swift에서는 문자열을 자르기가 힘들기 때문에 이렇게 하는 것이 편한듯.
    let ch: [Character] = Array(s)
    let maxPiece = ch.count / 2
    // i는 자르는 크기
    for i in 1 ... maxPiece {
        var length = 0
        var j = 0
        // j는 이동하는 점 (자르는 시작점)
        while j < ch.count {
            // j부터 i만큼의 문자를 잘라야하는데 끝에서는 넘어갈 수 있으니까 3항 연산자로 조건을 걸어둔다.
            let last = j+i < s.count ? j+i: s.count
            
            let current = ch[j..<last]
            var count = 1
            // 시작점 + 자르는 문자열의 크기가 s를 넘어가지 않는다면
            while j + i < s.count {
                
                let tempLast = j+2*i < s.count ? j+2*i : s.count

                if current == ch[j+i..<tempLast] {
                    // 압축이 몇 개 됐는가 ?
                    count += 1
                    // 여기서 하는 점프는 압축이다.
                    j += i
                } else {
                    break
                }
            }
            var digit = 0
            // 압축된 것이 있다면 ?
            if count != 1 {
                while count > 0 {
                    digit += 1
                    // 10개 이상 압축이 됐다면 2자리수, 100개 이상 압축이 됐다면 3자리수가 되니까.
                    count /= 10
                }
            }
            // j는 N * i인데 python이였다면 range(0, len(s), i) 이런식으로 처리했겠지만 Swift에서는 힘들어서 while로 처리함
            // 현재 문자열 + 압축된 문자열의 개수
            length += current.count + digit
            j += i
        }
        result = min(result, length)
    }
    return result
}

var s: String = "aabbaccc"
print(solution(s))
