def piramideNum(n):
    a = 1
    cont = 0
    while a < n: 
        while cont<a:
            print(a, end = " ")
            cont += 1
        cont = 0
        print("\n")
        a += 1

piramideNum(5)