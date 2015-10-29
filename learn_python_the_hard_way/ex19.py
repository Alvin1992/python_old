def cheese_and_crackers(cheese_count, box_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d crackers!" % box_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

print "We can just give the function numbers directly."
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
amount_cheese = 10
amount_crackers = 50

cheese_and_crackers(amount_cheese, amount_crackers)

print "We can even do math inside:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_cheese+100, amount_crackers+1000)