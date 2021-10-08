#!/usr/bin/env python3
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
    # Check if Session Exists
    # Gets a list of tmux sessions open and
    # then sends it over a pipe to be read.
    session_list = Popen(
        ['tmux', 'list-sessions'],
        stderr=PIPE,
        stdout=PIPE
    )
    # Gets the piped data and converts it from a byte string to a utf-8 string.
    output_of_list = session_list.stdout.read().decode('utf-8')
    # Splits string into list based on end of line character
    output_slice_rows = output_of_list.splitlines()
    # Loops through the lines in the list, splits each line into a list,
    # gets the item at the first index, and strips the colon off of it.
    output_first_args = []
    for line_slice in output_slice_rows:
        output_first_args.append(
            line_slice.split(' ')[0].replace(':', '')
        )

    # Checks to see if the session currently exists.
    # If it does not, then run code block.
    if session not in output_first_args:
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
