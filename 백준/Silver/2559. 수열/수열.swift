import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }

let N = input[0]
let K = input[1]


let temp = readLine()!.split(separator: " ").map { Int($0)! }

var total = temp[0..<K].reduce(0, +)

var answer = total

if N - K >= 1 {
    for i in 1...N-K {
        total -= temp[i-1]
        total += temp[i+K-1]
        answer = max(answer,total)
    }
}
print(answer)