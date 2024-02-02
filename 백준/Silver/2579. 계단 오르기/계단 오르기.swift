import Foundation

let N = Int(readLine()!)!
var scores:[Int] = [0]
for _ in 0..<N {
    let score = Int(readLine()!)!
    scores.append(score)
}

var d = Array(repeating: Array(repeating: 0, count: N+1), count: 3)

if N >= 1 {
    d[1][1] = scores[1]
}
if N >= 2 {
    d[1][2] = scores[1]+scores[2]
    d[2][2] = scores[2]
}

if N >= 3 {
    for i in 3...N {
        d[1][i] = d[2][i - 1] + scores[i]
        d[2][i] = max(d[1][i-2] + scores[i],d[2][i-2] + scores[i])
    }
}
print(max(d[1][N],d[2][N]))