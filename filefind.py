import os

def fild_all_files(directory):
    #print directory
    for root, dirs, files in os.walk(directory):
        #yield root
        for file in files:
            if file.find("xml") != -1:
                yield os.path.join(root, file)


#for file in fild_all_files('/Users/hideaki/Documents/2015Stanford-Python/data'):
#    print file
