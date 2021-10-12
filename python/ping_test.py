#!/usr/bin/env python3

from subprocess import call

ping_host = '8.8.8.8'
interfaces = {
    'wireless': 'wlp6s0',
    'wired': 'enp7s0'
}
number_of_pings = 4

interface = interfaces['wireless']

if __name__ == '__main__':
    print("**************************************************")
    print(f'**  From {interface}:')
    print("**************************************************")
    call([
        'ping',
        '-c',
        str(number_of_pings),
        '-I',
        interface,
        ping_host
    ])
