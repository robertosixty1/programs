#!/bin/env python3

from subprocess import run
from os import getenv
from sys import argv

if getenv("USER") != "root":
    run(["sudo", "python", __file__] + argv[1:])
    exit(0)

def get_programs_from_packagestxt(f):
    return open(f).read().split()

run(["pacman", "-S", "--needed"] + get_programs_from_packagestxt("packages.archwm.txt"))
