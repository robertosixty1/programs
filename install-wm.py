#!/bin/env python3

from subprocess import run
from os import getenv
from sys import argv

HOME = "/home/" + listdir("/home")[0]

if getenv("USER") != "root":
    run(["sudo", "python", __file__] + argv[1:])
    exit(0)

def get_programs_from_packagestxt(f):
    return open(f).read().split()

run(["pacman", "-S", "--needed"] + get_programs_from_packagestxt("packages.archwm.txt"))

# install compton

dependencies = [
    "libx11",
    "libxcb",
    "libXext",
    "xorgproto",
    "xcb-util",
    "libxdamage",
    "libxfixes",
    "shapelib",
    "xcb-util-renderutil",
    "libxrender",
    "libxrandr",
    "libxcomposite",
    "xcb-util-image",
    "libxpresent",
    "libxinerama",
    "pixman",
    "dbus",
    "libconfig",
    "mesa",
    "pcre2",
    "pcre",
    "libevdev",
    "uthash",
    "asciidoc"
]

run(["pacman", "-Syu", "--needed"] + dependencies)

run(["git", "clone", "https://github.com/tryone144/compton", f"{HOME}/.cache/compton"])

run(["make"], cwd=f"{HOME}/.cache/compton")
run(["make", "docs"], cwd=f"{HOME}/.cache/compton")
run(["make", "install"], cwd=f"{HOME}/.cache/compton")
