q1 = '1991'
q2 = 'Владимир'

qq1 = input('В каком году произошёл развал СССР - ')
if qq1 == q1:
    print('умничка!')
else:
    print('иди учить историю')

qq2 = input('Как зовут Путина - ')
if qq2 == q2:
    print('очень хорошо')
else:
    print('соу сэд!')
print('Пока что хватит')
print('СЛЕДУЮЩЕЕ ЗАДАНИЕ')



#1 min = 60
#1 hour = 60 * 60 = 3600
#1 day = 60 * 60 * 24 = 86400

q3 = input('количество секунд -')
t = int(q3)

day= t//86400
hour= (t-(day*86400))//3600
minit= (t - ((day*86400) + (hour*3600)))//60
seconds= t - ((day*86400) + (hour*3600) + (minit*60))
print( day, 'дней' , hour,'часов', minit, 'минут',seconds,'секунд')

print('СЛЕДУЮЩЕЕ ЗАДАНИЕ')

q4 = input('введи число q- ')
q41 = int("%s" % q4)
q42 = int("%s%s" % (q4,q4))
q43 = int("%s%s%s" % (q4,q4,q4))
print(q41+q42+q43)

print('СЛЕДУЮЩЕЕ ЗАДАНИЕ')

