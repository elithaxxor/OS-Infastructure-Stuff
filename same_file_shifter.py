import traceback, logging, sys, os, asyncio, random, platform, os, os.path, threading
import ctypes, rich, pprint, os.path, time, shutil, pathlib
from os.path import exists
from pathlib import Path
from time import sleep
from tqdm import tqdm
import IPCHECKER as IPx
from IPCHECKER import *
from subprocess import call


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

    def __init__(self, p): #declared here instead of class head
        # change_dirs = self.change_dirs
        self.p = p

    @classmethod ## will print the class location, without (p) PATH object declared in functional portion
    def info_fromClass(cls):
        print(f'{red}  :: Information that was parsed to the Class instance :: {reset}')
        print(f'{yellow}  :: Called From CLS Method :: {reset}')
        print(f'{red} {cls.CLASS_PARENT} {reset}')
        print(f'{red} {cls.CLASS_CWD} {reset}')
        print(f'{red} {cls.CURRENT_TIME} {reset}')
        print(f'{red} {cls.CURRENT_CLOCK} {reset}')
        print(f'{red} {cls.CLASS_PATH} {reset}')

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
    def write_specific_info(info):
        try:
            with open('specific_file_info.txt', 'a') as f:
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
                    return f'{red} System Error in .txt write'
        except Exception as E:
            traceback.print_exc()
            print(f'{red}** [SYSTEM] Error in writing CWD info to .txt{reset}')
            print(str(E))
            return str(E)

    ## regex inclusions to return fnmatch.translate for include/exclude filesystems ##
    @staticmethod
    def regex_inclusions(includes):
        inclusions = r'|'.join([fnmatch.translate(x) for x in includes])
        return inclusions
    @staticmethod
    def regex_exclusions(excludes):
        exclusions = r'|'.join([fnmatch.translate(x) for x in excludes])
        return exclusions

    ## 0 display all files, ask user for ext or name, and search params. return search to code below
    ## NEED TO ADD --> Write positinal args to .txt
    def display_all_files(self, p):
        no_append = ['none','n', 'no', 'c','cancel']
        path_str = str(p)  ### <--- may have to do that weird object thing
        exclude_extension = [path_str]
        include_extension = ['.txt', '.iso', '.doc', '.rar', '.tar', '.odt', '.gz']  ## might have to take out '', it could pull in folders
        print(f' :: Exclusion list, after being parsed thru glob converter :: ')
        print(f' :: \t\t RE_INCLUDE \t\t\t  RE_EXCLUDE:: ')
        print(f' :: {re_include} parsed thru glob converter :: ')

        print(f'Finding All Folders, \n in {bblue}{p}{reset} \n current time {yellow}{self.CURRENT_CLOCK}{reset}')
        print(f'Finding All Files, \n current time {self.CURRENT_CLOCK}')
        ## glob.glob to print all files
        print(f'** Enter the Extension You are looking For ** ')
        # if input has . in it add to list, if no . start, restart recursion
        print('X' * 30)
        print(f'{blue} list for os.walk {reset}')
        print(f'{blue}|| -- root--  || -- dirs -- || -- files -- || {reset}'.center(width))
        for root, dirs, files in os.walk(p):
            print(f'{bblue}{root}, || {dirs} || {files}{reset}')

        print(), print()
        print('x' * 50)
        print(f'{blue}** list for glob.glob() {reset}')
        for extension in include_extension:
            globbed_files = glob.glob(p, f"**\**.{extension}") ## use '**' for recursiver search
            print(f'{blue} :: {globbed_files} :: {reset}')
            write_glob = get_info.subDir_write(globbed_files)
            write_globStat = get_info.subDir_write_stat(os.stat(globbed_files))
            print(f'glob {write_glob}')
            print(f'write_globStat {write_globStat}')




        print(f'**Would you like to search For specific files or file-extensions? \n'
              f'\t\t{yellow}[Key]{reset} files= files, f, names, by name\n',
              f'\t\t{yellow}[Key]{reset} [file-extensions= f, fileext, file ext, ext]')

        search_name_A = ['name', 'file name', 'n', 'N', 'NAME']
        search_ext_A = ['file-extensions', 'extension' 'fileext', 'file ext', 'ext', 'fe',]
        exit_loops = ['e','E','Exit','EXIT', 'q','Q','quit','QUIT']
        search_fileQ = input('** ')


        ### 01 ### START SEQUENCE TO PARSE BY EXTENSION
        re_exclude = regex_exclude(exclude_extension)
        print(f'**Excluded Extensions \n *{re_exclude}')
        if search_fileQ in search_ext_A: ## if user wants to search by file name
            print('X' * 50)
            print(f' Add the extensions you would like to search for. {yellow}[20 MAX]{reset}',
                  f" to exit extension chooser, enter {yellow} ['q'] {reset} or {yellow} ['quit']{reset}")
            while True:
                ticktick = 0
                add_extension = input('** ')
                print()
                if add_extension in exit_loops:
                    parsed_extensions = change_info.getByext(add_extension)
                    print(parsed_extensions)
                    break
                if add_extension in no_append:
                    parsed_extensions = change_info.getByext(add_extension)
                    print(parsed_extensions)
                    break
                if add_extension[-1] == '.': ## continue adding to list--> look for flag to break
                    Flag = True
                    while Flag:
                        include_extension.append(str(search))
                        input_extensions = change_info.getByext(add_extension)
                        re_include = regex_inclusions(input_extensions)

                        print(f'Regex Conversion: \n {re_include}')
                        print(input_extensions)

                        print()
                        print('X' * 50)
                        print(f':: Extensions that will be included in the search :: \n {"X"*35} \n\t\t {yellow} {include_extension} {reset}')
                        print(f'{red} :: Use The Exit Keys to Leave Input Loop :: {reset}')
                        continue
                    if ticktick == 20:
                        print('X' * 50)
                        print(f'{red} Limit Reached. {reset} Moving on to parse search.')
                        print(f':: Extensions that will be included in the search :: \n {"X"*35} \n\t\t {yellow} {include_extension} {reset}')
                        parsed_extensions = change_info.getByext(add_extension)
                        write_extensions = change_info.write_specific_info(parsed_extensions)
                        print(write_extensions)

                        print('**Parsed Extensions')
                        print('*', parsed_extensions)
                        return parsed_extensions
                    if add_extension in exit_loops:
                        print('X' * 50)
                        print(f'{red} User Keyed Exit. {reset} Moving on to parse search.')
                        print(f':: Extensions that will be included in the search :: \n {"X"*35} \n\t\t {yellow} {include_extension} {reset}')
                        parsed_extensions = change_info.getByext(add_extension)
                        print('**Parsed Extensions')
                        print('*', parsed_extensions)
                        return parsed_extensions
                    continue
                else:
                    ticktick += 1
                    print(f' {red} :: Invalid Extension Choice, {reset}')
                    print(f' :: You have {red} [{5 - ticktick}]  {reset} times to get it right ')
                    if ticktick == 4:
                        break
                    continue


        #### START SEQUENCE FOR SEARCH BY FILE NAME ####
        if search_fileQ in search_ext_B:
            file_name_return = []
            print('X' * 50)
            print(f'** Enter the file name paramaters that you would like to search for. \n *{yellow} MAX_LEN = [512] {reset}',
                  f" To exit search by file name, enter {yellow} ['q'] {reset} or {yellow} ['quit']{reset}")
            print(f"{red} You can exit input and parse the search values by entering {yellow}  ['e'] {reset} , or {yellow} ['exit'] {reset} at anytime. ")
            while True:
                if seach_fileQ in exit_loops:
                    print(f'{red}** Sys.exit, user-specified. {reset}')
                    print(
                        f':: Extensions that will be included in the search :: \n {"X" * 35} \n\t\t {yellow} {include_extension} {reset}')
                    specified_files = change_info.get_fileByname(file_name_return)
                    print(specified_files)
                    #return specified_files

                ticktick = 0
                add_name = input('** ')
                print()
                if not add_name:
                    print('X' * 50)
                    print(f'{red}**A specific name was not specified, parsing ALL available values. (may take some time.){reset}')
                    print(file_name_return)
                    print('X' * 50)
                    specified_files = change_info.get_fileByname(file_name_return)
                    print(specified_files)
                    return specified_files
                   # break
                if add_name in no_append:
                    print('X' * 50)
                    print(f'{red}**A specified name has an error, parsing ALL available values. (may take some time.){reset}')
                    print(file_name_return)
                    print('X' * 50)
                    specified_files = change_info.get_fileByname(file_name_return)
                    print(specified_files)
                    return specified_files
                    #break
                if add_name:
                    print('X' * 50)
                    add_name = str(add_name)
                    file_name_return.append(str(add_name))
                    print(f'{bblue} :: You added ::{reset}')
                    print(f'{yellow}** {file_name_return} {reset}')
                    print('X' * 50)
                    if len(file_name_return) > 0:
                        specified_files = change_info.get_fileByname(file_name_return)
                        print(f'{red}** Use the keys to return back to menu {reset} \n'
                              f'{yellow} {exit_loops}{reset}')
                        print(f'{bblue} :: Files specified by name :: {reset}')
                        print(specified_files)
                        saved_specified_files = class_info.write_specified_info(specified_files)
                        print(f'{red} Saved search [File-Search-byName] {reset}')
                        print(saved_specified_files)

                    continue
                elif ticktick == 100:
                    break
                else:
                    ticktick += 1
                    print(f' {red} :: Invalid Extension Choice, {reset}')
                    print(f' :: You have {red} [{5 - ticktick}]  {reset} times to get it right ')
                    if ticktick == 4:
                        break
                    continue


            print(f'**{bblue} moving on to extract filenames. {reset} \n ',
                  f'{yellow} {include_extension} {reset} \n ',
                  f'{"x" * 50}')
            print(f'** {bblue} File Extensions that will be omitted {reset} \n',
                f'{red}{exclude_extension}{reset}')
            specified_files = change_info.get_fileByext(p, include_extension, exclude_extension)
            print(), print()

      ### create new func to find specific files
       # searchFlag = True
    ## FINISH THIS
    ## use os.walk and glob ##

    ##00
    def get_fileByext(self, included_extension, excluded_extension): # might be able to remove positional params
        print('X' * 50)
        print(f' :: Excludes Extensions :: \n {red}{excluded_extension}{reset}')
        print('\t\t', excluded_extension), print()
        print('X' * 50)
        print(f' :: Included Extensions :: \n {red}{included_extension}{reset}')
        print('\t\t', included_extension), print()


        ## add ** for globber, may need to shift down a few lines
        print(f'{yellow}** Adding [**] to extension for globber{reset}')
        included_extension = ['**' + included_extension for _ in include_extensions]
        ### start of os.walk
        print('X' * 50)
        for root, dirs, files in os.walk(p, followlinks=True):
            files = [os.path.join(root, f) for f in files]
            print(files)
            files_exclude = [f for f in files if not re.match(excludes, f)]
            files_include = [f for f in files if not re.match(includes, f)]
            print(f' ** Excludes Files ** \n {red}{files_exclude}{reset}')

        regex_included_extension = regex_inclusions(included_extension)
       # print_inclusions =
        regex_excluded_extension = regex_exclusions(excluded_extension)

        print(f'{yellow}** Regexed Included {Extensinos}{reset}')
        print(f'{bblue} ** {regex_included_extension} ** {reset}')
        print(f'{yellow}** Regexed Excluded Extensinos  {reset}')
        print(f'{bblue} ** {regex_excluded_extension} ** {reset}')
        ## start of globbing
        ## get ext from included extensions,
        ## parse path to globber with ext
        ## MAY HAVE TO FSTRING / REGEX THE p OBJECT (PATH)
        for ext in included_extension:
            for file in glob.glob(f"{p}**{ext}", recursive = True):
                print(file)



        #return f'files_exclude ** \n {files_include} **'


        ## exclude files ---> dirs

    def display_all_folders(self, p):
        print('X' * 50)
        print(f'Displaying All Folders for \n \t\t {yellow} {p} {reset} \n \t\t {yellow} {self.CURRENT_CLOCK} {reset}')
        for root, dirs, files in os.walk(p, ):
            folder_list = root + dirs
            print(f'{yellow} :: Folders Found :: {reset } \n {root} + {dirs} + {files}')
            pass

            #  files_exclude = [f for f in files if not re.match(excludes, f)]
            #  files_include = [f for f in files if not re.match(includes, f)]
            # print(f' ** Excludes Files ** \n {red}{files_exclude}{reset}')



    ### FINISH THIS

    # TO GET FILE BY NAME
    def get_fileByname(self, p, file_name):
        # glob.isglob to find all files recursivly
        file_counter = 0
        ## try both isfile() and exists ##
        for root, dirs, files in tqdm(os.walk(p)):
            if file_name in files and file_name.isfile(p):
                file_names = [os.path.join(root, f) for f in files]
                print(
                    f' ** Found {yellow} [{file_counter}] {reset} files with the name {yellow} [{file_name}] {reset} ** \n {red}{files}{reset}')
                print(f'{file_names}')
            file_counter += 1
        return file_names
          #  return f'files_exclude ** \n {files_include} **'

    ## FINISH THIS
    # TO GET FILE BY FOLDER
    def get_fileByfolder(self, p, folder_name):
        # glob.isglob to find all files recursivly
        folder_counter = 0
        ## try both isfile() and exists ##
        for root, dirs, files in os.walk(p, topdown=False, followlinks=True):
            if (folder_name in dirs) and (file_name.isdirs(p)):
                folder_names = [os.path.join(dirs, f) for f in files]
            folder_counter += 1

        print(f' ** Found {yellow} [{file_counter}] {reset} directories with the name {yellow} [{folder_name}] {reset} ** \n {red}{files}{reset}')
        print(f'{folder_names}')

        return folder_names
          #  return f'files_exclude ** \n {files_include} **'

##########################################################################################
    ##########################################################################################
##########################################################################################
    ##########################################################################################
##########################################################################################



    # 1
    ### may need to convert to class method for path access . if conversion, rewrite another for instance access
    # TO FIND DUPLICATES
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

def install():
    sucessfull_install = []
    subprocess.check_call([sys.executable, "-m", "pip", "install", threading])
    if subprocess.check_call:
        print(f'{yellow} Sucessfully Installed PIP')
        sucessful_install.append('pip')
    subprocess.check_call([sys.executable, "-m", "tqdm", "install", tqdm])
    if subprocess.check_call:
        print(f'{yellow} Sucessfully Installed TQDM')
    subprocess.check_call([sys.executable, "-m", "pip", "datetime", datetime])
    if subprocess.check_call:
        print(f'{yellow} Sucessfully Installed datetime')

    print('')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
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


    ## new adds
    big_names = platform.uname()
    processor = platform.processor()
    architecture = platform.architecture()
    user_id = os.uname()
    login = os.getlogin()
    os.access(cwd)

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
    print(f'\033[1;35;0m [{big_names}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{processor}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{architecture}]  ...? '.center(width))  ###
    print(f'\033[1;35;0m [{user_id}]  ...? '.center(width))  ###
    print(f'\033[1;35;0m [{login}]  ...? '.center(width))  ###
    print(f'\033[1;35;0m [{current_version}]  ...? '.center(width))  ### ADDD YOUR IP

    while True:
        if 'Linux' in platform.system():  ## get root for linux
            try:
                print('X' * 35)
                print(f' {Red} It Seems Like your on a Linux Distro, Please start with escalate privledge. {reset} ')
                if not 'SUDO_UID' in os.environ.keys(): ##
                    print(f'**{red}Must have SU Privledges.{reset}')
                    print('[SYSTEM] Commencing Login Process. \n Enter your Password: ')
                    print('X' * 35)
                    password = getpass('* ')
                    print()
                    proc = Popen('sudo -S apache2ctl restart'.split(), stdin = PIPE, stderr = PIPE)
                    proc.communicate(password.encode())
                    if proc.communicate:
                        print(f'**{yellow}Sudo Escelation Succesfull, moving on.. {reset}')
                        break
                    print(f'{red}** Sudo failed, attempting to run w/out privledges.. {reset}')
                    break
            except exception as e:
                print('IO ERROR - MUST BE SUPER USER()): ', e)
                sys.exit(1)
        import ctypes, sys

        if 'Windows' in platform.system():
            print(f' {Red} It Seems Like your on a Windows Distro, Checking if you are admin. {reset} ')
            if is_admin(): ## windows login
                print(f'{yellow}**cool you are admin.. moving on.{reset}' )
                break
            else:
                print(f'{yellow}** Attempting To Escelate Privledges{reset}')
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                if ctypes.windll.shell32.ShellExecuteW:
                    print(f'{yellow} Windows Admin Escalation Succesful, moving on.. {reset}')
                    break
                else:
                    print(f'{red}**[ERRNO]Cannot escalate.. proceeding without privledge.. ')
                    break
        if 'Darwin' in platform.system():  ## get root for Mac
            try:
                print('X' * 35)
                print(f' {Red} It Seems Like your on a Linux Distro, Please start with escalate privledge. {reset} ')
                if not 'SUDO_UID' in os.environ.keys(): ##
                    print(f'**{red}Must have SU Privledges.{reset}')
                    print('[SYSTEM] Commencing Login Process. \n Enter your Password: ')
                    print('X' * 35)
                    password = getpass('* ')
                    print()
                    proc = Popen('sudo -S apache2ctl restart'.split(), stdin = PIPE, stderr = PIPE)
                    proc.communicate(password.encode())
                    if proc.communicate:
                        print(f'**{yellow}Sudo Escelation Succesfull, moving on.. {reset}')
                        break
                    print(f'{red}** Sudo failed, attempting to run w/out privledges.. {reset}')
                    break
            except exception as e:
                print('IO ERROR - MUST BE SUPER USER()): ', e)
                sys.exit(1)


    print('X' * 150)
    print('X' * 150)
    print()

    print(f"{'X' * 50}".center(width))
    print(f"{'X' * 50}".center(width))

    time.sleep(4)
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

# global answer_00, answer_01, starting_path
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
#
# os.F_OK: Tests existence of the path.
# os.R_OK: Tests readability of the path.
# os.W_OK: Tests writability of the path.
# os.X_OK: Checks if path can be executed
## or while?

### check if paths exists
try:
    while True:
        if not p.exists():
            print(f'{red}** Path Does  Not Exist \n[PATH]*[{p}] {reset}')
            break
        elif os.access(p, os.R_OK):
            print(f'{red}** Path Is Not Readable \n[PATH]*[{p}] {reset}')
            break
        elif os.access(p, os.W_OK):
            print(f'{red}** Path Is Not Writable \n[PATH]*[{p}] {reset}')
            break

except OSError as ose:
    traceback.print_exc()
    print(str(ose))
except Exception as E:
    traceback.print_exc()
    print(str(E))




if p.exists() and os.access(p, os.R_OK) and os.access(p, os.W_OK):
    current_platform = platform.platform()
    if platform.platform():# == "Linux-4.4.0-22000-Microsoft-x86_64-with-glibc2.32":
        print(f'**It seems you may be on {yellow} {current_platform} {reset} \n {red}*The program may not work as expected if unture.{reset} ')
        # CURRENT_TIME = time.time()
        # CURRENT_CLOCK = time.ctime(CURRENT_TIME)
        # CLASS_PATH = pathlib.Path.cwd()
        class_info = change_info(p)
        wsl_path = pathlib.Path.cwd()

        print(f'{red} {class_info.info_fromClass()}{reset}'), print()
        print('X' * 50)
        print(f'* :: Path from Pathlib :: \n\t {yellow} *[{wsl_path}] {reset}')

        print(), print()


        try:
            fail_tick = 0
            while fail_tick <= 3:
                print('f View Directory Listing? [Yes or y]')
                question_input = input('')
                if question_input in answer_00:
                    ## DIRECTORIES ##

                    dirs = os.listdir()
                    dirs.sort()
                    print(f'{blue} :: Directories :: {reset}')
                    print('X' * 25)
                    pprint.pprint(dirs)

                    print(f'{blue} :: Directories :: {reset}')
                    print(f':: {bblue} {dirs}{reset} ::')
                    print('X' * 25)
                    ## WRITE DIR TO .TXT ##
                    dir_stat = os.stat(p)
                    dir_write_check = change_info.write_info(f'** dirs {dirs}')
                    dir_write_stat = change_info.write_info(f'** dir_stat {dir_stat}')
                    print('** Directory Write Check ', dir_write_check)
                    ## SUB DIRECTORIES ##
                    print(), print()
                    print(f'{blue} :: Sub-Directories :: {reset}')
                    print('X' * 25)
                    subdirs = [x for x in p.iterdir() if x.is_dir()]
                    subdirs.sort()
                    pprint.pprint(subdirs)


                    print('X' * 50)
                    print(f'{bblue} :: {subdirs} :: {reset}'), print()

                    print('X' * 50)
                    print(f'{red} :: Directories :: {reset}')
                    print(f':: {red} {dirs}{reset} ::')
                    print('X' * 25)

                    ### WRITE SUB DIRS TO .TXT ###
                    ## Navigate Path object to sub dir, then print stats.
                    #
                    fileSubs_stat = os.stat(subdirs)

                    fileSubs_write_check = change_info.write_info(subdirs)  ### write the sub dir
                    subDir_write_check = change_info.write_info(f'** Sub-Dirs {subdirs}')
                    subDir_write_stat = change_info.write_info(f'** Sub-Dir-Stats {dir_stat}')

                    print(fileSubs_write_check)
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
                            x = f'{red} {find_duplicates} {reset}'
                            pprint.pprint(find_duplicates)
                            print(f'** System found {yellow}[{x}]{reset} duplicates{red}{find_duplicates} {reset}')

                elif question_input in answer_01:
                    print(' ## Saving Directory Contents to txt ##')
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
