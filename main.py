import os
import sys
import inspect
import argparse

from imgrename import core

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],".\imgrename")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

def main():
    args = parse_args(sys.argv[1:])
    if os.path.isdir(args.dir):
        core.rename_imgs(args.dir)
    else:
        print("Given directory doesn't exist.")
        print("Usage: main.py <directory>")

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Directory with the images which should be renamed.")
    return parser.parse_args(args)

if __name__ == "__main__":
    main()