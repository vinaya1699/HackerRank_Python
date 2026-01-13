if name == 'main':
n = int(input())
arr = map(int, input().split())

unique_scores = list(set(arr))
unique_scores.sort(reverse=True)

Runner_Up = unique_scores[1]
print(Runner_Up)
