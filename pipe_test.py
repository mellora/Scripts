#!/usr/bin/env python3
'''
    This script was created to test understanding of different
    python modules to interact with the shell.
'''

from subprocess import Popen, PIPE

session = 'TEST'

session_list = Popen(
    ['tmux', 'list-sessions'],
    stdout=PIPE,
    stderr=PIPE
)
session_grep = Popen(
    ['grep', session],
    stdin=session_list.stdout,
    stdout=PIPE,
    stderr=PIPE
)

session_list.stdout.close()

session_output, session_error = session_grep.communicate()

session_output_clean = session_output.decode('utf8')

# print(session_output_clean)

if session_output_clean != "":
    print('Session Found')
else:
    print('Session Not Found')
