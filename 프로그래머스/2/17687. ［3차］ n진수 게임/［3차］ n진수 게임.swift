func solution(_ n:Int, _ t:Int, _ m:Int, _ p:Int) -> String {
    let num = (0...t*m).flatMap{ Array(String($0, radix:n).uppercased()) }
    var result: String = ""
    
    for i in 0..<num.count {
        if result.count == t {
            break
        }
        else if (i % m - (p - 1)) == 0 {
            result += String(num[i])
        }
    }

    return result
}