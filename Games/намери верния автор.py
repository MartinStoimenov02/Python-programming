d={'Ботев':'Хаджи Димитър', 'Далчев':'Прозорец', 'Димов':'Тютюн', 'Пелин':'Косачи', 'Вазов':'опълченците на Шипка'}
result=0
for i in d:
    print("{0}:".format(d[i]))
    ans=input()
    if ans==i:
        result=result+1
print("result: {0} от 5".format(result))