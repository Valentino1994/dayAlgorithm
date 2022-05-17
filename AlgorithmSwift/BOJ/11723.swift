import Foundation

var buffer: [UInt8] = Array(FileHandle.standardInput.readDataToEndOfFile()), byteIdx = 0; buffer.append(0)

@inline(__always) func readByte() -> UInt8 {
    defer { byteIdx += 1 }
    return buffer.withUnsafeBufferPointer { $0[byteIdx] }
}

@inline(__always) func readInt() -> Int {
    var number = 0, byte = readByte(), isNegative = false
    while byte == 10 || byte == 32 { byte = readByte() }
    if byte == 45 { byte = readByte(); isNegative = true }
    while 48...57 ~= byte { number = number * 10 + Int(byte - 48); byte = readByte() }
    return number * (isNegative ? -1 : 1)
}

@inline(__always) func readStirngSum() -> Int {
    var byte = readByte()
    while byte == 10 || byte == 32 { byte = readByte() }
    var sum = Int(byte)
    while byte != 10 && byte != 32 && byte != 0 { byte = readByte(); sum += Int(byte) }
    return sum - Int(byte)
}

@inline(__always) func writeByBytes(_ output: [UInt8]) {
    FileHandle.standardOutput.write(Data(bytes: output, count: output.count * MemoryLayout<UInt8>.stride))
}

var boolArray = Array(repeating: false, count: 21)
let fullArray = Array(repeating: true, count: 21)
let emptyArray = Array(repeating: false, count: 21)
var output = [UInt8]()

(1...readInt()).forEach{ _ in
    switch readStirngSum() {
    case 297:
        boolArray[readInt()] = true
        break
    case 654:
        boolArray[readInt()] = false
        break
    case 510:
        output.append(boolArray[readInt()] ? 49 : 48)
        output.append(32)
        break
    case 642:
        boolArray[readInt()].toggle()
        break
    case 313:
        boolArray = fullArray
        break
    default:
        boolArray = emptyArray
        break
    }
}

writeByBytes(output)

// 시간초과 코드

import Foundation

var N: Int = Int(readLine()!)!
var mySet: [Bool] = Array(repeating: false, count: 21)

for _ in 0..<N {
    let commands: [String] = readLine()!.split(separator: " ").map { String($0) }
    let command: String = commands[0]
    
    if commands.count > 1 {
        let nums: Int = Int(commands[1])!
        if command == "add" {
            if !mySet[nums] {
                mySet[nums] = true
            }
            continue
        }
        else if command == "remove" {
            if mySet[nums] {
                mySet[nums] = false
            }
            continue
        }
        else if command == "check" {
            if mySet[nums] {
                print(1)
            } else {
                print(0)
            }
            continue
        }
        else if command == "toggle" {
            if !mySet[nums] {
                mySet[nums] = true
            } else {
                mySet[nums] = false
            }
            continue
        }
    } else {
        if command == "all" {
            mySet = Array(repeating: true, count: 21)
            continue
        }
        else if command == "empty" {
            mySet = Array(repeating: false, count: 21)
            continue
        }
    }
}
