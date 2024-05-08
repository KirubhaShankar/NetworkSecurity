#ECE543--- PRIMEGEN & Primecheck Program
import random
#All the three methods Naive test, Miller-Rabin test, Fermat test corresponds to the Primecheck of the program.
#===================================Naive Test =================#
#Naive method just implemented for comparing the speed out of my own interest.
def Naive(p):
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    i = 3
    root = math.sqrt(p)
    while i <= root:
        if p % i == 0:
            return False
        i += 2
    return True

#===================================Fermat Test =================#
#Fermat's primality test:If n is a prime number & a is
#a positive integer less than n, then a^n mod n = a mod n 
def Fermat(p):
    if p == 2:
        return True
    if not p & 1:
        return False
    if pow(2,p-1,p) == 1:
        return True

#===================================Miller-Rabin Test =================#
def Miller_Rabin(p):
    k = 3       #change K for more precision
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    odd = p-1
    divide0 = 0
    while odd % 2 == 0:
        odd /= 2    #determining the 2^r.d
        divide0 += 1
    for i in range(k):# this for loop is called the witness loop
        while True:
            a = random.randint(2,p)-1
            if a !=0 and a !=1:
                break # checking if the number is not 0 and 1
        x = pow(a,odd,p) # x <- a^odd mod n
        if x != 1 or x != p-1:
            count = 1 #just continue the witness loop
        while(count <= divide0 -1) and (x != p-1):
            x = pow(x,2,p) # x<-x^2 mod n
            count += 1
        if x != p-1:
            return False
    return True #this is just a probable prime number increasing the witness loop times increases the accuracy

#===================================Primegen Function=================#
#This function allows you to choose any of the three primecheck function 
#Note: Always choose Fermat's method if you are giving big bits
def primegen(n):
    print "Choose the method you want to generate the prime number"
    print "0. Naive method"
    print "1. Fermat's method"
    print "2. Miller-Rabin method"
    print " Note: For optimal speed go for naive or fermat methode and for precision go for Miller-Rabin"
    choice = input()
    menu = [Naive,Fermat,Miller_Rabin]
    while True:
        randVar = random.getrandbits(n)
        answer = menu[choice](randVar)
        if answer == True:
            print "Found it"
            print "The primenumber that was generated is " + str(randVar)
            break
        else:
            print "Checking"

    print "The program is complete thanks for your time"
#===================================Main Function=================#
def main():
    print "Please change the number of times the operation had to be done by changing the k the k value is 3"
    print " Note :The more the number the more reliable the number beware it increases speed also"
    print " 1.Primecheck"
    print " 2.Primegen"
    ch = input()
    if ch== 1:
        print " Enter the number to check"
        num = input()
        print Fermat(num)
    else:
        print "Enter for how many number of bits you need to generate"
        bits = input()
        primegen(bits)


    
main()