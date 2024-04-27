import Foundation

while let input = readLine() {
    let str = input
    var answer = [0,0,0,0]
    for i in str {
        if i.isLowercase {
            answer[0] += 1
        } else if i.isUppercase {
            answer[1] += 1
        } else if i.isNumber {
            answer[2] += 1
        } else {
            answer[3] += 1
        }
    }
    print(answer.map {String($0)}.joined(separator: " "))
}