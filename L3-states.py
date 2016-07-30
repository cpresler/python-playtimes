# Challenge 1:

with open('L3-files/states.txt', 'r') as states_file:
	# format data
	states = states_file.read()
	states = states.split('\n')
	for state in range(len(states)):
		states[state] = states[state].split('\t')
	# print states

	# create select element
	select_el =  '<select>\n'
	select_el = select_el + '<option value="">Select State</option>\n'
	for state in range(len(states)):
		select_el = select_el + '<option value="{0}">{1}</option>\n'.format(states[state][0],states[state][1])
	select_el = select_el + '</select>'
	# print select_el

# Challenge 2:
	with open('L3-files/states.html', 'w') as s_html_file:
		s_html_file.write(select_el)

# Challenge 3:
import csv # makes converting csv to a dictionary easy

s_info_file = csv.DictReader(open('L3-files/state_info.csv'))
states_info = []

for row in s_info_file:
	states_info.append(row)
# print states_info

for state in range(len(states_info)):
	state = states_info[state]
	print state
	# table = '<table border="1">\n<tr>\n<td colspan="2"> {0} </td>\n</tr>\n<tr>\n<td> Rank: {1} </td>\n<td> Percent: {2} </td>\n</tr>\n<tr>\n<td> US House Members: {3} </td>\n<td> Population: {4} </td>\n</tr>\n</table>'.format(states_info[state]['State'], )
