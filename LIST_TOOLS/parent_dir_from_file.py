import os, sys 

def getParentDirectoryFromFile(absolutePathToFile):
    splitResutsFromZeroToNMinus1 = absolutePathToFile.split(os.sep)[:-1]
    pprint.pprint(splitResutsFromZeroToNMinus1)
    return f'** {yellow}file found in {reset} \n {os.sep.join(splitResutsFromZeroToNMinus1)}'

  
 absolutePathToFile = os.getcwd()
 getParentDirectoryFromFile(absolutePathToFile)
