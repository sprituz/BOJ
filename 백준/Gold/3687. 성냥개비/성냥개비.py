T = int(input())

d = [6,2,5,5,4,5,6,3,7,6]


def cal(n):
    array = [""] * (n + 1)
    max_num = ""
    for i in range(2, n + 1):
        if i <= 7:
            for j in range(1, 10):
                if i == d[j]:
                    array[i] += str(j)
                    break
        else:
            if i <= 14:
                min_num = 1e9
                for j in range(1, 9):
                    if 2 <= i - d[j] <= 7:
                        min_num = min(min_num, int(str(j) + str(d.index(i - d[j]))))
                array[i] = str(min_num)
            else:
                min_num = int(str(1) + array[i - d[1]].replace("6","0"))
                if i == 17:
                    array[i] = "200"
                    continue
                for j in range(1, 9):
                    min_num = min(min_num, int(array[i - d[j]] + str(j)))
                array[i] = str(min_num)
    remain = n
    while remain != 0:
        if remain % 2 != 0 and max_num == "":
            remain -= d[7]
            max_num += "7"
        else:
            remain -= d[1]
            max_num += "1"
    print(array[n], int(max_num))


for _ in range(T):
    n = int(input())
    cal(n)