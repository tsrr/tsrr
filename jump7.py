i = 0
while i <100:#当i小于100
    i = i + 1
    if i % 7 == 0:#除7等于0
        continue
    elif i % 10 == 7:#个位是7
        continue
    elif i // 10 == 7:#十位是7
        continue
    else:
        print (i)#输出i



