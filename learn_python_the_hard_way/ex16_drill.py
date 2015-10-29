from sys import argv

script, filename = argv

print "Now I'm going to open %r." % filename

f = open(filename)

print "Now I'll tell you the content in the fiel"

x = f.read()

print x;

print "Now close the file"

f.close()