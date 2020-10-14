#!/usr/bin/env python3
# -*- coding:utf-8 -*-



def read_csv(file_input):
	with open(file_input, encoding="utf-8") as f:
		file_read = f.read()
	return file_read

def get_res(file_name):
	file_reading = read_csv(file_name)
	x = file_reading.count("婦人")
	y = file_reading.count("土狗")
	z = file_reading.count("男")
	res = [("婦人", x), ("土狗", y), ("男", z)]
	return res

if __name__== "__main__":
	files = ("example/dbp.txt", "example/pbd.txt")
	print("dpb.txt:" , get_res(files[0]) , " , pbd.txt:" , get_res(files[1]))