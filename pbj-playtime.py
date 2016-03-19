peanut_butter = 0
jelly = 5
bread = 3
sandwiches = bread/2
pb_sandwiches = 0
half_sandwich = False
buy_bread = 0
buy_jelly = 0
buy_pb = 0
pbjs = 0

if peanut_butter >= 1 and jelly >= 1 and bread >= 2:
	## How many sandwiches?
	if sandwiches > peanut_butter or sandwiches > jelly:
		sandwiches = jelly if (peanut_butter >= jelly) else peanut_butter
	
	## Open sandwiches?
	if peanut_butter%2 == 1 and jelly%2 == 1 and bread%2 == 1:
			half_sandwich = True

	rem_bread = bread/2 - sandwiches	
	rem_pb = peanut_butter - sandwiches	
	if peanut_butter > jelly and rem_bread > 0 and rem_pb > 0:
		pb_sandwiches = rem_pb if rem_bread >= rem_pb else rem_bread

	## Adjust the grammar
	s = "sandwiches" if (sandwiches > 1) else "sandwich"
	pb_s = "sandwiches" if (pb_sandwiches > 1) else "sandwich"
	if(pb_sandwiches > 0):
		if(half_sandwich):
			print "I can make {0} peanut butter and jelly {1}, {2} peanut butter {3}, and 1 open sandwich".format(sandwiches, s, pb_sandwiches, pb_s)
		else:
			print "I can make {0} peanut butter and jelly {1} and {2} peanut butter {3}".format(sandwiches, s, pb_sandwiches, pb_s)
	else:
		if(half_sandwich):		
			print "I can make {0} peanut butter and jelly {1} and 1 open sandwich.".format(sandwiches, s)
		else:
			print "I can make {0} peanut butter and jelly {1}".format(sandwiches, s)

elif(jelly == 0 and sandwiches > 0 and peanut_butter > 0):
	## PB Sandwiches
		pb_sandwiches = peanut_butter if sandwiches > peanut_butter else sandwiches
		pb_s = "sandwiches" if (pb_sandwiches > 1) else "sandwich"
		print "I can make {0} peanut butter {1}".format(pb_sandwiches, pb_s)

else:
	## Max sandwiches to make
	if(peanut_butter >= jelly):
		pbjs = peanut_butter if peanut_butter > sandwiches else sandwiches
	elif(peanut_butter >= sandwiches):
		pbjs = peanut_butter if peanut_butter > jelly else jelly
	else:
		if(jelly >= sandwiches):
			pbjs = jelly
		else:
			pbjs = sandwiches
	## What to buy
	if(jelly < pbjs):
		buy_jelly = pbjs - jelly
	if(peanut_butter < pbjs):
		buy_pb = pbjs - peanut_butter
	if(sandwiches < pbjs):
		buy_bread = (pbjs * 2) - bread

	## Grocery List:
	print "Grocery List:"
	if(buy_bread > 0):
		print "{0} slice(s) of bread".format(buy_bread)
	if(buy_jelly > 0):
		print "{0} Jelly".format(buy_jelly)
	if(buy_pb > 0):
		print "{0} peanut butter".format(buy_pb)

