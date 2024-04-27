let input = readLine()!.split(separator: " ").map {String($0)}
var answer:Int = 0
var sumOfNum1 = input[0].map{Int(String($0))!}.reduce(0,+)

for j in input[1] {
    answer += sumOfNum1 * Int(String(j))!
}

print(answer)