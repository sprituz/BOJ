import Foundation

let N = Int(readLine()!)!

var card: [Int] = Array(1...N)

var index = 0

while true {
    index += 1
    if index < card.count {
        card.append(card[index])
    } else  {
        break
    }
    index += 1
}

print(card.last!)