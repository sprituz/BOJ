S = input()

answer = [0] * 26

for i in range(len(S)):
    answer[ord(S[i]) - ord("a")] += 1

print(*answer)