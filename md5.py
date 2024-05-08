#ECE543-------MD5 Algorithm Implementation
#MD5 has four passes # The algorithm referred has been explained in the report as it was little big.
import math

passes = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, #pass1
                  5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, #pass2
                  4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, #pass3
                  6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21] #pass4

const = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)]
#functions has the shift operations that are done.
functions = 16*[lambda b, c, d: (b & c) | (~b & d)] + \
            16*[lambda b, c, d: (d & b) | (~d & c)] + \
            16*[lambda b, c, d: b ^ c ^ d] + \
            16*[lambda b, c, d: c ^ (b | ~d)]
# index_functions has all the passes details based on which the rotation is performed.
index_functions = 16*[lambda i: i] + \
                  16*[lambda i: (5*i + 1)%16] + \
                  16*[lambda i: (3*i + 5)%16] + \
                  16*[lambda i: (7*i)%16]
initialize = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x<<amount) | (x>>(32-amount))) & 0xFFFFFFFF

def md5(plain):
	plain = bytearray(plain) # bytearray creates an array of string acts like a buffer
	mess_bits = (8 * len(plain)) & 0xffffffffffffffff
	plain.append(0x80)
	while len(plain)%64 != 56:
		plain.append(0)
	plain += mess_bits.to_bytes(8,byteorder = 'little')

	digest = initialize[:]

	for mess_chunks in range(0,len(plain),64):
		a,b,c,d = digest
		chunk = plain[mess_chunks:mess_chunks+64]
		for i in range(64):
			f = functions[i](b,c,d)
			g = index_functions[i](i)
			rotate = a + f + const[i] + int.from_bytes(chunk[4*g:4*g+4], byteorder='little')
			new = (b + left_rotate(rotate,passes[i])) & 0xFFFFFFFF
			a,b,c,d = d,new,b,c
		for i,val in enumerate([a,b,c,d]):
			digest[i] = digest[i] + val
			digest[i] &= 0xFFFFFFFF
	return sum(x<<(32*i) for i,x in enumerate(digest))

def final_hash(digest):
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

def main():
	default_messages = [b"Kirubha Shankar",b"KIRUBHA SHANKAR"] # give the word in the binary format 
	print ("1 To add the new message")
	print ("2. To continue")
	print ("Give the word in the binary format general form is b""")
	#print ("Type N or n for no")
	ch = input()
	if ch == 1:
		print ("Enter the message")
		new_message = input()
		default_messages.append[new_message]
		for message in default_messages:
			hash = (md5(message))
			print ("The hash of the message is =>")
			print (final_hash(hash))
			print (message.decode('ascii'))
	elif ch == 2:
		print ("Continuing with the programming")
		for message in default_messages:
			hash = (md5(message))
			print ("The hash of the message is =>")
			print (final_hash(hash))
			print (message.decode('ascii'))


main()

