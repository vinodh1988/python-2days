import os

file_name = "d:/flask.pdf"

file_stats = os.stat(file_name)

print(file_stats)
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')


file = open("d:/flask.pdf", "rb")  
file2 = open("d:/flaskcopy.pdf",'wb')
x=0;
while x<file_stats.st_size:
    file.seek(x)
    file_bytes=file.read(1000)
    file2.write(file_bytes)
    x =x+1000

file2.close()