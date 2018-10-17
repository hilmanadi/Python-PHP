def splitbiner(w):
    splits = -((-len(w)) // 2)
    return w[:splits:], w[splits:]

def decode_binary_string(s):
    return ''.join(chr(int(s[i * 8:i * 8 + 8], 2)) for i in range(len(s) // 8))

def split_bits(val,n):
    parts,mask = [],(1<<n)-1
    parts = [0]*4
    while val:
        parts.insert(4,val&mask)
        parts.pop(0)
        val >>=n
    parts.reverse()
    return parts

ROUNDS = 32

def geserkiri(value, shift):
    tmp_bin = bin(value)[2:].zfill(64)
    binary = []
    for i in tmp_bin:
        binary.append(i)
    for i in range(shift):
        binary.append(binary.pop(0))
    result = ''.join(binary)
    return int(result, 2)

def geserkanan(value, shift):
    tmp_bin = bin(value)[2:].zfill(64)
    binary = []
    for i in tmp_bin:
        binary.append(i)
    for i in range(shift):
        binary.insert(0, binary.pop())
    result = ''.join(binary)
    return int(result, 2)

def speck_block(x, y, k):
    x = geserkanan(x, 8)
    x += y
    while x > 18446744073709551615:
        x -= (18446744073709551615+1)
    x ^= k
    y = geserkiri(y, 3)
    y ^= x
    result = [x, y]
    return result

def speck_key(key, key_schedule):
    a = key[0]
    b = key[1]
    key_schedule[0] = b
    for i in range(ROUNDS-1):
        tmp_res = speck_block(a, b, i)
        a = tmp_res[0]
        b = tmp_res[1]
        key_schedule[i+1] = b
    return key_schedule

def proses_enkripsi(plaintext, key_schedule, ciphertext):
    ciphertext[0] = plaintext[0]
    ciphertext[1] = plaintext[1]
    for i in range(ROUNDS):
        tmp_res = speck_block(ciphertext[0], ciphertext[1], key_schedule[i])
        ciphertext[1] = tmp_res[1]
        ciphertext[0] = tmp_res[0]
    return ciphertext


def enkrip(pl1,pl2,k1,k2):
    plaintext = [0] * 2
    key = [0] * 2
    ciphertext = [0] * 2
    dekripted = [0]*2
    key_schedule = [0] * ROUNDS

    plaintext[0] = pl1
    plaintext[1] = pl2
    key[0] = k1
    key[1] = k2

    key_schedule = speck_key(key, key_schedule)
    ciphertext = proses_enkripsi(plaintext, key_schedule, ciphertext)
    pt1 = hex(plaintext[0]).rstrip("L").lstrip('0x') or "0"
    pt2 = hex(plaintext[1]).rstrip("L").lstrip('0x') or "0"
    enkripsi1 = hex(ciphertext[0]).rstrip("L").lstrip('0x') or "0"
    enkripsi2 = hex(ciphertext[1]).rstrip("L").lstrip('0x') or "0"
    key1 = hex(key[0]).rstrip("L").lstrip('0x') or "0"
    key2 = hex(key[1]).rstrip("L").lstrip('0x') or "0"
    e1 = enkripsi1.zfill(16)
    e2 = enkripsi2.zfill(16)
    enkripp = e1 +" "+ e2
    print "PT1: " + pt1.zfill(16)
    print "PT2: " + pt2.zfill(16)
    print "key 1 : "+key1.zfill(16)
    print "key 2 : "+key2.zfill(16)
    print "Hasil Enkripsi PT1 : " + e1
    print "Hasil Enkripsi PT2 : " + e2
    print "Plaintext : " + pt1.zfill(16)+" "+pt2.zfill(16)
    print "Hasil Enkripsi : " + enkripp
    return enkripp

def runprogram():
    testvector = enkrip(7809653424151160096, 8388271400802151712, 1084818905618843912, 506097522914230528)

runprogram()
