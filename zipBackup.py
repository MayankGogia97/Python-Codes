#! python3
import os
import time
import zipfile as zf
import datetime as dt
start = time.time()
os.chdir(r'G:\Codes\Python')
cdate = dt.date.today().isoformat()
ctime = dt.datetime.now().strftime('%H-%M-%S')
zipName = 'Python_Codes %s %s.zip' % (cdate, ctime)
print('Creating the backup zip named %s ...\n' % (zipName))
zipName = ('C:\\Users\\mayan\\OneDrive\\Python Backups\\' + zipName)
backupZip = zf.ZipFile(zipName, 'w')
for curFolder, subFolders, fileNames in os.walk('.'):
    print('Backing up %s...\n' % (os.path.abspath(curFolder)))
    if curFolder != '.':
        backupZip.write(curFolder)
    for fileName in fileNames:
        fullFilePath = os.path.join(curFolder, fileName)
        print('\t\tBacking up %s...\n' % (fileName))
        backupZip.write(fullFilePath)
backupZip.close()
print('Backup finished.\nBackup took %s seconds.' % (time.time()-start))
