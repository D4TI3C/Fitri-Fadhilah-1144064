

import time
start_time = time.time()
print("menghitung nilai rumus matematika menggunakan bahasa jepang")
p = raw_input("Masukan Nilai 1: ")
o = raw_input("Masukan Nilai 2: ")
l = raw_input("Masukan Nilai 3: ")
a = raw_input("Masukan Nilai 4: ")
r = raw_input("Masukan Nilai 5: ")

if p == 'ichi':
	p=1

if p == 'ni':
	p=2

if p == 'san':
	p=3

if p == 'yon':
	p=4

if p == 'go':
	p=5

if p == 'roku':
	p=6

if p == 'nana':
	p=7

if p == 'hachi':
	p=8

if p == 'kyuu':
	p=9

if p == 'juu':
	p=0


if o == 'ichi':
	o=1

if o == 'ni':
	o=2

if o == 'san':
	o=3

if o == 'yon':
	o=4

if o == 'go':
	o=5

if o == 'roku':
	o=6

if o == 'nana':
	o=7

if o== 'hachi':
	o=8

if o == 'kyuu':
	o=9

if o == 'juu':
	o=0

if l == 'ichi':
	l=1

if l == 'ni':
	l=2

if l == 'san':
	l=3

if l == 'yon':
	l=4

if l == 'go':
	l=5

if l == 'roku':
	l=6

if l == 'nana':
	l=7

if l == 'hachi':
	l=8

if l == 'kyuu':
	l=9

if l == 'juu':
	l=0


if a == 'ichi':
	a=1

if a == 'ni':
	a=2

if a == 'san':
	a=3

if a == 'yon':
	a=4

if a == 'go':
	a=5

if a == 'roku':
	a=6

if a == 'nana':
	a=7

if a == 'hachi':
	a=8

if a == 'kyuu':
	a=9

if a== 'juu':
	a=0


if r == 'ichi':
	r=1

if r == 'ni':
	r=2

if r == 'san':
	r=3

if r == 'yon':
	r=4

if r == 'go':
	r=5

if r == 'roku':
	r=6

if r == 'nana':
	r=7

if r == 'hachi':
	r=8

if r == 'kyuu':
	r=9

if r == 'juu':
	r=0


jumlah =(p*o)+(l/a-r)
print ("hasil" , jumlah)
print("time : %s detik " % (time.time() - start_time))
