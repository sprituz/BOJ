import Foundation

func solution(_ rsp:String) -> String {
    var answer: String = ""
    for i in rsp {
        if i == "2" {
            answer += "0"
        }
        else if i == "0" {
            answer += "5"
        } else {
            answer += "2"
        }
    }
    return answer
}