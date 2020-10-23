#!/usr/bin/python3
from pwn import * 
from time import *
import re
import os

# Keep top-defined variables to a bare minimum
binary = 'bin_name'
flag_format = '(flag{.*})' # Useful for auto-regexing for expected flag with r(regex=flag_foramt)

# Payload goes here
def main():
    pass

# Define globals here; put into a function so we can collapse it in the IDE
def init():
    global p
    global throttle
    # Variable initialization
    if True: # Collapsible
        endpoint = "" # Remote challenge endpoint
        port = 1337 # Remote challenge port
        mode = 'DEBUG' # DEBUG = use GDB; else = use process() locally
        libc_name = '' # For alternate version of libc
        env = {} # Environment variables
    # Process creation 
    if True: # Collapsible
        # Local
        if mode == 'DEBUG':
            elf_name = binary  # File name

            elf = ELF(elf_name)
            if libc_name != '':
                libc = ELF(libc_name)
                env = {"LD_PRELOAD": libc.path}
            throttle = 0.35 # Extensive troubleshooting found this number sufficient for local connections even during brute forcing
            p = process(elf.path, env=env)

            # Optional GDB attach on create
            """
            context.terminal = ['tmux', 'neww', '-a'] # ['tmux', 'splitw', '-p 90']
            gdb.attach(p, gdbscript='''
            ''') 
            """
        # Remote
        else: 
            throttle = 0.7 # Can go lower if the connection is fast and not brute forcing anything
            p = remote(endpoint, port) 

## Aux functions
# Send data & print out the send
def s(data, process=None, quiet=False):
    if not process:
        process = p
    process.sendline(data)
    if not quiet:
        try:
            print('< %s' % data.decode())
        except:
            print('< %s' % str(data))

# Recv data, print out the recv, & return it
def r(limiter=None, regex=None, parse=None, timeout=1, process=None, quiet=False, delay=None):
    if not process:
        process = p
    if not delay:
        delay = throttle
    sleep(delay) # Throttling based on local VS remote
    if not regex:
        if limiter == None:
            data = process.recv(timeout=timeout)
        elif type(limiter) == int:
            data = process.recv(limiter, timeout=timeout)
        elif type(limiter) == str:
            data = process.recvuntil(limiter, timeout=timeout)
        else:
            raise Exception('Dunno what kind of limiter %s is.' % limiter)
    else:
        data = process.recvregex(regex.encode(), timeout=timeout)
    if not quiet:
        try:
            print('> %s' % data.decode())
        except:
            print('> %s' % str(data))
    if parse:
        match = re.search(parse, data.decode())
        if match:
            data = match.groups()
    try:
        return data.decode().strip('\n')
    except:
        try:
            return bytes(str(data).strip('\n'))
        except:
            return data    

if __name__ == '__main__':
    init()
    main()
