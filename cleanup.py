fread = open("nvsim.cfg", "r")
fwrite = open("cleanup.cfg", "a")

for line in fread:
    if line[0] == "-":
        fwrite.write(line)

fread.close()
fwrite.close()
    

