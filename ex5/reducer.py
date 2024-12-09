import sys

total_sales = 0

for line in sys.stdin:
    if not line.strip():
        continue
    try:
        key, value = line.strip().split("\t")
    except ValueError:
               continue
    try:
        value = float(value)
    except ValueError:
        continue
    total_sales += value

print("Total de ventas: " + str(total_sales))

