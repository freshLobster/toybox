import sys
import string
import subprocess

filename = sys.argv[1]
infile = open(filename, 'r')
filetext = infile.read()
infile.close()
filetext = filetext.lower()
cleanfiletext = '\n\n'
for character in filetext:
	if character.isalnum():
		cleanfiletext += character
	elif character == ' ':
		cleanfiletext += character
	elif character == '.':
		cleanfiletext += '.\n'
	elif character == '?':
		cleanfiletext += '?\n'
	elif character == '\n':
		cleanfiletext += ' '

cleanfilename = 'clean'+filename
create_command = 'touch '+cleanfilename
subprocess.call(create_command, shell=True)
cleanfile = open(cleanfilename, 'w')
cleanfile.write(cleanfiletext)
cleanfile.close()
print cleanfilename + 'created\n'
