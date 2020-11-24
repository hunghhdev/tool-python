import pysftp

srv = pysftp.Connection(host="10.30.5.68", username="root", password="Admin@123")
remoteDir = "/data/cdr/PROCESS_DIR/ICBS/CPS/"
localDir = "/home/thinkpad/datatest/PROCESS_DIR/ICBS/CPS/"

for file in srv.listdir_attr(remoteDir):
    print 'get file ' + file.filename
    srv.get(remoteDir+file.filename,localDir+file.filename)

srv.close()
