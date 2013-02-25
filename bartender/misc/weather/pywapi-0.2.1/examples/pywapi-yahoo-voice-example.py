import pywapi
import random
import subprocess

yahoo_result = pywapi.get_weather_from_yahoo('95060')
curr=yahoo_result['condition']['temp']
high=yahoo_result['forecasts'][1]['high']
low=yahoo_result['forecasts'][1]['low']
awake=["Good morning sir. I hope you slept well. ","It is now time for you to wake up. ","Rise from your bed my master, there is much to do. ","The hour has come for your awakening sire. ","This is your wake up call sir. "]

def c2ftemp(ctemp): 
	ftemp = ((int(ctemp)*9)/5)+32
	ftemp = str(ftemp)
	return ftemp
while True:
	greeting = awake[random.randint(0,4)]+" Today is " + yahoo_result['condition']['date'] + yahoo_result['condition']['title'] + " are " + c2ftemp(curr) + " degrees and " + yahoo_result['condition']['text'] + " outside. Today's high is estimated at " + c2ftemp(high) + " degrees and as for todays low it should be about " + c2ftemp(low) + " degrees. It is looking like there will be " + yahoo_result['forecasts'][1]['text'] + " today. Must I repeat myself?"
	subprocess.call('espeak -s 100 -p 50 -k20 -v en ' + '"' + greeting + '"', shell=True)
print greeting

