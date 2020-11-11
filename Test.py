A=set(input().split())
n=int(input())
flag=False
for _ in range(n):
    B=set(input().split())
    flag=A.issuperset(B) and len(A)>len(B)
print(flag)
