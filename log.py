# write a pyhton program that opens a file name log.txt in append mode and add
# the new line " new entry added". explain wether the exisiting content is affected

with open('log.txt','a') as file:
    print (file.write("\nnew thing added"))