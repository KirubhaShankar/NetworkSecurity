#ECE543--- RSA Implementation using Python
#The entire pseudocode of which the RSA algorithm was implented is given below:
#First enter two prime numbers p and q also check if they are prime by fermat method
#Calculate the n and also the totient function based on pi_n = (p-1)(q-1)
#Choose an e which is a prime number with in the range of 2 to pi_n
#Calculate d which is a co-prime of the e
#Encrypt the message using to obtain cipher c = m^e mod n
#Decrypt the message m = c ^ d mod n
import random
import math
e=0
de=0
cipher,message = 0,0
#main function 
def main():
	print "Enter two prime numbers"
	p = input()	#enter the number p
	q = input()	#enter the number q
	n = p*q
	print " n is :" + str(n)
	#check if it is a primenumber or not
	en,den = keygen(p,q)	#getting the public key and private key
	print "Encrypt function"
	secret = encrypt(n,en)		#calling the encrypt function
	print "Decrypt function"
	decrypt(secret,den,n)		#calling the decrypt function
#===================================FERMATS THEOREM(Primality test)=================#
def fermat(n):
	if n == 2:
		return True
	if not n & 1:
		return False
	if pow(2, n-1, n) == 1:
		return True
#===================================Euclid theorem test=================#
def gcd(rande,randd,pi_n):
	if (randd * rande)%pi_n == 1:
		return True
#===================================Keygen generation=================#
def keygen(p,q):
		
	n = p * q
	pi_n = (p-1) * (q-1) #totient function calculation.
	while True:
		rande = random.randrange(1,pi_n)
		d = fermat(rande)
		if d == True and rande != 2:
			print "encryption(public) key :"+str(rande)+"n:"+str(n)
			break
	e = rande
			
	while True:
		randd = random.randrange(1,pi_n)
		d = fermat(randd)
		if d == True and rande != 2 and gcd(rande,randd,pi_n) == True:
			print "decryption(private) key :"+str(randd)+"n:"+str(n)
			break
	de = randd
	return e,de
#===================================Encryption Function=================#
def encrypt(n,en):
	print "Enter the message you want encrypt"
	message = input()#  m <256 should be the value of the message
	
	cipher = (message ** en)%n
	print "Cipher text is :"+ str(cipher)
	return cipher
#===================================Decryption Function=================#
def decrypt(secret,den,n):    
	plain_text = (secret ** den) % n
	print "Plain text is :"+ str(plain_text)

main()
