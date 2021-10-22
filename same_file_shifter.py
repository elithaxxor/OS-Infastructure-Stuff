import os
import os.path
from pathlib import Path
import pathlib
import time
import shutil
from time import sleep
from tqdm import tqdm
import traceback, logging, sys, os, asyncio, random, platform, os, os.path
import IPCHECKER as IPx
from IPCHECKER import *
from subprocess import call
import pprint


# from pprint import pprint


class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False


class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"

    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"

    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"

    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"


###########
color = Colors()
spinner = Spinner()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset


############


def display_header():
    # print('*' * 75)

    color_red = Colors()
    global red0
    red0 = color_red.fgRed
    global reset0
    reset0 = color_red.reset

    x = 'x'
    print(f"{'X' * 125:^70}")
    print(f"{'X' * 125:^70}")
    pretty = f'{red0}xxx FILE-MOVER xxx{reset0}'.center(width)
    print(f'{pretty : ^70}')
    print(f"{'X' * 125: ^70}")

    one = (
        f'[USAGE] - [1] This is a python program that takes a specified file names, and moves them into an individual folder.')
    two = (
        f'[USAGE] - [2] The program works well with most download repositories, and currently gets around security measure implimented by \n[USAGE] - [2]b 1337x.to, itorrent && archive.org')
    three = (
        f'[USAGE] - [3] Download a LINK GRABBING extension from chrome, to pull the URLs off of the browsers tabs.')
    four = (f'[USAGE] - [4] Save the list into download_list.txt (Found in the Directory as this program')
    five = (
        f'[USAGE] - [5] Wait for downloads. Archive.org may be slow. The program saves both a LIST and DICT for further usage. (see functions)')
    six = (f'[SYSTEM] copyright material from Adel Al-Aali [SYSTEM]')

    print(f"{one:^70}")
    print(f"{two:^70}")
    print(f"{three:^70}")
    print(f"{four:^70}")
    print(f"{five:^70}")
    print(f"{six:^70}")
    print(f"{x * 20: ^70}")
    print(), print()


def clear():
    # check and make call for specific operating system
    os_name = platform.system()
    _ = call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')


def shellSort0(input_list):
    global j, temp
    global gap
    gap = len(input_list) // 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
    # Sort the sub list for this gap
    while j >= gap and input_list[j - gap] > temp:
        input_list[j] = input_list[j - gap]
        j = j - gap
        input_list[j] = temp
    # Reduce the gap for the next element
    gap = gap // 2
    return input_list


class change_info():
    def __init__(self, p):
        # change_dirs = self.change_dirs
        self.p = p

    def make_dirs(self, p):
        ## creates child path using p
        return f'Changing {self.p}'

    def move_dirs(self, p):
        # first seperate files names 
        # move dirs using os and sub-dirs using Path (p)
        pass

    def move_files(self, p):
        pass


try:
    print(IPx.IP)
    # print(f'\033[0;35;47m \t\t[{IPx.get_ip()}]  ...? \033[0m 0;35;47m')
    width = os.get_terminal_size().columns  # set the width to center goods
    terminal = os.environ.get('TERM')
    width_len = width
    cwd = os.getcwd()
    IP = f"\033[1;35;0m {IPx.IP}"
    current_version = platform.release()
    system_info = platform.platform()
    os_name0 = platform.system()

    display_header()
    print(), print()
    print('X' * 150)
    print('X' * 150)
    print()
    print(f'SYSTEM INFO'.center(width))
    print(f'\033[1;35;m [{current_version}]  ...? '.center(width))
    print(f'\033[1;35;m [{os_name0}] + [{terminal}] ...? '.center(width))
    print(f'\033[1;35;m [{system_info}]  ...? '.center(width))
    print(f'\033[1;35;0m [{current_version}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{IP}]  ...? '.center(width))  ### ADDD YOUR IP

    print('X' * 150)
    print('X' * 150)
    print()

    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))

    time.sleep(.5)
    clear()

except OSError as ose:
    print(str(ose))
except Exception as E:
    traceback.print_exc()
    print(str(E))

#
# Pure path objects provide path-handling operations which don’t actually access a filesystem.
#
# Concrete paths are subclasses of the pure path classes. In addition to operations provided by the former(pure path), they also provide methods
# # to do system calls on path objects.

# In conclusion, PurePath acts like string (remove parts of path, join with another path, get parents etc). To remove directory, search d
# irectory, create a file or write to file, you must use Path object.


###########################################################
# get cwd, # ask user if they would like to see path dir listing#
# save available paths to dictionary
# ask user if thery would like to see avail files
# save to dir list or dict for sorting..
# take first portion of file folder or name and create new folder with it
# move all of the found folders/ files into folder
###########################################################
## get vars ##


try:
    pass
except Exception as E:
    traceback.print_exc()
    print(str(E))

starting_path = os.getcwd()
answer_00 = ['yes', 'Yes', 'YES', 'y', 'Y']
answer_01 = ['No', 'NO', 'n', 'no', 'N']
print(f'Your Directory Type: {platform.platform()}'), print()
print(
    f' Enter The Path You Would Like To Work on: \n This is your Current Working Directory {bblue}{starting_path}{reset} \n')
print(f"Alternately, you can type {yellow} [cwd], [c], or [here] {reset} to work in the current directory")
path_to_work_in = input()

cwd_ans = ['cwd', 'c', 'here', 'home', '']
fail_check = ['/']

## find path

try:
    if path_to_work_in in cwd_ans:
        p = Path(starting_path)  ## create path object

    elif path_to_work_in in fail_check:
        p = Path(path_to_work_in)  ## create path object
        print(f' Moving CWD to: {bblue}{path_to_work_in}{reset}')

    else:  # if any garbage is thrown at us
        strike_out = 1
        while strike_out <= 5:
            chances = strike_out - 5
            print(f"** Directory Input Invalid, you have {red}{chances} chances before sys.exit(){reset}")
            path_to_work_in = input()
            if path_to_work_in in cwd_ans:
                print(' Thank you for entering correct path.')
                break
            else:
                strike_out += 1
                print(f"**Yet again, invalid input, you have {chances} chances before sys.exit()")
                print()
                print('X' * 50)
                print(
                    f'** Stop messing with me.. {red} type yes for CWD or enter the correct directory. {reset}'), print()
                if strike_out == 5:
                    print(' You entered too an invalid path too many times, system exiting'), time.sleep(2)
                    sys.exit(0)
                continue
except Exception as f:
    print()
    traceback.print_exc()
    print('X' * 50)
    print(str(f))

    print()

## or while?
if p.exists():
    if platform.platform() == "Linux-4.4.0-22000-Microsoft-x86_64-with-glibc2.32":
        print('It seems you may be on Windows WSL, here is your CWD: ')
        wsl_path = pathlib.Path.cwd()
        print(wsl_path)
        print(), print()
        global PARENT
        PARENT = pathlib.Path(__file__).parent.resolve()
        print(PARENT)

    try:
        fail_tick = 0
        while fail_tick <= 3:
            print('f View Directory Listing? [Yes or y]')
            question_input = input('')
            if question_input in answer_00:
                ## DIRECTORIES ##
                print(f'{blue} :: Directories :: {reset}')
                dirs = os.listdir()
                dirs.sort()
                pprint.pprint(dirs)

                ## SUB DIRECTORIES ##
                print(f'{blue} :: Sub-Directories :: {reset}')
                subdirs = [x for x in p.iterdir() if x.is_dir()]
                subdirs.sort()
                pprint.pprint(subdirs)
                file_choices = ['1','[1]', 'files']
                folder_choices = ['2','[2]', 'folders']

                print('X' * 50)
                print(' :: PARENT DIR::')
                print(PARENT)
                print('** Choose [1] move similar files or [2] similar folders')
                choice = input('')
                if choice in file_choices:
                    print(), print()
                    print(
                        f'{bblue} :: Moving Similarly  Files into new directory :: {reset}')
                    file_00 = change_info(p)
                    move_files = file_00.move_files(p)
                    print(move_files)
                    pass
                elif choice in folder_choices:
                    folder_00 = change_info(p)
                    move_folder = folder_00.move_dirs(p)

            elif question_input in answer_01:
                print('## Saving Directory Contents to Dict ##')
                break
            else:
                sys_exit = 3 - fail_tick
                print(f'Invalid Input, you have {sys_exit} tries before sys.exit')
                fail_tick += 1
                if fail_tick == 3:
                    print('Too many invalid attempts, system exiting.. ')
                    time.sleep(1)
                    sys.exit(0)

    except Exception as f:
        traceback.print_exc()
        print(str(f))
#
# else: ## if it is not a path, return back to user input
# pass
