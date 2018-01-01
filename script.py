import subprocess
import sys
import urlparse

skyIp = '192.168.0.2'

params = urlparse.parse_qs('&'.join(sys.argv[1:]))
command = params.get('command', None)[0]
	
		
if command == 'bbc1':
	command = '1 1 5'
elif command == 'bbc2':
	command = '1 0 2'
elif command == 'channel4':
	command = '2 2 7'
elif command == 'info':
	command = 'i'
elif command == 'tvguide':
    command = 'tvguide tvguide down'	
elif command == 'pagedown':
	command = 'down down down down down down down down'
elif command == 'pageup':
	command = 'up up up up up up up up'
elif command == 'rewind':
	command = 'rewind rewind rewind rewind'
elif command == 'fastforward':
	command = 'fastforward fastforward fastforward fastforward'
	
cliString = 'sky-remote-cli {} {}'.format(skyIp, command)	
print cliString

subprocess.check_call(cliString, shell=True)