import Foundation

var tc: Int = Int(String(readLine()!))!
var info: [[Character]] = []

var preOrdered: String = ""
var inOrdered: String = ""
var postOrdered: String = ""

// 입력
for _ in 0..<tc {
    let now: [Character] = readLine()!.split(separator: " ").map { Character(String($0)) }
    info.append(now)
}
// tree 만들기
var tree = Array(repeating: [0, 0], count: 27)
for i in 0..<tc {
    let parent: Int = Int(info[i][0].asciiValue!) - 64
    for j in 1..<3 {
        let child: Int = Int(info[i][j].asciiValue!) - 64
        // 범위 연산자 개Cool
        if 0...26 ~= child {
            tree[parent][j-1] = child
        }
    }
}

func preOrder(node: Int) {
    
    if node == 0 {
        return
    }
    
    preOrdered += String((UnicodeScalar(node + 64)!))
    preOrder(node: tree[node][0])
    preOrder(node: tree[node][1])
}

func inOrder(node: Int) {
    
    if node == 0 {
        return
    }
    
    inOrder(node: tree[node][0])
    inOrdered += String((UnicodeScalar(node + 64)!))
    inOrder(node: tree[node][1])
}

func postOrder(node: Int) {
    
    if node == 0 {
        return
    }
    
    postOrder(node: tree[node][0])
    postOrder(node: tree[node][1])
    postOrdered += String((UnicodeScalar(node + 64)!))
}

preOrder(node: 1)
inOrder(node: 1)
postOrder(node: 1)

print(preOrdered)
print(inOrdered)
print(postOrdered)
