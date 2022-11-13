'''
I'd like to know how can I divide a 24-digit binary number which is taken from user in python to 3 parts and then put different conditions on each of these 3 parts

	e.g: input => 111100011110110100100100 

divide the input to 3 equal parts (each part should have 8 digits): 

	11110001 | 11101101 | 00100100 

for the first part I want to turn the 8-digit bin num to an int num (no sign + -) 
for the second part I want to turn the 8-digit bin num to an int num (with sign + -) 
for the third part I want to take an ASCII output from the number in the 3rd part 

So the output for the example above will be: 

	241 -109 $
'''


binaryInput = input('Input your binary number: ')

binaryList = [] #blank list
for i in range(0, 24, 8): #every 8th number
	binaryList.append(binaryInput[i:i+8]) #add the number and the next 7 numbers

returnList = [] #blank list

returnList.append(int(binaryList[0], 2)) #convert from base2 to base10

if binaryList[1][0] == '1': #if first char is a 1 (ie negative)
	returnList.append(-abs(int(binaryList[1][1:], 2))) #make denary out of last 7 chars then make it negative
elif binaryList[1][0] == '0':
	returnList.append(int(binaryList[1][1:], 2)) #just convert last 7 chars to denary

returnList.append(chr(int(binaryList[2], 2))) #convert base2 to base10 then base10 to char

for byte in returnList:
	print(byte) #prints each item separably

#returnString = '' #blank string
#for byte in returnList: #for each byte
	#returnString += str(byte) + ' ' #convert it to a string and add a space buffer to end
#print(returnString) #prints as a string
