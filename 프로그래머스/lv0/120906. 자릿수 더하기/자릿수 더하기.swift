import Foundation

func solution(_ n:Int) -> Int {
    var num:String = String(n)
    var answer:Int = 0
    
    for i in num.indices {
        answer += Int(String(num[i]))!
    }
    
    return answer
}