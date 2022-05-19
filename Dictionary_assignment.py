Dic = {}

while True:
    key = input('키 입력 > ')
    value = str(input('키 값 입력 > '))

    if key=='0' or value=='종료':
        print('종료')
        break
    else:
        k = int(key)
        Dic[k] = value
print(Dic)
print(list(Dic.keys()))
print(list(Dic.values()))
print(list(Dic.items())) 


