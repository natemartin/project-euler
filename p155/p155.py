from sets import Set
from fractions import Fraction

configs = {}
configs[1] = Set([Fraction(1, 1)])

max_c = 18

for c in range(2, max_c + 1):
    configs[c] = Set()
    for i in range(1, int(c / 2) + 1):
        for config1 in configs[i]:
            for config2 in configs[c - i]:
                configs[c].add(config1 + config2);
                configs[c].add(Fraction(1, (Fraction(1, config1) + Fraction(1, config2))))

results = Set()
total = 0
for i in range(1, max_c + 1):
    total += len(configs[i])
print total
