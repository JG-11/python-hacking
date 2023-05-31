import crypt

word = input('Type word to encrypt: ')
option = int(input('[0] SHA512\n[1] SHA256\n[2] MD5\n Type the hashing method: '))

if option < 0 or option > 2:
	print('Invalid hashing method')
	print('Finishing program')
	exit()

if option == 0:
	print('SHA512: ', crypt.crypt(word, crypt.METHOD_SHA512))
elif option == 1:
	print('SHA256: ', crypt.crypt(word, crypt.METHOD_SHA256))
else:
	print('MD5: ', crypt.crypt(word, crypt.METHOD_MD5))

