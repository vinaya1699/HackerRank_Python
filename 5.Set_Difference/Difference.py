# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
English = set(map(int, input().split()))

b=int(input())
French = set(map(int, input().split()))

Only_English = English.difference(French)

print(len(Only_English))
