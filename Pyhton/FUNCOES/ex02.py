def piramideNumCrescente(n):
    a = 1
    b = 1
    for i in range(n+1):
        while a < b:
            print(a, end = " ")
            a +=1
        print("\n")
        b +=1
        a = 1
        

piramideNumCrescente(5)