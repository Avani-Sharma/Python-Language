# append mode: into the append mode we basically add new lines or write new lines into the file without 
# overwriting the content.
file = open('write.txt', 'a')
file.write('\nthis is forth line into the file\n')
file.close