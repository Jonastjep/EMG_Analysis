filenames = ["f1","f2","f3","f4","m1","m2","m3","m4"]

for name in filenames:
	fin = open("1_Channel/"+name,"r")
	lines = fin.readlines()
	
	fout = open("ParsedData/"+name+"_OUT.csv","w")
	
	DATA = False
	for line in lines:
		if DATA:
			vals = line.split()
			volt = vals[1].replace(",",".")
			fout.write(str(time)+","+volt+"\n")
			time+=1
			
		if "Time (s)" in line:
			fout.write("Time (s),Kanaal 1\n")
			DATA = True
			time = 0
			
	fin.close()
	fout.close()

			
			
