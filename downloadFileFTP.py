from ftplib import FTP
import sys
import ftplib
import os
import fnmatch
os.chdir(r'thu muc luu file')
ftp=ftplib.FTP()
ftp.connect('host','port')
ftp.login('user','pass')
ftp.cwd('thu muc lay file tren server')
filematch='*'
import time
downloaded = []
skipped = 0
for filename in ftp.nlst(filematch):
  if filename not in downloaded:
    fhandle=open(filename, 'wb')
    print 'Getting ' + filename
    ftp.retrbinary('RETR '+ filename, fhandle.write)
    fhandle.close()
    downloaded.append(filename)
  else:
    skipped += 1
  print 'Downloaded %s, skipped %d files' % (downloaded[-1], skipped)
ftp.quit()
