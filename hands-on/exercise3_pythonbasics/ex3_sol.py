# numero primo: divisibile solo per sé stesso e per 1
def prime():
    '''
    Questa funzione crea una lista di numeri compresi tra 2 e 100 che siano primi.

    '''
    primi = []
    num_to_test = list(range(2,101))
    for i in num_to_test:
        fattori_i=[]
        j = 2
        while j < i:
            if i%j == 0:
                fattori_i.append(j)
                print(j, "is a factor of", i, "!")
                #print(fattori_i)
            else:
                #print(j, "is NOT a factor f", i, "!")
                pass
            j+=1
        if len(fattori_i) == 0:
            primi.append(i)
            print(i, "IS a prime!")
            for multiple in range(i*2, 101, i):
                if multiple in num_to_test:
                    num_to_test.remove(multiple)
                else: 
                    pass
        else:
            print(i, "NOT a prime!")
    return primi
                
primi=prime()
print("numeri primi:", primi)

# while i%j is not False:

