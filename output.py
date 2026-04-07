# write a python program that opens the named output.txt in write mode and writes
# "hello, world!" into it . explain what happens if the file already exist

with open ('output.txt','w' )as file:
    (file.write("Hello world"))