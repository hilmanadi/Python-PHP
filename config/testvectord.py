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
        x -= (18446744073709551615 + 1)
    x ^= k
    y = geserkiri(y, 3)
    y ^= x
    result = [x, y]
    return result

def dekripsi_speck_block(x, y, k):
    y ^= x
    y = geserkanan(y, 3)
    x ^= k
    x -= y
    while x < 0:
        x += (18446744073709551615 + 1)
    x = geserkiri(x, 8)
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

def proses_dekripsi(ciphertext, key_schedule, decrypted):
    decrypted[0] = ciphertext[0]
    decrypted[1] = ciphertext[1]
    for i in reversed(range(ROUNDS)):
        tmp_res = dekripsi_speck_block(decrypted[0], decrypted[1], key_schedule[i])
        decrypted[0] = tmp_res[0]
        decrypted[1] = tmp_res[1]
    return decrypted

def dekrip(ct1,ct2,k1,k2):
    key = [0] * 2
    ciphertext = [0] * 2
    dekripted = [0]*2
    key_schedule = [0] * ROUNDS

    ciphertext[0] = ct1
    ciphertext[1] = ct2
    key[0] = k1
    key[1] = k2

    key_schedule = speck_key(key, key_schedule)
    dekripted = proses_dekripsi(ciphertext,key_schedule,dekripted)

    pt1 = hex(ciphertext[0]).rstrip("L").lstrip('0x') or "0"
    pt2 = hex(ciphertext[1]).rstrip("L").lstrip('0x') or "0"
    dekrip1 = hex(dekripted[0]).rstrip("L").lstrip('0x') or "0"
    dekrip2 = hex(dekripted[1]).rstrip("L").lstrip('0x') or "0"
    key1 = hex(key[0]).rstrip("L").lstrip('0x') or "0"
    key2 = hex(key[1]).rstrip("L").lstrip('0x') or "0"
    print "Cipher 1: " + pt1.zfill(16)
    print "Cipher 2: " + pt2.zfill(16)
    print "Hasil Dekripsi 1 : " + dekrip1
    print "Hasil Dekripsi 2 : " + dekrip2
    print "key 1 : "+key1.zfill(16)
    print "key 2 : "+key2.zfill(16)

def runprogram():
    testvector = dekrip(11987905258827821669, 8674213117595946264, 1084818905618843912, 506097522914230528)


runprogram()
