"""Main script file for the imgrename package.

Use this script from your command line console to rename you images.
Example:
> python main.py -r C:\imgFolder

The flag '-r' is optional an can be used, if you want to rename images in all
subfolders as well. Leave it out, if you don't.
"""

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

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Directory with the images which should be renamed.")
    parser.add_argument("-r", "--recursive", action="store_true", 
                            help="Changes also names in subfolders")
    return parser.parse_args(args)

def main():
    args = parse_args(sys.argv[1:])
    if os.path.isdir(args.dir):
        print("\nStarting renaming...")
        for (path, _dirs, _files) in os.walk(args.dir):
            core.rename_imgs(path)
        print("...renaming finished.")
    else:
        print("Given directory doesn't exist.")
        print("Usage: main.py <directory>")

if __name__ == "__main__":
    main()