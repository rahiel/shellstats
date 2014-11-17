#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
from os import getenv
from os.path import isfile


def main():
    history_file = get_history()
    if not history_file:
        print("Shell history not found.")
    with open(history_file, 'r') as h:
        history = [l.strip() for l in h.readlines() if l.strip()]
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
    for i in range(10):
        cmd = frequency[i]
        count = commands[cmd]
        print("{i:>3} {cmd:<20} {count:<10} {percent:<3.3}%"
              .format(i=i+1, cmd=cmd, count=count, percent=count / total * 100))
    return frequency


def get_history():
    """Get the history file for the shell in use."""
    shell = getenv("SHELL").split('/')[-1]
    home = getenv("HOME") + '/'
    hist = {"bash": [".bash_history"], "fish": [".config/fish/fish_history"],
            "zsh": [".zhistory", ".zsh_history"]}
    if shell in hist:
        for history in hist[shell]:
            if isfile(home + history):
                return home + history


if __name__ == "__main__":
    main()
