import string

f = open(raw_input('enter a .txt file: '),'r') # open in read mode
convo = f.read()
names = ['Ace Levenberg','Grace Anello','Sophie Isabelle Iribarren', 'Aidan IronTiger Seine', 'Neha Talreja']
total = 0

for name in names: 
	count = convo.count(name)
	total += count

for name in names:
	count = convo.count(name)
	percent = (float(count)/total)*100
	print name + ": " + str(count) + " comments, "+ str(percent)+"% of thread\n"
	
print str(total) + " comments total\n"

