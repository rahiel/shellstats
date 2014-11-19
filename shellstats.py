#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
from os import getenv
from os.path import isfile
from sys import argv, exit


def main(n=10):
    history = get_history()
    if not history:
        print("Shell history not found.")
        exit()
    commands = {}
    for line in history:
        cmd = line.split()
        # if not cmd: continue
        if cmd[0] in commands:
            commands[cmd[0]] += 1
        else:
            commands[cmd[0]] = 1

    total = len(history)
    counts = sorted(commands.items(), key=lambda x: x[1], reverse=True)
    print_top(n, counts, total)
    pie_top(n, counts)
    return counts


def pie_top(n, counts):
    """Show a pie chart of n most used commands."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Please install matplotlib to use this option.")
        exit()
    label, x = zip(*counts[:n])
    fig = plt.figure()
    fig.canvas.set_window_title("ShellStats")
    plt.axes(aspect=1)
    plt.title("Top {0} used shell commands.".format(min(n, len(counts))))
    plt.pie(x, labels=label)
    plt.show()


def print_top(n, counts, total):
    """Print the top n used commands."""
    print("{:>3} {:<20} {:<10} {:<3}".format('', "Command", "Count", "Percentage"))
    # min for when history is too small
    for i in min(range(n), range(len(counts)), key=len):
        cmd, count = counts[i]
        print("{i:>3} {cmd:<20} {count:<10} {percent:<3.3}%"
              .format(i=i+1, cmd=cmd, count=count, percent=count / total * 100))


def get_history(history_file=None):
    """Get usage history for the shell in use."""
    if history_file is None:
        shell = getenv("SHELL").split('/')[-1]
        home = getenv("HOME") + '/'
        hist_files = {"bash": [".bash_history"], "fish": [".config/fish/fish_history"],
                      "zsh": [".zhistory", ".zsh_history"]}
        if shell in hist_files:
            for hist_file in hist_files[shell]:
                if isfile(home + hist_file):
                    history_file = home + hist_file
        if not history_file:
            print("Shell history file not found.")
            exit()

    with open(history_file, 'r') as h:
        history = [l.strip() for l in h.readlines() if l.strip()]
    if shell == "fish":
        history = [l[7:] for l in history if l.startswith("- cmd:")]
    return history


if __name__ == "__main__":
    if len(argv) > 1:
        main(int(argv[1]))
    else:
        main()
