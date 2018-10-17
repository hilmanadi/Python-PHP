import sha3

a = "abc"
b = "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
c = ""
d = raw_input("input : ")
print "test vector hasil input  : "
print sha3.sha3_224(d).hexdigest()
print "test vector 'abc' : "
print sha3.sha3_224(a).hexdigest()
print "test vector 'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq' : "
print sha3.sha3_224(b).hexdigest()
print "test vector '' : "
print sha3.sha3_224(c).hexdigest()