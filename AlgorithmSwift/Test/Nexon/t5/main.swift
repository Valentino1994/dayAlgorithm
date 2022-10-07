//
//  t4.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/07.
//

import Foundation

struct MaxHeap<T: Comparable> {
    var heap: Array<T> = []
    
    init(_ data: T) {
        heap.append(data)       // 0번 index 채우기용
        heap.append(data)       // 실제 Root Node 채우기
    }
    
    mutating func insert(_ data: T) {
        if heap.isEmpty {
            heap.append(data)
            heap.append(data)
            return
        }
        heap.append(data)
        
        func isMoveUp(_ insertIndex: Int) -> Bool {
            if insertIndex <= 1 {               // 루트 노드일 때
                return false
            }
            let parentIndex: Int = insertIndex / 2
            return heap[insertIndex] > heap[parentIndex] ? true : false
        }
        
        var insertIndex: Int = heap.count - 1
        while isMoveUp(insertIndex) {
            let parentIndex: Int = insertIndex / 2
            heap.swapAt(insertIndex, parentIndex)
            insertIndex = parentIndex
        }
    }
    
    enum moveDownStatus { case left, right, none }
    
    mutating func pop() -> T? {
        if heap.count <= 1 { return nil }
        
        let returnData = heap[1]
        heap.swapAt(1, heap.count - 1)
        heap.removeLast()
        
        func moveDown(_ poppedIndex: Int) -> moveDownStatus {
            let leftChildIndex = (poppedIndex * 2)
            let rightCildIndex = leftChildIndex + 1
            
            // case1. 모든(왼쪽) 자식 노드가 없는 경우 (완전이진트리는 왼쪽부터 채워지므로)
            if leftChildIndex >= (heap.count) {
                return .none
            }
            
            // case2. 왼쪽 자식 노드만 있는 경우
            if rightCildIndex >= (heap.count) {
                return heap[leftChildIndex] > heap[poppedIndex] ? .left : .none
            }
            
            // case3. 왼쪽 & 오른쪽 자식 노드 모두 있는 경우
            // case 3-1. 자식들이 자신보다 모두 작은 경우
            if (heap[leftChildIndex] < heap[poppedIndex]) && (heap[rightCildIndex] < heap[poppedIndex]) {
                return .none
            }
            
            // case 3-2. 자식들이 자신보다 모두 큰 경우 (왼쪽과 오른쪽 자식 중 더 큰 자식 선별)
            if (heap[leftChildIndex] > heap[poppedIndex]) && (heap[rightCildIndex] > heap[poppedIndex]) {
                return heap[leftChildIndex] > heap[rightCildIndex] ? .left : .right
            }
            
            // case 3-3. 왼쪽 & 오른쪽 중 한 자식만 자신보다 큰 경우
            return heap[leftChildIndex] > heap[poppedIndex] ? .left : .right
        }
        
        var poppedIndex = 1
        while true {
            switch moveDown(poppedIndex) {
            case .none:
                return returnData
            case .left:
                let leftChildIndex = poppedIndex * 2
                heap.swapAt(poppedIndex, leftChildIndex)
                poppedIndex = leftChildIndex
            case .right:
                let rightChildIndex = (poppedIndex * 2) + 1
                heap.swapAt(poppedIndex, rightChildIndex)
                poppedIndex = rightChildIndex
                
            }
        }
    }
    
    func isEmpty() -> Bool {
        return heap.count <= 1 ? true : false
    }
}

struct NodePriority: Comparable {
    static func < (lhs: NodePriority, rhs: NodePriority) -> Bool {
        lhs.priority > rhs.priority
    }
    var node: String = ""
    var priority: Int = 0
}

func dijkstra(graph: [String: [String: Int]], start: String) ->  [String: Int] {
    var distances: [String: Int] = [:]
    var priorityQueue = MaxHeap(NodePriority.init(node: start, priority: 0))
    
    for key in graph.keys {
        let value = key == start ? 0 : 2147483647
        distances.updateValue(value, forKey: key)
    }
    
    while !priorityQueue.isEmpty() {
        guard let popped = priorityQueue.pop() else { break }
        
        if distances[popped.node]! < popped.priority {
            continue
        }
        
        for (node, priority) in graph[popped.node]! {
            let distance = priority + popped.priority
            if distance < distances[node]! {
                distances[node] = distance
                priorityQueue.insert(NodePriority.init(node: node, priority: distance))
            }
        }
    }
    return distances
}

func minCostPath(gNodes: Int, gFrom: [Int], gTo: [Int], gWeight: [Int], x: Int, y: Int) -> Int {
    // Write your code here
    var answer = 0
    var graph = [String: [String: Int]]()
    
    for i in 0..<gNodes {
        if graph[String(i+1)] == nil {
            graph[String(i+1)] = [String: Int]()
        }
    }
    
    for i in 0..<gFrom.count {
        let from = gFrom[i]
        let to = gTo[i]
        let weight = gWeight[i]
        
        if graph[String(from)]![String(to)] == nil {
            graph[String(from)]![String(to)] = weight
            graph[String(to)]![String(from)] = weight
        }
    }
    
    let fromStartToX = dijkstra(graph: graph, start: "1")
    let fromXToY = dijkstra(graph: graph, start: String(x))
    let fromYToG = dijkstra(graph: graph, start: String(y))
    
    answer += fromStartToX[String(x)]!
    answer += fromXToY[String(y)]!
    answer += fromYToG[String(gNodes)]!
    
    return answer
}

let gNodes = 4
let gFrom = [1, 1, 2, 2, 3]
let gTo = [2, 4, 4, 3, 4]
let gWeight = [6, 9, 10, 6, 11]
let x = 2
let y = 3

//print(dijkstra(graph: graph, start: "A"))
print(minCostPath(gNodes: gNodes, gFrom: gFrom, gTo: gTo, gWeight: gWeight, x: x, y: y))
