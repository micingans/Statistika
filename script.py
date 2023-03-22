#!/usr/bin/env python3

# This code belong to developer @micingans

import math
import re
import os
from collections import Counter

def jarak(s):
	jarak = max(s) - min(s)

	return jarak

def kelas(s):
	panjang = jarak(s) / panjang_kelas(s)

	return round(panjang)

def banyak(s):
	banyak = len(s)

	return banyak

def panjang_kelas(s):
	much = banyak(s)
	besar = (1 + (3.3)*(math.log(much)))

	return round(besar)

data = list(map(int, input("Masukkan data : ").strip().split()))
sort = sorted(data)

angka = Counter(sort)

sering_muncul = angka.most_common(1)[0][0]

kecil = min(sort)
besar = max(sort)

# print(besar)
os.system('clear')
print(f"\nData = {data}\n")
print(f"Data yang sudah disusun = {sort}\n")
print(f"Jumlah data = {banyak(data)}\n")
print(f"Rentang data = {jarak(sort)}\n")
print(f"Panjang Kelas data = {panjang_kelas(data)}\n")
print(f"Kelas data = {kelas(sort)}\n")
print(f"Interval data {kecil}-{kecil + panjang_kelas(sort)-1}")
for x in range(kecil, kecil + panjang_kelas(sort)):
	for a in str(sort.count(x)):
		banyak_data = a
	print(f"Interval data {x} -> {banyak_data}")
print("")

print(f"Interval data {kecil + panjang_kelas(sort)}-{(kecil + panjang_kelas(sort)) + panjang_kelas(sort)-1}")
for x in range(kecil + panjang_kelas(sort), (kecil + panjang_kelas(sort)) + panjang_kelas(sort)):
	for a in str(sort.count(x)):
		banyak_data = a
	print(f"Interval data {x} -> {banyak_data}")
print("")

print(f"Interval data {(kecil + panjang_kelas(sort)) + panjang_kelas(sort)}-{((kecil + panjang_kelas(sort)) + panjang_kelas(sort)) + panjang_kelas(sort)-1}")
for x in range((kecil + panjang_kelas(sort)) + panjang_kelas(sort), ((kecil + panjang_kelas(sort)) + panjang_kelas(sort)) + panjang_kelas(sort)):
	for a in str(sort.count(x)):
		banyak_data = a
	print(f"Interval data {x} -> {banyak_data}")
print("")

print(f"Interval data {(kecil + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort)}-{((kecil + panjang_kelas(sort)) + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort)-1}")
for x in range((kecil + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort), ((kecil + panjang_kelas(sort)) + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort)):
	for a in str(sort.count(x)):
		banyak_data = a
	print(f"Interval data {x} -> {banyak_data}")
print("")

print(f"Interval data {(kecil + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort)}-{((kecil + panjang_kelas(sort)) + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort)-1}")
for x in range((kecil + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort), ((kecil + panjang_kelas(sort)) + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort)):
	for a in str(sort.count(x)):
		banyak_data = a
	print(f"Interval data {x} -> {banyak_data}")
print("")

print(f"Interval data {(kecil + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort)}-{((kecil + panjang_kelas(sort)) + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort)-1}")
for x in range((kecil + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort), ((((kecil + panjang_kelas(sort)) + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort)))):
	for a in str(sort.count(x)):
		banyak_data = a
	print(f"Interval data {x} -> {banyak_data}")
print("")

print(f"Interval data {(kecil + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort)}-{((kecil + panjang_kelas(sort)) + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort)-1}")
for x in range((kecil + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort), (((kecil + panjang_kelas(sort)) + panjang_kelas(sort)) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort) + panjang_kelas(sort))):
	for a in str(sort.count(x)):
		banyak_data = a
	print(f"Interval data {x} -> {banyak_data}")
print("")
