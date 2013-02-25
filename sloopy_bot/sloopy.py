import pickle,random
import subprocess
a=open('lexicon-sloopy','rb')
successorlist=pickle.load(a)
a.close()
def nextword(a):
    if a in successorlist:
        return random.choice(successorlist[a])
    else:
        return 'the'
speech=''
human=''
conversation=''
while speech!='quit':
    if speech!='quit':
	human += speech
    speech=raw_input('>')
    s=random.choice(speech.split())
    response=''
    while True:
        neword=nextword(s)
        response+=' '+neword
        s=neword
        if neword[-1] in ',?!.':
            break
    print response
    conversation += '\n'+speech+'\n\n'+response+'\n'
create_log = 'touch '+'sloopylessonlog.txt'
subprocess.call(create_log, shell=True)
logfile = 'sloopylessonlog.txt'
logfile = open(logfile, 'a')
logfile.write('\n\n\nHUMAN\n'+conversation)
logfile.close()
create_human = 'touch '+'sloopyhuman.txt'
subprocess.call(create_human, shell=True)
humanfile = 'sloopyhuman.txt'
humanfile = open(humanfile, 'w')
humanfile.write(human)
humanfile.close()
