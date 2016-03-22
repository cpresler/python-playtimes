# Goal 1:
bread = 10
peanut_butter = 6
jelly = 3
sandwiches = bread/2
sandwich = 0


if(sandwiches > jelly and jelly <= peanut_butter):
	sandwiches = jelly
elif(sandwiches > peanut_butter and peanut_butter <= jelly):
	sandwiches = peanut_butter
elif(sandwiches == 0):
	print "Blarg, I've got no lunch!"


if(sandwiches > 0):
	while sandwiches > 0:
		sandwich += 1
		print 'Making sandwich #{0}'.format(sandwich)
		sandwiches -= 1
		# Goal 2:
		rem_bread = bread/2 - sandwich
		rem_jelly = jelly - sandwich
		rem_pb = peanut_butter - sandwich
		if(rem_bread > 0 and rem_pb > 0 and rem_jelly > 0):
			print 'I have enough bread for {0} more sandwiches, enough peanut butter for {1} more, and enough jelly for {2} more.'.format(rem_bread, rem_pb, rem_jelly)
		elif(rem_bread == 0):
			print "All done; I ran out of bread"
		elif(rem_jelly == 0):
			print "All done; I ran out of jelly"
		elif(rem_pb == 0):
			print "All done; I ran out of peanut butter"
		else:
			print "Error, something weird happened."
else:
	print "Oh no, I'm missing peanut butter or jelly"

