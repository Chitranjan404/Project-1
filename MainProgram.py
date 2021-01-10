import os

def menu():
	print '1. Folder creation'
	print '2. Directory listing'
	print '3. For executing a system command'
	a=input("Enter your choice: ")
	return a

def directorychange(val1):
	if(val1==3):
		mainchoice(a)
	else:
		c=os.getcwd()
		print 'Your current directory is:',c
		b=input("Do you want to change your directory[1(Yes)/2(No)]")
		if(b==1):
			d=raw_input("Type in which dir you want to go:")
			os.chdir(d)
			e=os.getcwd()
			print 'You are now inside:',e
			mainchoice(a)
		else:
			mainchoice(a)


def mainchoice(a):
	if(a==1):
		choice1()
	elif(a==2):
		choice2()
	elif(a==3):
		choice3()


def choice1():
	f=raw_input("Enter the name of the folder:")
	os.mkdir(f)

def choice2():
	os.system('ls')

def choice3():
	b=raw_input('shell>')
	os.system(b)

#main program
a=menu()
directorychange(a)
