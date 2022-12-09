from subprocess import run

if getenv("USER") != "root":
    run(["sudo", "python", __file__] + argv[1:])
    exit(0)

def get_programs_from_packagestxt(f):
    return open(f).read().split()

run(["pacman", "-S", "--needed", get_programs_from_packagestxt("packages.archwm.txt")])
