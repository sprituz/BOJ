import Foundation

let nums = readLine()!.split(separator: " ").map { Int($0)! }

let N = nums[0]

let M = nums[1]

let V = nums[2]

var graph = Array(repeating: (Array(repeating: 0, count: N+1)), count: N + 1)

for _ in 0..<M {
    let node = readLine()!.split(separator: " ").map { Int($0)! }
    graph[node[0]][node[1]] = 1
    graph[node[1]][node[0]] = 1
}

func bfs(graph: [[Int]], start: Int, N: Int) {
    var visited : [Int] = []
    var queue: [Int] = []
    visited.append(start)
    queue.append(start)
    while !(queue.isEmpty) {
        var node = queue.removeFirst()
        for i in 1...N {
            if graph[node][i] == 1 && !visited.contains(i) {
                queue.append(i)
                visited.append(i)
            }
        }
    }
    print(visited.map { String($0) }.joined(separator: " "))
}

func dfs(graph: [[Int]], start: Int,  N: Int, visited:inout [Int]) {
    visited[start] = 1
    print(start, terminator: " ")
    for i in 1...N {
        if graph[start][i] == 1 && visited[i] == 0 {
            dfs(graph: graph, start: i, N: N, visited: &visited)
        }
    }
}

var visited : [Int] = Array(repeating: 0, count: N+1)

dfs(graph: graph, start: V, N: N, visited: &visited)
print()
bfs(graph: graph, start: V, N: N)

