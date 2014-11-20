# -*- coding: utf-8 -*-
from __future__ import division
from os import getenv
from os.path import isfile
from sys import exit

import click


@click.command()
@click.option("--n", default=10, help="How many commands to show.")
@click.option("--history-file", type=click.Path(exists=True, readable=True),
              default=None, help="Read shell history from history-file.")
@click.option("--plot", is_flag=True, help="Plot command usage in pie chart.")
def main(n, plot, history_file):
    """Print the most frequently used shell commands."""
    history = get_history(history_file)
    commands = {}
    for line in history:
        cmd = line.split()
        if cmd[0] in commands:
            commands[cmd[0]] += 1
        else:
            commands[cmd[0]] = 1

    total = len(history)
    # counts :: [(command, num_occurance)]
    counts = sorted(commands.items(), key=lambda x: x[1], reverse=True)
    print_top(n, counts, total)
    if plot:
        pie_top(n, counts)
    return counts


def pie_top(n, counts):
    """Show a pie chart of n most used commands."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        click.echo(click.style("Please install matplotlib for plotting.", fg="red"))
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
    click.echo("{:>3} {:<20} {:<10} {:<3}"
               .format('', "Command", "Count", "Percentage"))
    # min for when history is too small
    for i in min(range(n), range(len(counts)), key=len):
        cmd, count = counts[i]
        click.echo("{i:>3} {cmd:<20} {count:<10} {percent:<3.3}%"
                   .format(i=i+1, cmd=cmd, count=count,
                           percent=count / total * 100))


def get_history(history_file):
    """Get usage history for the shell in use."""
    shell = getenv("SHELL").split('/')[-1]
    if history_file is None:
        home = getenv("HOME") + '/'
        hist_files = {"bash": [".bash_history"],
                      "fish": [".config/fish/fish_history"],
                      "zsh": [".zhistory", ".zsh_history"]}
        if shell in hist_files:
            for hist_file in hist_files[shell]:
                if isfile(home + hist_file):
                    history_file = home + hist_file
        if not history_file:
            click.echo(click.style("Shell history file not found.", fg="red"))
            exit()

    with open(history_file, 'r') as h:
        history = [l.strip() for l in h.readlines() if l.strip()]
    if shell == "fish":
        history = [l[7:] for l in history if l.startswith("- cmd:")]
    elif shell == "zsh":
        hist = []
        for l in history:
            if l.startswith(': '):
                hist.append(l.split(';', 1)[-1])
            else:
                hist.append(l)
        history = hist
    return history
