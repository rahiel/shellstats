#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
from os import getenv
from os.path import isfile


def main():
    history = get_history()
    if not history:
        print("Shell history not found.")
    commands = {}
    for line in history:
        cmd = line.split()
        # if not cmd: continue
        if cmd[0] in commands:
            commands[cmd[0]] += 1
        else:
            commands[cmd[0]] = 1

    total = len(history)
    frequency = sorted(commands.keys(), key=lambda x: commands[x], reverse=True)
    print("{:>3} {:<20} {:<10} {:<3}".format('', "Command", "Count", "Percentage"))
    # min for when history is very small 
    for i in min(range(10), range(len(frequency)), key=len):
        cmd = frequency[i]
        count = commands[cmd]
        print("{i:>3} {cmd:<20} {count:<10} {percent:<3.3}%"
              .format(i=i+1, cmd=cmd, count=count, percent=count / total * 100))
    return frequency


def get_history(history_file=None):
    """Get usage history for the shell in use."""
    shell = getenv("SHELL").split('/')[-1]
    home = getenv("HOME") + '/'
    hist_files = {"bash": [".bash_history"], "fish": [".config/fish/fish_history"],
                  "zsh": [".zhistory", ".zsh_history"]}
    if shell in hist_files:
        for hist_file in hist_files[shell]:
            if isfile(home + hist_file):
                history_file = home + hist_file
    with open(history_file, 'r') as h:
        history = [l.strip() for l in h.readlines() if l.strip()]
    if shell == "fish":
        history = [l[7:] for l in  history if l.startswith("- cmd:")]
    return history


if __name__ == "__main__":
    main()
