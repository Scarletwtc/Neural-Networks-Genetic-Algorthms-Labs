n=input('Gimme an input')

#if statement to compare the inout to 0
try:
    if int(n) > 0:
        #if cond is true
        print(n, ' is greater than 0')
    elif int(n) < 0: 
        print(n, ' is lower than 0')
    else:
        print(n, ' is equal to 0')   
except ValueError:
    print("The input needs to be a number.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    
    