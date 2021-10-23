import os
import os.path
from pathlib import Path
import pathlib
import time
import shutil
from time import sleep
from tqdm import tqdm
import traceback, logging, sys, os, asyncio, random, platform, os, os.path, threading
import IPCHECKER as IPx
from IPCHECKER import *
from subprocess import call
import pprint
import rich


# from rich import print


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
    busy = True
    delay = .001
    CLASS_PARENT = pathlib.Path(__file__).parent.resolve()  ##
    CLASS_CWD = os.getcwd()
    CURRENT_TIME = time.time()
    CURRENT_CLOCK = time.ctime(CURRENT_TIME)
    CLASS_PATH = pathlib.Path.cwd()

    def __init__(self, p):
        # change_dirs = self.change_dirs
        self.p = p

    def get_sys_info(self, p):
        # print('** ::Getting System Info :: && Starting Threading Process ::')
        # while self.busy:
        print(f' :: {blue} Getting System Info ::,\n current time {reset} {yellow} {self.CURRENT_CLOCK} {reset}')
        global PARENT
        PARENT = pathlib.Path(__file__).parent.resolve()
        CURRENT_USER = os.path.basename(PARENT)
        NORMALIZE_PATH = os.path.normpath(PARENT)
        REAL_PATH = os.path.realpath(PARENT)
        WSL_PATH = pathlib.Path.cwd()
        print(f'* Path Object (p) {red} {p} {reset}')
        print(f'* WSL Path {bblue} {WSL_PATH}{reset}')
        print(f'* Current User: {bblue}{CURRENT_USER}{reset}')
        print(f'* Parent Directory {bblue}{PARENT}{reset}')
        print(f"* Normalized Path {bblue}{NORMALIZE_PATH}{reset}")
        print(f"* Real Path {bblue}{REAL_PATH}{reset}")

    @staticmethod  ## find len to get a stop pass
    def write_info(info):
        try:
            with open('file_info.txt', 'a') as f:
                if len(info) >= 0:
                    line_ticker = 0
                    for line in info:
                        strLine = str(line)
                        f.write(strLine)
                        f.write("\n")
                        line_ticker += 1
                        if line_ticker == len(info):
                            return f'Successfully wrote cwd info to .txt'

                elif not info:
                    return f'{red}No Info Found, moving on... {reset} \n [ :: List Inputted::] {bblue}{info} {reset}'
                    # pass
                else:
                    print(f'{red} System Error in .txt write')
        except Exception as E:
            traceback.print_exc()
            print(f'{red}** [SYSTEM] Error in writing CWD info to .txt{reset}')
            print(str(E))


    @staticmethod
    def regex_exclusions():
        inclusions = r'|'.join
        exclusions =

        return inclusions, exclusions
    def display_all_files(self, p):
        path_str = str(p)  ### <--- may have to do that weird object thing
        excludes = [path_str]
        includes = ['.txt', '.iso', '.doc', '.rar', '.tar', '.odt', '']  ## might have to take out '', it could pull in folders
        Includes = regex_exclusions()


        print(f'Finding All Folders, \n in {bblue}{p}{reset} \n current time {yellow}{self.CURRENT_CLOCK}{reset}')
        print(f'Finding All Files, \n current time {self.CURRENT_CLOCK}')
        print(f'** Enter the Extension You are looking For :: ')
        include_inSearch =
        for root, dirs, files in os.walk(p):
            files = [os.path.join(root, f) for f in files]
          #  files_exclude = [f for f in files if not re.match(excludes, f)]
          #  files_include = [f for f in files if not re.match(includes, f)]
            #print(f' ** Excludes Files ** \n {red}{files_exclude}{reset}')
            print(f' ** Excludes Files ** \n {red}{files}{reset}')

            return f'files_exclude ** \n {files_include} **'

        ## exclude files ---> dirs

    def display_all_folders(self, p):
        for root, dirs, files in os.walk(p):
            print(root + dirs)
            pass

    # 1
    ### may need to convert to class method for path access . if conversion, rewrite another for instance access
    def find_duplicates(self, p):
        print(f'Finding Duplicates, \n current time {self.CURRENT_CLOCK}')
        # while self.busy:  # thread t0
        for dup01, dup02 in os.path.walk(path1, path2):
            if os.path.samefile(path1, path2):
                dupe_append = []
                print(f'* :: Found Duplicates::')
                print(f'* Duplicate One :: {dup01} \t\t ** Duplicate Two :: {dup02}')
                dupe_list.append(path1, path2)

                return dup01, dup02
            else:
                break
            # break

    # 2
    def split_files(self, p):  ## first find duplicates and return them
        print(f'Splitting directories, \n current time {self.CURRENT_CLOCK}')
        print(f'[1] :: Finding Duplicate Files / Directies ')
        # dup_file, dup_folder = self.find_duplicates(self, )

        pass

    # 3
    def make_dirs(self, p):
        print(f'Making directories,\n current time {self.CURRENT_CLOCK}')
        pass

        while self.busy:
            return f'*Making Dirs'
            pass  #####
        ## creates child path using p
        return f' *Changing {self.p}'

    # 4
    def move_dirs(self, p):
        print(f'moving directories,\n current time {self.CURRENT_CLOCK}')
        while self.busy:
            for root, dirs, files in os.walk(p):
                pass
            return ' *Moving Directories'

        while self.busy:  ## initiate threading instance
            for x in os.listdir(p):
                print(x)
                if x in os.path(PARENT):
                    print(x)  # # # #
                # return x
            else:
                return f'* did not find shit to print'

        # first seperate files names
        # move dirs using os and sub-dirs using Path (p)
        pass

    # 5
    def move_files(self, p):
        while self.busy:
            return f'Moving files'
        pass

    ######### FOR THREADING #######
    def __enter__(self):
        self.busy = True
        t0 = threading.Thread(target=self.get_sys_info(p))
        t0.start()
        # t0.join()
        t1 = threading.Thread(target=self.make_dirs)
        t1.start()
        t2 = threading.Thread(target=self.move_dirs)
        t2.start()
        t2.join()
        t3 = threading.Thread(target=self.move_files)
        t3.start()
        t3.join()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False


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

################  ######################  #############################  ########################## ##############
#############  ######################  #############################  ########################## ##############


cwd_ans = ['cwd', 'c', 'here', 'home', '']
fail_check = ['/']

####
## find path
try:
    if path_to_work_in in cwd_ans:
        p = Path(starting_path)  ## create path object

    elif path_to_work_in in fail_check:
        p = Path(path_to_work_in)  ## create path object
        print(f' {red} Moving CWD to: {reset} {bblue} {p} {reset}')

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
        # CURRENT_TIME = time.time()
        # CURRENT_CLOCK = time.ctime(CURRENT_TIME)
        # CLASS_PATH = pathlib.Path.cwd()
        current_info_c = change_info(p)
        # current_info00 = \
        current_info_c.get_sys_info(p)
        # current_info00()

        ###
        wsl_path = pathlib.Path.cwd()
        print(f'* WSL Path {wsl_path}')

        print(), print()
        # global PARENT
        # PARENT = pathlib.Path(__file__).parent.resolve()
        # CURRENT_USER = os.path.basename(PARENT)
        # NORMALIZE_PATH = os.path.normpath(PARENT)
        # REAL_PATH = os.path.realpath(PARENT)
        # print(f'* Path Object (p) {p}')
        #
        # print(f'* WSL Path {wsl_path}')
        # print(f'* Current User: {CURRENT_USER}')
        # print(f'* Parent Directory {PARENT}')
        # print(f"* Normalized Path {NORMALIZE_PATH}")
        # print(f"* Real Path {REAL_PATH}")

        try:
            fail_tick = 0
            while fail_tick <= 3:
                print('f View Directory Listing? [Yes or y]')
                question_input = input('')
                if question_input in answer_00:
                    ## DIRECTORIES ##
                    print(f'{blue} :: Directories :: {reset}')
                    print('X' * 25)

                    dirs = os.listdir()
                    dirs.sort()
                    pprint.pprint(dirs)
                    ## WRITE DIR TO .TXT ##
                    dir_write_check = change_info.write_info(dirs)
                    print(dir_write_check)
                    ## SUB DIRECTORIES ##
                    print(), print()
                    print(f'{blue} :: Sub-Directories :: {reset}')
                    print('X' * 25)
                    subdirs = [x for x in p.iterdir() if x.is_dir()]
                    subdirs.sort()
                    print(f'{bblue} :: {subdirs} :: {reset}')

                    ### WRITE SUB DIRS TO .TXT ###
                    file_write_check = change_info.write_info(subdirs)  ###
                    print(file_write_check)
                    if file_write_check:
                        print(f'{bblue} : Successfully Wrote Sub-Dirs to .txt : {reset}')
                    file_choices = ['1', '[1]', 'files', 1]
                    folder_choices = ['2', '[2]', 'folders', 2]

                    ## ask user if they want to see sub-directory contents ::
                    print(f'** Would you like to see the all the sub directory contents? ')
                    all_content = input()
                    if all_content in answer_00:
                        for files in os.walk(p, topdown=False, followlinks=True):
                            pprint.pprint(files)
                    elif all_content in answer_01:
                        for files in os.walk(p, topdown=False, followlinks=True):
                            change_info.write_info(files)
                    else:
                        print(f'{red} :: INVALID INPUT :: {reset},, \n printing all dirs, then moving on..')
                        for files in os.walk(p, topdown=False, followlinks=True):
                            change_info.write_info(files)
                            pprint.pprint(files)

                    #####################  #############################
                    #####################  #############################
                    #####################  #############################
                    #####################  #############################

                    print('X' * 50)
                    print(' :: Your Working DIR::')
                    print(f"{red}{p}{reset}")
                    print(f'{red}** [MAKE SURE THE PARENT DIR BELOW IS CORRECT, PRESS CTRL + Z TO TO EXIT] {reset}  ')
                    print(f' :: PARENT DIR [To Be Worked On] \n {red} {p} {reset} ::')
                    print()
                    print(
                        f'** Choose {yellow}[1]{reset} view all files or {yellow} [2]{reset} display duplicate folders {yellow}[3]{reset} move files')
                    choice = input('')
                    ###
                    parsing_displayFile = ['1', 1, 'display files', 'display file', 'file', 'files', '[1]']
                    parsing_displayDupe = ['2', 2, 'display dupe', 'display duplicate', 'duplicates', '[2]']
                    parsing_moveFiles = ['3', 3, 'move files', 'move', '[3]']

                    ###
                    file_00 = change_info(p)  ## obj instiate
                    ## display all files
                    if choice in parsing_displayFile:
                        # move_files = file_00.move_files(p)
                        with Spinner():
                            print(f'** {bblue} initiating find_duplicates sequence {reset}')
                            x = f'{red} add amt of duplicaters {reset}'
                            print(f'** System found {x} {file_00.find_duplicates}')
                            print(), print()
                            print('X' * 50)
                            print(f"{red}{file_00.get_sys_info(p)}{reset}")  ## pulls file from class method
                            print(f'** {bblue}initiating {red} --FILE-- {reset} display-all-sequence {reset}')
                            display_files = file_00.display_all_files(p)
                            if display_files:
                                print(display_files)
                            else:
                                print('** No files found with the extension indicated')

                    # find_duplicates = file_00.find_duplicates(p)
                    elif choice in parsing_displayDupe:
                        same_files = file_00.find_duplicates(p)
                        with Spinner():
                            print(f'** {bblue}initiating {red} --FILE-- {reset} display-dupe-sequence {reset}')
                            find_duplicates = file_00.find_duplicates(p)
                            x = f'{red} add amt of duplicaters {reset}'
                            print(f'** System found {x} {find_duplicates}')
                            pass

                    ## ask uswer what they want to do. 1. display only files. 2. display duplicates. 3. group-move similar files.
                    ## MOVE FOLDERS

                    elif choice in folder_choices:
                        folder_00 = change_info(p)
                        print(), print()
                        print('X' * 50)
                        print(f' {blue}:: PARENT DIR [To Be Worked On] ::{reset}')
                        print(f"{red}{folder_00.get_sys_info(p)}{reset}")  ## pulls file from class method
                        with Spinner():
                            print(f'** {bblue}initiating find_duplicates sequence {reset}')
                            find_duplicates = folder_00.find_duplicates(p)
                            x = f'{red} add amt of duplicaters {reset}'
                            print(f'** System found {x} {find_duplicates}')

                elif question_input in answer_01:
                    print(' ## Saving Directory Contents to Dict ##')
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
