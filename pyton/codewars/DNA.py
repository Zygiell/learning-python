'''
A" and "T" //"C" and "G"

'''
result = []
dna = 'ATCG'  # TAGC

for litera in dna:
    if litera == 'A':
        result.append('T')
    elif litera == 'T':
        result.append('A')
    elif litera == 'C':
        result.append('G')
    elif litera == 'G':
        result.append('C')
    else:
        result.append(litera)
print(''.join(result))
