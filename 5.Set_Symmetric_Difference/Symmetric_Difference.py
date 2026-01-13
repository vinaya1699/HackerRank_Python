# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
English = set(map(int, input().split()))

b=int(input())
French = set(map(int, input().split()))

Neither_English_Nor_French = English.symmetric_difference(French)

print(len(Neither_English_Nor_French))
