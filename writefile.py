f = open("demofile2.txt", "w")
for i in range(500000):
    f.write("Now the file has more content!\n")
f.close()
