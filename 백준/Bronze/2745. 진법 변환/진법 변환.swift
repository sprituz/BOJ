import Foundation

var arr = readLine()!.split(separator: " ").map {String($0)}

var answer:Int = Int(arr[0], radix: Int(arr[1])!)!

print(answer)