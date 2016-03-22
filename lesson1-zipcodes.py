studybuddy_1 = 'Alison McCauley, 1234 County Line Road, Skaneateles, NY 13152'
studybuddy_2 = 'Dee Cater, 555 Bradford Pkwy, Syracuse, NY 13224'
studybuddy_3 = 'Andrea Bianchi, 987 South St, Jamesville, NY 13078'
studybuddy_4 = 'Kristen Link Logan, 264 Craig Street, Syracuse, NY 13211'
studybuddy_5 = 'Nina Verity, 111 Bridge St, Solvey, NY 13209'


# Goal 1:
zip1 = studybuddy_1[-5:]
zip2 = studybuddy_2[-5:]
zip3 = studybuddy_3[-5:]
zip4 = studybuddy_4[-5:]
zip5 = studybuddy_5[-5:]

print zip1
print zip2
print zip3
print zip4
print zip5

# Goal 2:
print "People are from these zip codes: {0}, {1}, {2}, {3}, {4}".format(zip1, zip2, zip3, zip4, zip5)

# Goal 3:
name1 = studybuddy_1[:studybuddy_1.find(' ')]
name2 = studybuddy_2[:studybuddy_2.find(' ')]
name3 = studybuddy_3[:studybuddy_3.find(' ')]
name4 = studybuddy_4[:studybuddy_4.find(' ')]
name5 = studybuddy_5[:studybuddy_5.find(' ')]

print "{0} can be found in zipcode {1}".format(name1,zip1)
print "{0} can be found in zipcode {1}".format(name2,zip2)
print "{0} can be found in zipcode {1}".format(name3,zip3)
print "{0} can be found in zipcode {1}".format(name4,zip4)
print "{0} can be found in zipcode {1}".format(name5,zip5)