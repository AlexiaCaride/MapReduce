import sys

max_sale = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    
    if len(data) != 2:
        continue

    payment, cost = data

    try:
        cost = float(cost)
    except ValueError:
        continue

    max_sale = max(max_sale, cost)

print( str(max_sale))

