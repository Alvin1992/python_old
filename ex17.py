from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Coping from %s to %s." % (from_file, to_file)

# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)

print "Hit RETURN to continue and CTRL-C to abort"

raw_input()

out_file = open(to_file, "w")
out_file.write(indata)

print "Alright, all done"
out_file.close()
# in_file.close()


# echo "This is a test file." > test.txt
# 将后面的参数给test.file，如果文件不存在将会创建这个文件。