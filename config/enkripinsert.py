print("content-type: text/html\n\n" )
import pymysql #pip install pymysql
import sys

try:
    conn = pymysql.connect(host="127.0.0.1", user="root", password="", db="rekam_medik")
    cur = conn.cursor()
    pasien = cur.execute("SELECT * from user")

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

    id = sys.argv[1].rstrip("'").lstrip("'")
    nama = sys.argv[2].rstrip("'").lstrip("'")
    tanggal = sys.argv[3].rstrip("'").lstrip("'")
    umur = sys.argv[4].rstrip("'").lstrip("'")
    jeniskelamin = sys.argv[5].rstrip("'").lstrip("'")
    alamat = sys.argv[6].rstrip("'").lstrip("'")
    pekerjaan = sys.argv[7].rstrip("'").lstrip("'")
    dokter = sys.argv[8].rstrip("'").lstrip("'")
    riwayatpenyakit = sys.argv[9].rstrip("'").lstrip("'")
    gejla = sys.argv[10].rstrip("'").lstrip("'")

    namaa ="".join('{0:08b}'.format(x, 'b') for x in bytearray(nama))
    alamatt = "".join('{0:08b}'.format(x, 'b') for x in bytearray(alamat))
    riwayatt = "".join('{0:08b}'.format(x, 'b') for x in bytearray(riwayatpenyakit))
    gejalaa = "".join('{0:08b}'.format(x, 'b') for x in bytearray(gejla))

    namaaa  = namaa.zfill(128)
    alamattt = alamatt.zfill(512)
    riwayattt = riwayatt.zfill(512)
    gejalaaa = gejalaa.zfill(512)

    gjj = int(gejalaaa,2)
    rpp = int(riwayattt,2)
    almtt = int(alamattt,2)

    a = split_bits(almtt,128)
    g = split_bits(gjj,128)
    r = split_bits(rpp,128)
    al1 = bin(a[0])[2:].zfill(128)
    al2 = bin(a[1])[2:].zfill(128)
    al3 = bin(a[2])[2:].zfill(128)
    al4 = bin(a[3])[2:].zfill(128)

    ket1 = bin(r[0])[2:].zfill(128)
    ket2 = bin(r[1])[2:].zfill(128)
    ket3 = bin(r[2])[2:].zfill(128)
    ket4 = bin(r[3])[2:].zfill(128)

    gejala1 = bin(g[0])[2:].zfill(128)
    gejala2 = bin(g[1])[2:].zfill(128)
    gejala3 = bin(g[2])[2:].zfill(128)
    gejala4 = bin(g[3])[2:].zfill(128)

    #pecah biner
    nama1, nama2 = splitbiner(namaaa)
    alm1,alm2 = splitbiner(al1)
    alm3,alm4 = splitbiner(al2)
    alm5,alm6 = splitbiner(al3)
    alm7,alm8 = splitbiner(al4)
    rp1, rp2 = splitbiner(ket1)
    rp3, rp4 = splitbiner(ket2)
    rp5, rp6 = splitbiner(ket3)
    rp7, rp8 = splitbiner(ket4)
    gj1, gj2 = splitbiner(gejala1)
    gj3, gj4 = splitbiner(gejala2)
    gj5, gj6 = splitbiner(gejala3)
    gj7, gj8 = splitbiner(gejala4)
    #input int
    nama1_1 = int(nama1, 2)
    nama1_2 = int(nama2, 2)
    alamat1_1 = int(alm1, 2)
    alamat1_2 = int(alm2, 2)
    alamat2_1 = int(alm3, 2)
    alamat2_2 = int(alm4, 2)
    alamat3_1 = int(alm5, 2)
    alamat3_2 = int(alm6, 2)
    alamat4_1 = int(alm7, 2)
    alamat4_2 = int(alm8, 2)
    rp1_1 = int(rp1, 2)
    rp1_2 = int(rp2, 2)
    rp2_1 = int(rp3, 2)
    rp2_2 = int(rp4, 2)
    rp3_1 = int(rp5, 2)
    rp3_2 = int(rp6, 2)
    rp4_1 = int(rp7, 2)
    rp4_2 = int(rp8, 2)
    gj1_1 = int(gj1, 2)
    gj1_2 = int(gj2, 2)
    gj2_1 = int(gj3,2)
    gj2_2 = int(gj4,2)
    gj3_1 = int(gj5,2)
    gj3_2 = int(gj6,2)
    gj4_1 = int(gj7,2)
    gj4_2 = int(gj8,2)

    opnknci = open("C:\Users\ASUS\Desktop\workfile.txt",'r')
    kncii = opnknci.read()
    keys = "".join('{0:08b}'.format(x, 'b') for x in bytearray(kncii))
    kunci = keys.zfill(128)
    knci1, knci2 = splitbiner(kunci)
    knci1_1 = int(knci1,2)
    knci1_2 = int(knci2,2)

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
            ciphertext[0] = tmp_res[0]
            ciphertext[1] = tmp_res[1]
        return ciphertext

    def enkrip(pl1,pl2,k1,k2):
        plaintext = [0] * 2
        key = [0] * 2
        ciphertext = [0] * 2
        key_schedule = [0] * ROUNDS

        plaintext[0] = pl1
        plaintext[1] = pl2
        key[0] = k1
        key[1] = k2

        key_schedule = speck_key(key, key_schedule)
        ciphertext = proses_enkripsi(plaintext, key_schedule, ciphertext)
        pt1 = bin(plaintext[0])[2:].zfill(64)
        pt2 = bin(plaintext[1])[2:].zfill(64)
        enkripsi1 = hex(ciphertext[0]).rstrip("L").lstrip('0x') or "0"
        enkripsi2 = hex(ciphertext[1]).rstrip("L").lstrip('0x') or "0"
        e1 = enkripsi1.zfill(16)
        e2 = enkripsi2.zfill(16)
        enkripp = e1 + e2
        print "PT1: " + decode_binary_string(pt1)
        print "PT2: " + decode_binary_string(pt2)
        print "Hasil Enkripsi PT1 : " + e1
        print "Hasil Enkripsi PT2 : " + e2
        print "Plaintext : " + decode_binary_string(pt1 + pt2)
        print "Hasil Enkripsi : " + enkripp
        return enkripp

    def runprogram():
       nama = enkrip(nama1_1,nama1_2,knci1_1,knci1_2)
       alamat1 = enkrip(alamat1_1,alamat1_2,knci1_1,knci1_2)
       alamat2 = enkrip(alamat2_1, alamat2_2,knci1_1,knci1_2)
       alamat3 = enkrip(alamat3_1, alamat3_2,knci1_1,knci1_2)
       alamat4 = enkrip(alamat4_1, alamat4_2,knci1_1,knci1_2)
       riwayat1 = enkrip(rp1_1,rp1_2,knci1_1,knci1_2)
       riwayat2 = enkrip(rp2_1, rp2_2,knci1_1,knci1_2)
       riwayat3 = enkrip(rp3_1, rp3_2,knci1_1,knci1_2)
       riwayat4 = enkrip(rp4_1, rp4_2,knci1_1,knci1_2)
       gejalaa1 = enkrip(gj1_1,gj1_2,knci1_1,knci1_2)
       gejalaa2 = enkrip(gj2_1, gj2_2,knci1_1,knci1_2)
       gejalaa3 = enkrip(gj3_1, gj3_2,knci1_1,knci1_2)
       gejalaa4 = enkrip(gj4_1, gj4_2,knci1_1,knci1_2)

       alamatsemua = (alamat1+alamat2+alamat3+alamat4).rstrip("'").lstrip("'")
       riwayatsemua = (riwayat1+riwayat2+riwayat3+riwayat4).rstrip("'").lstrip("'")
       gejalasemua = (gejalaa1+gejalaa2+gejalaa3+gejalaa4).rstrip("'").lstrip("'")
       tambah_pasien = ("""INSERT INTO pasien (no_pasien, nama, tgl_berobat, umur,jenis_kelamin,alamat,pekerjaan,nama_dokter,ket_rekam_medik,gejala) 
                            VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"""
                        )
       add_pasien = (id,nama,tanggal,umur,jeniskelamin,alamatsemua,pekerjaan,dokter,riwayatsemua,gejalasemua)
       cur.execute(tambah_pasien, add_pasien)
       conn.commit()

    runprogram()
except pymysql.Error as error :
    print("koneksi ke database error"), error