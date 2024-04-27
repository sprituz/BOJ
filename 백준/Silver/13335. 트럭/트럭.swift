import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
let trucks = readLine()!.split(separator: " ").map{Int($0)!}
let n = input[0] // 트럭 수
let w = input[1] // 다리 길이
let L = input[2] // 다리 최대 하중
var answer:Int = 0
var trucksTime = Array(repeating: 0, count: n)
var bridgeWeight = 0
var bridgeTruckNum = 0
while trucksTime.filter({ $0 == w + 1}).count < trucks.count {
    answer += 1
    for i in 0..<trucks.count {
        if trucksTime[i] == w + 1 { // 이미 지나간거
            continue
        } else if trucksTime[i] == w { // 끝에온거
            bridgeWeight -= trucks[i]
            bridgeTruckNum -= 1
            trucksTime[i] += 1
        } else {
            if trucksTime[i] != 0 { //이미 올라가 있는 것들
                trucksTime[i] += 1
            } else {
                if bridgeTruckNum + 1 <= w &&  bridgeWeight + trucks[i] <= L { //신규
                    trucksTime[i] += 1
                    bridgeTruckNum += 1
                    bridgeWeight += trucks[i]
                    break
                } else {
                    break
                }
            }
        }
    }
    
}

print(answer)