import os
print '1. Folder creation'
print '2. Directory listing'
print '3. For executing a system command'
a=input("Enter your choice: ")
if(a==1):
	b=raw_input("Enter the name of the folder:")
	c=os.getcwd()
	print 'Your current directory is:',c
	f=input("Do you want to change your directory[1(Yes)/2(No)]")
	if(f==1):
		d=raw_input("Type in which dir you want to go:")
		os.chdir(d)
		e=os.getcwd()
		print 'You are now inside:',e
		os.mkdir(b)
	else:
		os.mkdir(b)
elif(a==2):
	c=os.getcwd()
	print 'Your current directory is:',c
	b=input("Do you want to change your location:[1(Yes)/2(No)]:")
	if(b==1):
		d=raw_input("Type in which dir you want to go:")
		os.chdir(d)
		e=os.getcwd()
		print 'You are now inside:',e
		os.system('ls')
	else:
		os.system('ls')
elif(a==3):
	g=raw_input('shell>')
	os.system(g)
