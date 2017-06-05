

# Logika Fuzzy 
adalah peningkatan dari logika Boolean yang mengenalkan konsep kebenaran sebagian. Di mana logika klasik menyatakan bahwa segala hal dapat diekspresikan dalam istilah binary (0 atau 1, hitam atau putih, ya atau tidak), logika fuzzy menggantikan kebenaran boolean dengan tingkat kebenaran. Logika fuzzy adalah suatu cara yang tepat untuk memetakan suatu ruang input ke dalam suatu ruang output. Skema logika fuzzy adalah sebagai berikut:

<p align="center">
  <img src="/img/fuzzy1.jpg" width="400px">
</p>

# Sistem fuzzy 
mempunyai beberapa keuntungan bila dibandingkan dengan sistem tradisional, misalkan pada jumlah aturan yang dipergunakan. Pemrosesan awal sejumlah besar nilai menjadi sebuah nilai derajat keanggotaan pada sistem fuzzy mengurangi jumlah nilai menjadi sebuah nilai derajat keanggotaan pada sistem fuzzy mengurangi jumlah nilai yang harus dipergunakan pengontrol untuk membuat suatu keputusan. Keuntungan lainnya adalah sistem fuzzy mempunyai kemampuan penalaran yang mirip dengan kemampuan penalaran manusia. Hal ini disebabkan karena sistem fuzzy mempunyai kemampuan untuk memberikan respon berdasarkan informasi yang bersifat kualitatif, tidak akurat, dan ambigu.

<p align="center">
  <img src="/img/AGS2.jpg" width="400px">
</p>

Sistem fuzzy secara umum terdapat 5 langkah dalam melakukan penalaran, yaitu:

Memasukkan input fuzzy.

Mengaplikasikan operator fuzy.

Mengaplikasikan metode implikasi.

Komposisi semua output.

Defuzifikasi.

Pada himpunan tegas (crisp set), nilai keanggotaan suatu item x dalam suatu himpunan A (ditulis mA[x]) memiliki 2 kemungkinan :
Satu (1), artinya x adalah anggota A
Nol (0), artinya x bukan anggota A

Contoh :

  “Jika suhu lebih tinggi atau sama dengan 80 oF, maka suhu disebut panas, sebaliknya disebut tidak panas”

Metode Sugeno mirip dengan metode Mamdani, hanya output (konsekuen) tidak berupa himpunan fuzzy, melainkan berupa konstanta atau persamaan liniar. Ada dua model metode Sugeno yaitu model fuzzy sugeno orde nol dan model fuzzy sugeno orde satu. Bentuk umum model fuzzy sugeno orde nol adalah :


IF (x1 is A1) o (x2 is A2) o ….. o (xn is An) THEN z = k

Bentuk umum model fuzzy Sugeno orde satu adalah :

IF (x1 is A1) o (x2 is A2) o ….. o (xn is An) THEN z = p1.x1 + … pn.xn + q

Defuzzifikasi pada metode Sugeno dilakukan dengan mencari nilai rata-ratanya.

•Operasi logika adalah operasi yang mengkombinasikan dan memodifikasi 2 atau lebih himpunan fuzzy.

•Nilai keanggotaan baru hasil operasi dua himpunan disebut firing strength atau a predikat, terdapat 3 operasi dasar pada himpunan fuzzy :

–OR (Union)

–AND (Intersection)

–NOT (Complement)

Daftar Pustaka:
http://socs.binus.ac.id/2012/03/02/pemodelan-dasar-sistem-fuzzy
https://hxpinter.files.wordpress.com/2013/01/ai-06-fuzzy.ppt

Github Fitri Fadhilah

Link Scan Plagiarism
[1] Duplichecker
[2] Smallseotools