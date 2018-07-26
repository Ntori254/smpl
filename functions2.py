def message():
    Texts="the,quick,brown,fox,jumps,over,the,lazy,dog"
    spliter= Texts.split(',')
    joiner= '***'.join(spliter)
    print(spliter)
    print(joiner)
    for Mess in Texts:
        print(Mess.title())
print(message())
#split and combine