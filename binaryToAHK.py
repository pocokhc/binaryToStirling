#! coding: Shift_JIS


def Str16(n):
	s = ""
	if n < 10:
		s=str(n)
	elif n==10:
		s="A"
	elif n==11:
		s="B"
	elif n==12:
		s="C"
	elif n==13:
		s="D"
	elif n==14:
		s="E"
	elif n==15:
		s="F"
	return s


f1 = open("無圧縮.gba","rb")
f2 = open("a.txt","w")

i=0
buf = f1.read(1)
while buf :
	val = int.from_bytes(buf, byteorder='big', signed=False)
	n1 = int(val/16)
	n2 = val%16
	f2.write("Send,"+Str16(n1)+"\n")
	f2.write("Send,"+Str16(n2)+"\n")
	
	buf = f1.read(1)
	i=i+1
	if i%1000 == 0:
		f2.write("sleep,450\n")


f1.close()
f2.close()


