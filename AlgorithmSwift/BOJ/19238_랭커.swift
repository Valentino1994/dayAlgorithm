//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/08/30.
//

//input
var t = readLine()!.split(separator: " ").map{Int(String($0))!}
let (n,m,o) = (t[0],t[1],t[2])

var graph = [[Int]]()

for _ in 0..<n {
    let t = readLine()!.split(separator: " ").map{Int(String($0))!}
    graph.append(t)
}

t = readLine()!.split(separator: " ").map{Int(String($0))!}

var (row,col) = (t[0]-1,t[1]-1)
var info: [[Int]: [Int]] = [:]

for i in 0..<m {
    t = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (sr,sc,dr,dc) = (t[0] - 1,t[1] - 1,t[2] - 1,t[3] - 1)
    graph[sr][sc] = 10
    info[[sr,sc]] = [dr,dc]
}

//현재위치에서 가장 가까운 출발지/ 목적지를 찾는다.
func bfs(_ x: Int, _ y: Int, _ type: String) -> (Int,Int,Int){
    let dx = [1,-1,0,0]
    let dy = [0,0,1,-1]

    var visited = Array(repeating: Array(repeating: false, count: n), count: n)
    visited[x][y] = true
    var queue = [(x,y,0)]
    var idx = 0

    //row, col, dist
    var target = (-1,-1,1000)

    while queue.count > idx {
        let cur = queue[idx]
        idx += 1

        //출발지를 찾는 함수일 경우, 가장 작은 번호의 출발지를 선택하자
        if type == "find" {
            //현재 구한거보다 거리가 더 크면 리턴
            if cur.2 > target.2 {
                //print("출발지는 \((target.0, target.1, target.2))")
                return (target.0, target.1, target.2)
            }

            let num = graph[cur.0][cur.1]

            //1.최단거리, 2. 행번호, 3. 열번호
            if num > 1 {
                if cur.2 == target.2 {
                    if cur.0 == target.0 {
                        //열번호가 더 작다면..!
                        if cur.1 < target.1 {
                            target = cur
                        }
                    } else {
                        if cur.0 < target.0 {
                            target = cur
                        }
                    }
                } else {
                    if cur.2 < target.2 {
                        target = cur
                    }
                }
            }

        }
        //목적지 찾는 함수일 경우
        else {
            let des = info[[x,y]]!
            if [cur.0, cur.1] == des {
                //print("목적지는 des: \(des)")
                //출발지와 목적지를 지우자
                graph[x][y] = 0
                info[[x,y]] = nil
                return cur
            }
        }


        for i in 0..<4 {
            let (nx,ny) = (cur.0 + dx[i], cur.1 + dy[i])
            if (0..<n).contains(nx) && (0..<n).contains(ny) && graph[nx][ny] != 1 && !visited[nx][ny]{
                queue.append((nx,ny,cur.2+1))
                visited[nx][ny] = true
            }
        }
    }

    return target
    //return (-1,-1,-1)
}

var dist = 0
var oil = o

for _ in 0..<m {
    //1 가장 가까운 출발지를 찾는다
    (row,col,dist) = bfs(row,col,"find")
    oil -= dist
    //error1 : 기름이 부족함
    if oil < 0 {
        oil = -1
        break
    }
    //error2 : 출발지에 도달할 수 없음.
    if row == -1 {
        oil = -1
        break
    }
    //print("oil: ",oil)

    //정상적인  결과
    //2 찾은 출발지로 이동한다.
    (row,col,dist) = bfs(row,col,"move")
    oil -= dist

    if oil < 0 {
        oil = -1
        break
    }

    if row == -1 {
        oil = -1
        break
    }

    oil += dist * 2

    //print("oil: ",oil)
    
}

print(oil)
