def gauss(n):
    if n==0 or n==1:
        return 1
    else: return n*(n+1)/2
n=int(input("Elige un numero"))
print(gauss(n))