import subprocess

bot = raw_input('enter bot to train: ')
infile = raw_input('enter a .txt file name to train with: ')
clean_command ='python cleanfile.py '+ infile
subprocess.call(clean_command, shell=True)
infile = 'clean'+infile
infile = open(infile, 'r')
botfile = bot+'.txt'
botfile = open(botfile, 'a')

contents = infile.read()
botfile.write(contents)
print 'added to '+ bot+'s training file\n'
infile.close()
botfile.close()
train_command = 'python '+bot+'trainer.py'
replace_lexicon = 'rm lexicon-'+bot
subprocess.call(replace_lexicon, shell=True)
subprocess.call(train_command, shell=True)
print 'trained '+ bot
