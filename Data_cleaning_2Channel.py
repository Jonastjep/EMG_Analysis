import os

for name in os.listdir("2_Channel/"):
	fin = open("2_Channel/"+name,"r")
	lines = fin.readlines()
	
	fout = open("ParsedData/"+name+"_OUT.csv","w")
	
	DATA = False
	for line in lines:
		if DATA:
			vals = line.split()
			volt0 = vals[1].replace(",",".")
			volt1 = vals[2].replace(",",".")
			fout.write(str(time)+","+volt0+","+volt1+"\n")
			time+=1
			
		if "Time (s)" in line:
			fout.write("Time (s),Kanaal 1,Kanaal 5\n")
			DATA = True
			time = 0
			
	fin.close()
	fout.close()

			
			
