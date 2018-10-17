print("content-type: text/html\n\n" )
import pymysql #pip install pymysql
#import timeit
try:
    conn = pymysql.connect(host="127.0.0.1", user="root", password="", db="rekam_medik")
    cur = conn.cursor()
    pas = cur.execute("SELECT * from user,pasien")

    nama1_1 = [""]*pas
    nama1_2 = [""]*pas
    alm1 = [""]*pas
    alm2 = [""]*pas
    alm3 = [""]*pas
    alm4 = [""]*pas
    alm5 = [""]*pas
    alm6 = [""]*pas
    alm7 = [""]*pas
    alm8 = [""]*pas
    riw1 = [""]*pas
    riw2 = [""]*pas
    riw3 = [""]*pas
    riw4 = [""]*pas
    riw5 = [""]*pas
    riw6 = [""]*pas
    riw7 = [""]*pas
    riw8 = [""]*pas
    gej1 = [""]*pas
    gej2 = [""]*pas
    gej3 = [""]*pas
    gej4 = [""]*pas
    gej5 = [""]*pas
    gej6 = [""]*pas
    gej7 = [""]*pas
    gej8 = [""]*pas

    opnknci = open("C:\Users\ASUS\Desktop\workfile.txt",'r')
    kncii = opnknci.read()

    def splitbiner(w):
        splits = -((-len(w)) // 2)
        return w[:splits], w[splits:]

    def decode_binary_string(s):
        return ''.join(chr(int(s[i * 8:i * 8 + 8], 2)) for i in range(len(s) // 8))


    pasien = map(list, cur.fetchall())

    for index, a in enumerate(pasien):
        nama1,nama2 = splitbiner(pasien[index][4])
        alamat1, alamat2 = splitbiner(pasien[index][8])
        rp1,rp2 = splitbiner(pasien[index][11])
        gj1,gj2 = splitbiner(pasien[index][12])

        al1_1,al1_2 = splitbiner(alamat1)
        al2_1,al2_2 = splitbiner(alamat2)
        rp1_1,rp1_2 = splitbiner(rp1)
        rp2_1,rp2_2 = splitbiner(rp2)
        gj1_1,gj1_2 = splitbiner(gj1)
        gj2_1,gj2_2 = splitbiner(gj2)

        al1_1_1, al1_1_2 = splitbiner(al1_1)
        al1_2_1, al1_2_2 = splitbiner(al1_2)
        al2_1_1, al2_1_2 = splitbiner(al2_1)
        al2_2_1, al2_2_2 = splitbiner(al2_2)

        rp1_1_1,rp1_1_2 = splitbiner(rp1_1)
        rp1_2_1, rp1_2_2 = splitbiner(rp1_2)
        rp2_1_1, rp2_1_2 = splitbiner(rp2_1)
        rp2_2_1, rp2_2_2 = splitbiner(rp2_2)

        gj1_1_1,gj1_1_2 = splitbiner(gj1_1)
        gj1_2_1,gj1_2_2 = splitbiner(gj1_2)
        gj2_1_1,gj2_1_2 = splitbiner(gj2_1)
        gj2_2_1,gj2_2_2 = splitbiner(gj2_2)

        keys = "".join('{0:08b}'.format(x, 'b') for x in bytearray(kncii))
        kunci = keys.zfill(128)
        knci1, knci2 = splitbiner(kunci)

        nama1_1[index] = int(nama1,16)
        nama1_2[index] = int(nama2,16)
        alm1[index] = int(al1_1_1,16)
        alm2[index] = int(al1_1_2,16)
        alm3[index] = int(al1_2_1,16)
        alm4[index] = int(al1_2_2,16)
        alm5[index] = int(al2_1_1,16)
        alm6[index] = int(al2_1_2,16)
        alm7[index] = int(al2_2_1,16)
        alm8[index] = int(al2_2_2,16)
        riw1[index] = int(rp1_1_1,16)
        riw2[index] = int(rp1_1_2,16)
        riw3[index] = int(rp1_2_1,16)
        riw4[index] = int(rp1_2_2,16)
        riw5[index] = int(rp2_1_1,16)
        riw6[index] = int(rp2_1_2,16)
        riw7[index] = int(rp2_2_1,16)
        riw8[index] = int(rp2_2_2,16)
        gej1[index] = int(gj1_1_1,16)
        gej2[index] = int(gj1_1_2,16)
        gej3[index] = int(gj1_2_1,16)
        gej4[index] = int(gj1_2_2,16)
        gej5[index] = int(gj2_1_1,16)
        gej6[index] = int(gj2_1_2,16)
        gej7[index] = int(gj2_2_1,16)
        gej8[index] = int(gj2_2_2,16)

        knci1_1 = int(knci1, 2)
        knci1_2 = int(knci2, 2)

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
        for i in range(ROUNDS - 1):
            tmp_res = speck_block(a, b, i)
            a = tmp_res[0]
            b = tmp_res[1]
            key_schedule[i + 1] = b
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
        ciphertext = [0] * 2
        key = [0] * 2
        decrypted = [0] * 2
        key_schedule = [0]*ROUNDS

        ciphertext[0] = ct1
        ciphertext[1] = ct2
        key[0] = k1
        key[1] = k2
        key_schedule = speck_key(key,key_schedule)
        #start = timeit.default_timer()
        decrypted = proses_dekripsi(ciphertext, key_schedule, decrypted)
        #print timeit.default_timer() - start
        cipher1 = hex(ciphertext[0]).rstrip("L").lstrip('0x') or "0"
        cipher2 = hex(ciphertext[1]).rstrip("L").lstrip('0x') or "0"
        dekripsi1 = bin(decrypted[0])[2:].zfill(64)
        dekripsi2 = bin(decrypted[1])[2:].zfill(64)

        dekripp = decode_binary_string(dekripsi1+dekripsi2)
        #hashpasswd = sha3.sha3_512(pasien[0][1]).hexdigest()
        # print "Ciphertext 1 : " + cipher1
        # print "Ciphertext 2 : " + cipher2
        # print "Hasil Dekripsi PT1 : " + decode_binary_string(dekripsi1)
        # print "Hasil Dekripsi PT2 : " + decode_binary_string(dekripsi2)
        # print "Ciphertext : " + (cipher1 + cipher2)
        # print "Hasil Dekripsi : " + decode_binary_string(dekripsi1 + dekripsi2)
        return dekripp

    def runprogram():
        for index, a in enumerate(pasien):
            nama= dekrip(nama1_1[index],nama1_2[index],knci1_1,knci1_2)
            alamatt1 = dekrip(alm1[index],alm2[index],knci1_1,knci1_2)
            alamatt2 = dekrip(alm3[index],alm4[index],knci1_1,knci1_2)
            alamatt3 = dekrip(alm5[index],alm6[index],knci1_1,knci1_2)
            alamatt4 = dekrip(alm7[index],alm8[index],knci1_1,knci1_2)
            riwayat1 = dekrip(riw1[index],riw2[index],knci1_1,knci1_2)
            riwayat2 = dekrip(riw3[index],riw4[index], knci1_1, knci1_2)
            riwayat3 = dekrip(riw5[index],riw6[index], knci1_1, knci1_2)
            riwayat4 = dekrip(riw7[index],riw8[index], knci1_1, knci1_2)
            gejala1 = dekrip(gej1[index], gej2[index], knci1_1, knci1_2)
            gejala2 = dekrip(gej3[index], gej4[index], knci1_1, knci1_2)
            gejala3 = dekrip(gej5[index], gej6[index], knci1_1, knci1_2)
            gejala4 = dekrip(gej7[index], gej8[index], knci1_1, knci1_2)

            alamatsemua = (alamatt1+alamatt2+alamatt3+alamatt4).rstrip('\x00').lstrip('\x00')
            gejalasemua = (gejala1+gejala2+gejala3+gejala4).rstrip('\x00').lstrip('\x00')
            riwayatsemua = (riwayat1+riwayat2+riwayat3+riwayat4).rstrip('\x00').lstrip('\x00')

            tambah_pasien = ("UPDATE pasien "
                             "SET nama = %s, alamat =%s,ket_rekam_medik=%s,gejala=%s"
                             "WHERE no_pasien  = %s"
                             )
            add_pasien = (nama, alamatsemua, riwayatsemua, gejalasemua, pasien[index][3])
            cur.execute(tambah_pasien, add_pasien)
            conn.commit()

    runprogram()
    # print "testvector"
    # runprogram(8388271400802151712,7809653424151160096 , 506097522914230528, 1084818905618843912,'')

except pymysql.Error as error :
    print("koneksi ke database error"), error









