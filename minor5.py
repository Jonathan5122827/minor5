#! /usr/bin/env python

zip_dict = {}
city_dict = {}
#one = 1

def load_records(file):

	f = open(file,"r")

	lines = f.readlines()

	tuple_list = []

	tab_i = 0

	index = 0
	one = 1

	t1 = ()
	t2 = ()
	for x in lines:
		for y in range(0,len(x)):
			if x[y] == '\t' or x[y] == '\n':
				tab_i = y;
				field = x[index:tab_i]

				sint = str(one)
				field = field + sint
				one = one + 1
				#t2 = field
				a = (field,)
				t1 = t1 + a
				index = tab_i+1
		tuple_list.append(t1)
		t1 = ()
		tab_i = 0
		index = 0

#	for x in tuple_list:
#		zip_dict[x[3]] = x

	for x in tuple_list:
		city_dict[x[2]] = x

#	print city_dict
	for x in city_dict:
		if "NY" in x:
			for y in city_dict[x]:

				#lenx = len(y[1]) - 2
				#addr = y[1][0:lenx]
				print y
load_records("minor5.tsv")
