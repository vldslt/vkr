q1 = {1 : 'ZIMA', 2 : 'VESNA', 3 : 'LETO', 4 : 'OSEN'}
mes = int(input(" VVEDI NOMER - "))
if mes == 1 or mes == 2 or mes == 12:
        print(q1.get(1))
elif mes == 3 or mes == 4 or mes ==5:
    print(q1.get(2))
elif mes == 6 or mes == 7 or mes == 8:
    print(q1.get(3))
elif mes == 9 or mes == 10 or mes == 11:
    print(q1.get(4))

q2 = ['ZIMA', 'VESNA', 'LETO', 'OSEN']
mes = int(input(" VVEDI NOMER - "))
if mes ==1 or mes == 12 or mes == 2:
        print(q2[0])
elif mes == 3 or mes == 4 or mes == 5:
    print(q2[1])
elif mes == 6 or mes == 7 or mes == 8:
    print(q2[2])
elif mes == 9 or mes == 10 or mes == 11:
    print(q2[3])