import Foundation

struct Node {
    let current: Int
    let maxIntensity: Int
}

//해당 경로와 해당 경로까지 도달했을때의 최대 intensity 저장용

func solution(_ n:Int, _ paths:[[Int]], _ gates:[Int], _ summits:[Int]) -> [Int] {

    var dict: [Int:[[Int]]] = [:] //start 지점, [end 지점, intensity]
    var summitsSet = Set([Int]())
    var gatesSet = Set([Int]())
    // 어떤 노드로 갈 수 있는 가장 큰 값
    var maxIntensities = Array(repeating: Int.max, count: n+1)
    var queue: [Node] = []

    for path in paths {
        dict[path[0], default: []].append([path[1], path[2]])
        dict[path[1], default: []].append([path[0], path[2]])
    }

    for gate in gates {
        gatesSet.insert(gate)
    }

    for summit in summits {
        summitsSet.insert(summit)
    }

    var result = [Int.max, Int.max]

    func checkNode(_ node: Node) {
        if summitsSet.contains(node.current) || node.maxIntensity > maxIntensities[node.current] {
            return
        }//봉우리거나 기존의 maxIntensity보다 크면 check할 필요가 없음
        
        // 현재 node에서 갈 곳이 있으면 감
        if dict[node.current] != nil {
            // 현재 node에서 갈 수 있는 모든 node를 봄
            for i in dict[node.current]! {
                // 다음으로 갈 곳이 출구가 아니라면 보기 시작함
                if !gatesSet.contains(i[0]) {
                    // 현재 node의 큰 값과 다음 갈 곳의 w 중에 큰 값
                    let maxIntensity = max(node.maxIntensity, i[1])
                    //  현재 저장해 놓은 다음 갈 곳의 node 위치로 가는 값의 최댓값보다 현재 값이 작을때만 본다.
                    if maxIntensity < maxIntensities[i[0]] {
                        // 다음갈 곳이 봉우리라면
                        if summitsSet.contains(i[0]) {
                            // 같은 maxIntensity 값일 때는 더 작은 번호의 봉우리로 감
                            if maxIntensity == result[1] {
                                result[0] = min(result[0], i[0])
                            // 결과의 maxIntensity가 기존의 result Intensity보다 더 작으면 넣어줌
                            } else if maxIntensity < result[1] {
                                result = [i[0], maxIntensity]
                            }
                        }
                        // 다음 값
                        maxIntensities[i[0]] = maxIntensity
                        queue.append(Node(current: i[0], maxIntensity: maxIntensity))
                    }
                }
            }
        }
    }

    func bfs() {
        while !queue.isEmpty {
            let element = queue.removeFirst()
            checkNode(element)
        }
    }

    for gate in gates {
        queue.append(Node(current: gate, maxIntensity: -1))
        bfs()
    }

    return result
}
