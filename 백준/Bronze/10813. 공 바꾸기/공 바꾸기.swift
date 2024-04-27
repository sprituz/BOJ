import Foundation

let arr = readLine()!.split(separator: " ").map { Int($0)! }
var balls:[Int] = Array(1...arr[0])

for _ in 0..<arr[1] {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    balls.swapAt(input[0] - 1, input[1] - 1)
}

print(balls.map{ String($0) }.joined(separator: " "))