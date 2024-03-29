from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline(),  # 如果没有这个逗号，每个都会有两个\n
	# The readline() function returns the \n that's in the file at the end of that line.
	# Add a , at the end of your print function calls to avoid adding double \n to every line.

current_file = open(input_file)

print "First, let's print the whole file. \n"
print_all(current_file);

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines."
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)