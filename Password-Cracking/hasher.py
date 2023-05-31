import hashlib

if __name__ == '__main__':
	word = input('Type the word to hash: ').encode()
	
	# MD5
	md5 = hashlib.md5()
	md5.update(word)
	print('MD5:', md5.hexdigest())

	# SHA1
	sha1 = hashlib.sha1()
	sha1.update(word)
	print('SHA1:', sha1.hexdigest())

	# SHA256
	sha256 = hashlib.sha256()
	sha256.update(word)
	print('SHA256:', sha256.hexdigest())

	# SHA512
	sha512 = hashlib.sha512()
	sha512.update(word)
	print('SHA512:', sha512.hexdigest())
