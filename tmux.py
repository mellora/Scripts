#!/usr/bin/env python3
from subprocess import call

session = 'TEST'
window_01 = 'test_bash'
window_01_command = ''
window_02 = 'HTOP'
window_02_command = 'htop'

if __name__ == '__main__':
    # Start new Session with specified name
    call(['tmux', 'new-session', '-d', '-s', session])
    # Rename first window
    call(['tmux', 'rename-window', '-t', '0', window_01])
    # Create second window in session
    call(['tmux', 'new-window', '-t', session, '-n', window_02])
    # Start htop in session window
    call(['tmux', 'send-keys', '-t', window_02, window_02_command, 'C-m'])
