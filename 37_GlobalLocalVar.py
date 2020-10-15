def f1():
    a=10                            #local variable for f1()
    print(a)
def f2():
    a=777                           #local variable for f2()
    print(a)
f1()                                #prints 10
f2()                                #prints 777


b=10                                #global variable for program
def f3():
    print("\n\n",b,sep='')
def f4():
    print(b,"\n\n")
f3()                                #prints 10
f4()                                #prints 10
def f5():
    b=2
    print(b)
f5()                                #prints 2, the local variable, even if global b is present
