
for bottles in range(99, -1, -1):
	if(bottles > 1):
		print '{0} bottles of beer on the wall, {0} bottles of beer ...'.format(bottles)
		print 'If one of those bottles should happen to fall, {0} bottles of beer on the wall'.format(bottles - 1)