With open (‘c:/ Users/ User/ Desktop/input. txt’, “r”) as f:
    C=f. readline ()
numar_vocale=0
With open(‘c:/ Users/ User/ Desktop/output. txt’, “w”) as f:
     for i in C:
       if i in ‘abcdABCD’:
              f. write(“ Vocalele sunt: “+i)
               numar_vocale+=1
print (‘ Numărul vocalelor este:’ ,numar_vocale)
