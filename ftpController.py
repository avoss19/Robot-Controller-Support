import ftplib
import time
ftp = ftplib.FTP('192.168.21.113', 'avoss19', 'Good!682')
ftp.cwd('Desktop/Robot-Controller-Support')
past = time.time()
gFile = open("ftpTest.txt", "wb")
ftp.retrbinary('RETR ftptestFile.txt', gFile.write)
gFile.close()
ftp.quit()
print "\nReadme File Output:"
gFile = open("ftpTest.txt", "r")
buff = gFile.read()
print buff
print time.time() - past
gFile.close()
