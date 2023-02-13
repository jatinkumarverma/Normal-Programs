def pypart(n):

     

    

    for i in range(0, n):

     

 

        for j in range(0, i+1):

         

            

            print("* ",end="")

      

        

        print("\r")
 

n = 5
pypart(n)





def pypart(n):

    myList = []

    for i in range(1,n+1):

        myList.append("*"*i)

    print("\n".join(myList))
 
# Driver Code

n = 5
pypart(n)


def pypart(n):

    if n==0:

        return

    else:

        pypart(n-1)

        print("* "*n)

  
# Driver Code

n = 5
pypart(n)



def pypart2(n):

     

    # number of spaces

    k = 2*n - 2
 

    # outer loop to handle number of rows

    for i in range(0, n):

     

        # inner loop to handle number spaces

        # values changing acc. to requirement

        for j in range(0, k):

            print(end=" ")

     

        # decrementing k after each loop

        k = k - 2

     

        # inner loop to handle number of columns

        # values changing acc. to outer loop

        for j in range(0, i+1):

         

            # printing stars

            print("* ", end="")

     

        # ending line after each row

        print("\r")
 
# Driver Code

n = 5
pypart2(n)
