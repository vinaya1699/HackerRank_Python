# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
English = set(map(int, input().split()))

b=int(input())
French = set(map(int, input().split()))

both = English.intersection(French)

print(len(both))
