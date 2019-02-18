import pysftp

srv = pysftp.Connection(host="", username="", password="")
remoteDir = ""
localDir = ""

for file in srv.listdir_attr(remoteDir):
    print 'get file ' + file.filename
    srv.get(remoteDir+file.filename,localDir+file.filename)

srv.close()
