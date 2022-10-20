#!/bin/env python3

from os import getenv
from subprocess import run

def get_programs_from_packagestxt(f):
    return open(f).read().split()

if getenv("USER") != "root":
    run(["sudo", "python", __file__])
    exit(0)

run(["apt", "install"] + get_programs_from_packagestxt("packages.ubuntu.txt"))