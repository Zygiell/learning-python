dancing_brigade = 'abBA'
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
duze = [e for e in dancing_brigade if e in big]
male = [e for e in dancing_brigade if e in small]
result = []
for e in duze:
    result.append(e)
for e in male:
    result.append(e)
print(sorted(result, key=str.casefold))
