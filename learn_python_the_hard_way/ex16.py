from sys import argv

script, filename = argv

print "We'r going to erase %r." % filename
print "If you don't want that, hit control-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, "w")

print "Truncating the file. Goodbye!"
target.truncate() #open mode dosen't need this command

print "Now I'm going to ask you three lines."
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."
# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "Finally, we close it."
target.close()