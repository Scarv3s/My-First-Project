import os
import fnmatch

#Change working directory
os.chdir("C:\\Users\\Beast\\Desktop\\Python Testing\\Test")

#Variable working directory and destination directory
path = os.getcwd()
newFile = "C:\\Users\\Beast\\Desktop\\Python Testing\\Test2"
print (path)

#List of files in (path)
folderlist = os.listdir(path)
print (folderlist)

#Open and read the number in Counter.txt
counterFile = open(path + '\\Counter.txt', 'r+')
counter = int(counterFile.read())
counterFile.close()

#Displays number of files aside from Counter.txt
print("Files: " + str(len(folderlist) - 1))

#Conditional display depending on number of files
if len(folderlist) - 1 >= 1:
    print ("Renaming and moving files")
else:
    print ("No files found")

#Renaming and moving the files
for file in folderlist:
    if not fnmatch.fnmatch(file, 'Counter.txt'):
        os.rename(path + '\\' + file, newFile + '\\' + str(counter) + '.txt')
        counter += 1
        counterFile = open(path + '\\Counter.txt', 'w')
        counterFile.write(str(counter))
        counterFile.close()

#Display list of files in destination directory        
print(os.listdir(newFile))
