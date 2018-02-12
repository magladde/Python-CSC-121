# Password Encryption/Decryption program

# init
password_out = ''
case_changer = ord('a') - ord('A')
encryption_key = (('a', 'm'), ('b', 'h'), ('c', 't'), ('d', 'f'), ('e', 'g'),
	('f', 'k'), ('g', 'b'), ('h', 'p'), ('i', 'j'), ('j', 'w'), ('k', 'e'),
	('l', 'r'), ('m', 'q'), ('n', 's'), ('o', 'l'), ('p', 'n'), ('q', 'i'),
	('r', 'u'), ('s', 'o'), ('t', 'x'), ('u', 'z'), ('v', 'y'), ('w', 'v'),
	('x', 'd'), ('y', 'c'), ('z', 'a'))
	
# program greeting
print('This program will encrypt and decrypt user passwords\n')

# get selection (encrypt/decrypt)
which = input('Enter (e) to encrypt a password, and (d) to decrypt: ')

while which != 'e' and which != 'd':
	which = input("\nINVALID - Enter (e) to encrypt, 'd' to decrypt: ")
	
encrypting = (which == 'e') # assigns True or False

# get password
password_in = input('Enter password: ')

#perform encryption / decryption
if encrypting:
	from_index = 0
	to_index = 1
else:
	from_index = 1
	to_index = 0
	
case_changer = ord('a') - ord('A')

for ch in password_in:
	letter_found = False
	
	for t in encryption_key:
		if('a' <= ch and ch <= 'z') and ch == t[from_index]:
			password_out = password_out + t[to_index]
			letter_found = True
		elif('A' <= ch and ch <= 'Z') and ch(ord(ch) + 32) == t[from_index]:
			password_out = password_out + chr(ord(t[to_index]) - case_changer)
			letter_found = True
			
	if not letter_found:
		password_out = password_out + ch
		
# output
if encrypting:
	print('Your encrypted password is:', password_out)
else:
	print('Your decrypted password is:', password_out)
