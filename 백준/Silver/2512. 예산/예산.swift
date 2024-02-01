import Foundation

let N = Int(readLine()!)!
let yesan = readLine()!.split(separator: " ").map { Int($0)! }
let M = Int(readLine()!)!
var maxYesan = yesan.max()

for i in stride(from: maxYesan!, to: 0, by: -1) {
    var answer = 0
    yesan.forEach {
        answer += ($0 - i >= 0 ? i : $0)
    }
    if answer <= M {
        print(i)
        break
    }
}