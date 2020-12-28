q = input(" VVEDI SLOVA -  ")
q1 = []
num = 1
for el in range(q.count(' ') + 1):
    q1 = q.split()
    if len(str(q1)) <= 10:
        print(f" {num} {q1 [el]}")
        num += 1
    else:
        print(f" {num} {q1 [el] [0:10]}")
        num += 1