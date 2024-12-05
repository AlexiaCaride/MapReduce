import sys

max_sale = 0
old_payment = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    payment, cost = data

    if old_payment and old_payment != payment:
        print(old_payment + "\t" + str(max_sale))
        old_payment = payment
        max_sale = 0

    old_payment = payment
    max_sale = max(max_sale, float(cost)) 

if old_payment:
    print(old_payment + "\t" + str(max_sale))
