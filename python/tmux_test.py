#!/usr/bin/env python3
'''
    This script was created to automate starting programs/scripts within a
    tmux session.  Needs at least one dictionary defined in the windows
    dictionary to work.  Subdictionaries need to have 2 key value pairs, the
    name and command keys.
'''
# Standard Imports
from subprocess import call, PIPE, Popen

session = 'TEST'
windows = {
    'window_1': {
        'name': 'test_bash',
        'command': 'ls'
    },
    'window_2': {
        'name': 'HTOP',
        'command': 'htop'
    }
}

if __name__ == '__main__':
    # Check if Session Exists and pipes the output
    session_list = Popen(
        ['tmux', 'list-sessions'],
        stdout=PIPE,
        stderr=PIPE
    )
    # Gets piped output from session list and runs the grep command
    session_grep = Popen(
        ['grep', session],
        stdin=session_list.stdout,
        stdout=PIPE,
        stderr=PIPE
    )

    # Makes sure process closes
    session_list.stdout.close()

    # Allows output of commands to be used and closes the process
    session_output, session_error = session_grep.communicate()

    # Decodes output from a binary string to a utf-8 string.
    # Allows an easier way to check if string is empty.
    session_output_clean = session_output.decode('utf-8')

    # Checks to see if the session currently exists.
    # If it does not, then run code block.
    # The variable will be equal to an empty string if session
    # does not exist at time of execution.
    if session_output_clean == "":
        # Start new Session with specified name
        call([
            'tmux',
            'new-session',
            '-d',
            '-s',
            session]
        )
        window_1 = windows.pop('window_1')
        # Rename default first window
        call([
            'tmux',
            'rename-window',
            '-t',
            '0',
            window_1['name']
        ])
        call([
            'tmux',
            'send-keys',
            '-t',
            window_1['name'],
            window_1['command'],
            'C-m'
        ])
        # Loop through the rest of the windows
        for key in windows:
            window = windows[key]
            # Create second window in session
            call([
                'tmux',
                'new-window',
                '-t',
                session,
                '-n',
                window['name']
            ])
            # Start htop in session window
            call([
                'tmux',
                'send-keys',
                '-t',
                window['name'],
                window['command'],
                'C-m'
            ])
