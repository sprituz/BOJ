let T = Int(readLine()!)!

for _ in 0..<T {
    var input = readLine()!.split(separator: " ").map { String($0)}
    var str:[String] = input[1].map { String($0) }
    str.remove(at: Int(input[0])! - 1)
    print(str.joined())
}