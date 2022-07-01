def solution(routes):
    answer = 0
    routes.sort()
    stack = [routes[0]]
    del routes[0]
    flag=0
    while routes:
        for i in range(len(routes)):
            if flag==1:
                flag=0
                break
            for j in range(len(stack)):
                if stack[j][0] <= routes[i][0] <= routes[i][1] and routes[i][1] <= stack[j][1]:
                    stack.append([routes[i][0], routes[i][1]])
                    del stack[j]
                    del routes[i]
                    flag = 1
                    break
                elif routes[i][0] < stack[j][0] and stack[j][0] <= routes[i][1] <= stack[j][1]:
                    stack.append([stack[j][0], routes[i][1]])
                    del stack[j]
                    del routes[i]
                    flag = 1
                    break
                elif stack[j][0] <= routes[i][0] <= stack[j][1] and stack[j][1] < routes[i][1]:
                    stack.append([routes[i][0], stack[j][1]])
                    del stack[j]
                    del routes[i]
                    flag=1
                    break
                elif j==len(stack)-1:
                    stack.append([routes[i][0], routes[i][1]])
                    del routes[i]
                    flag=1
                    break
    return len(stack)