import Foundation

let T = Int(readLine()!)!
var N:[Int] = []

for _ in 0..<T {
    let tmp = Int(readLine()!)!
    N.append(tmp)
}

let maxN = N.max()!

var d = Array(repeating: 0, count:maxN  + 1)

d[1] = 1
d[2] = 2
d[3] = 4

for i in 4...maxN {
    d[i] = d[i-1] + d[i-2] + d[i-3]
}

N.forEach {
    print(d[$0])
}