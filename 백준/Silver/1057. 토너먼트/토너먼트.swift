import Foundation

var input = readLine()!.split(separator: " ").map{Int($0)!}
let N = input[0]
var jimin = input[1]
var hansu = input[2]

for i in 1...((Int(N)/2)+1){
    if Int(jimin + 1) / 2 == Int(hansu + 1) / 2 {
        if jimin < hansu {
            if Int(jimin + 1)/2 == Int(hansu)/2 {
                print(i)
                break
            }
        } else {
            if Int(jimin)/2 == Int(hansu + 1)/2 {
                print(i)
                break
            }
        }
    }
        jimin = (jimin + 1) / 2
        hansu = (hansu + 1) / 2
}