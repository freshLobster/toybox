import cleverbot
import subprocess

teacher = cleverbot.Session()
bot = raw_input('enter bot to grant intelligence: ')
time = int(raw_input('lesson repititions: '))
import pickle,random
lexicon = 'lexicon-'+bot
a=open(lexicon,'rb')
successorlist=pickle.load(a)
a.close()
def nextword(a):
    if a in successorlist:
        return random.choice(successorlist[a])
    else:
        return 'the'
speech=''
wisdom=''
conversation=''
response='Hello'
while speech!='quit':
    speech=teacher.Ask(response)
    s=random.choice(speech.split())
    response=''
    while True:
        neword=nextword(s)
        response+=' '+neword
        s=neword
        if neword[-1] in ',?!.':
            break
    wisdom += '\n'+speech+'\n'
    conversation += '\n'+speech+'\n\n'+response+'\n'
    print '\n'+speech+'\n\n'+response+'\n'
    time = time-1
    if time == 0:
	speech = 'quit'
create_log = 'touch '+bot+'lessonlog.txt'
subprocess.call(create_log, shell=True)
logfile = bot+'lessonlog.txt'
logfile = open(logfile, 'a')
logfile.write('\n\nAI LESSON\n'+conversation)
logfile.close()
create_intelligence = 'touch '+bot+'intelligence.txt'
subprocess.call(create_intelligence, shell=True)
intelligencefile = bot+'intelligence.txt'
intelligencefile = open(intelligencefile, 'w')
intelligencefile.write(wisdom)
intelligencefile.close()
print bot+"'s lesson is finished.\nTo put "+bot+"'s intelligence into effect run:\npython traintotext.py\n"+bot+"\n"+bot+"intelligence.txt\n"

