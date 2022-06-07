num = 1
while num <= 10 :
    for i in range(1,11):
        print(i,"*",num,"=",num*i, end="    ")
    num+=1
    print("\n")