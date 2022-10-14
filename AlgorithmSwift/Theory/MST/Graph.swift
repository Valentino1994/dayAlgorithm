//
//  Graph.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/10/14.
//

import Foundation

// Undirected edge
public struct Edge<T>: CustomStringConvertible {
  public let vertex1: T
  public let vertex2: T
  public let weight: Int

  public var description: String {
    return "[\(vertex1)-\(vertex2), \(weight)]"
  }
}

// Undirected weighted graph
public struct Graph<T: Hashable>: CustomStringConvertible {

  public private(set) var edgeList: [Edge<T>]
  public private(set) var vertices: Set<T>
  public private(set) var adjList: [T: [(vertex: T, weight: Int)]]

  public init() {
    edgeList = [Edge<T>]()
    vertices = Set<T>()
    adjList = [T: [(vertex: T, weight: Int)]]()
  }

  public var description: String {
    var description = ""
    for edge in edgeList {
      description += edge.description + "\n"
    }
    return description
  }

  public mutating func addEdge(vertex1 v1: T, vertex2 v2: T, weight w: Int) {
    edgeList.append(Edge(vertex1: v1, vertex2: v2, weight: w))
    vertices.insert(v1)
    vertices.insert(v2)

    adjList[v1] = adjList[v1] ?? []
    adjList[v1]?.append((vertex: v2, weight: w))

    adjList[v2] = adjList[v2] ?? []
    adjList[v2]?.append((vertex: v1, weight: w))
  }

  public mutating func addEdge(_ edge: Edge<T>) {
    addEdge(vertex1: edge.vertex1, vertex2: edge.vertex2, weight: edge.weight)
  }
}

func minimumSpanningTreeKruskal<T>(graph: Graph<T>) -> (cost: Int, tree: Graph<T>) {
  var cost: Int = 0
  var tree = Graph<T>()
  let sortedEdgeListByWeight = graph.edgeList.sorted(by: { $0.weight < $1.weight })
  
  var unionFind = UnionFind<T>()
  for vertex in graph.vertices {
    unionFind.addSetWith(vertex)
  }
  
  for edge in sortedEdgeListByWeight {
    let v1 = edge.vertex1
    let v2 = edge.vertex2
    if !unionFind.inSameSet(v1, and: v2) {
      cost += edge.weight
      tree.addEdge(edge)
      unionFind.unionSetsContaining(v1, and: v2)
    }
  }
  
  return (cost: cost, tree: tree)
}
