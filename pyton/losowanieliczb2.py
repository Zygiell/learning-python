'''
random - z ang. losowy

random()       0 <= x < 1 lub [0,1)

uniform (2.5, 10.0) 2.5 <= x < 10.0 lub [2.5, 10)
randomrange(10)        z puli (0,1,2,3,4,5,6,7,8,9)
randomrange(0, 15, 2) parzyste z puli (0,2,4....14) 3 cyfra w randomrange = co ile

randint (0, 4) [0,4]
'''

import random
from collections import Counter
x = 0
# while x < 100:
# x += 1
#print(random.uniform(0, 100))


def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0, 100)
    if isHitChance <= weaponChanceToHitPercentage:
        return 'trafiony'
    else:
        return 'chybiony'


listHit = []
while x < 1:
    x += 1
    listHit.append(will_weapon_hit(50))
print(listHit.count('trafiony'))
print(listHit.count('chybiony'))

dictionaryHit = Counter(listHit)

case = ['covert', 'restricted', 'classified', 'rare']
print(Counter(random.choices(case, [83, 15.6, 2.83, 0.3], k=1000)))
