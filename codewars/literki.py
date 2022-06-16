a = ''
literki = []
result = [a[i] for i in range(len(a)-1) if a[i] != a[i+1]] + [a[-1]]
print(result)
