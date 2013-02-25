import cleverbot
import subprocess

cbOne=cleverbot.Session()
cbTwo=cleverbot.Session()
x = cbOne.Ask('Hello')
y = cbTwo.Ask(x)
while True:
	print 'cb1: ',x
	subprocess.call('espeak -s 160 -p 30 -k20 -v en ' + '"' + x + '"', shell=True)
	x = cbOne.Ask(y)
	print 'cb2: ',y
	subprocess.call('espeak -s 160 -p 60 -k20 -v en ' + '"' + y + '"', shell=True)
	y = cbTwo.Ask(x)
