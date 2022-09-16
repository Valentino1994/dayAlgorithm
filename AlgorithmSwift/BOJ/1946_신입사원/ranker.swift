//
//  ranker.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/09/16.
//

import Foundation

let file = FileIO()

for _ in 0..<file.readInt() {
    
    let N = file.readInt()
    var arr = Array(repeating: 0, count: N)

    for _ in 0..<N {
        let input = [file.readInt(), file.readInt()]
        arr[input[0]-1] = input[1]
    }
    
    var min = Int.max
    var count = 0
    arr.forEach{
        if $0 < min {
            count += 1
            min = $0
        }
    }
    print(count)
}

final class FileIO {
    private var buffer:[UInt8]
    private var index: Int
    
    init(fileHandle: FileHandle = FileHandle.standardInput) {
        buffer = Array(fileHandle.readDataToEndOfFile())+[UInt8(0)] // 인덱스 범위 넘어가는 것 방지
        index = 0
    }
    
    @inline(__always) private func read() -> UInt8 {
        defer { index += 1 }
        
        return buffer.withUnsafeBufferPointer { $0[index] }
    }
    
    @inline(__always) func readInt() -> Int {
        var sum = 0
        var now = read()
        var isPositive = true
        
        while now == 10
                || now == 32 { now = read() } // 공백과 줄바꿈 무시
        if now == 45{ isPositive.toggle(); now = read() } // 음수 처리
        while now >= 48, now <= 57 {
            sum = sum * 10 + Int(now-48)
            now = read()
        }
        
        return sum * (isPositive ? 1:-1)
    }
    
    @inline(__always) func readString() -> String {
        var str = ""
        var now = read()
        
        while now == 10
                || now == 32 { now = read() } // 공백과 줄바꿈 무시
        
        while now != 10
                && now != 32 && now != 0 {
            str += String(bytes: [now], encoding: .ascii)!
            now = read()
        }
        return str
    }
}
