import sys

from rbst import *

def did_x_beat_y(x, y):
	'''
	x and y are two teams (integers).
	Returns True if team x beat y, otherwise returns False.
	'''
	assert x != y, f"Teams x = {x} and y = {y} need to be different."
	if x > y:
		return not did_x_beat_y(y, x)
		
	return True if ((((17 + 8321813 * x + 1861 * y) % 1299827) % 2) == 0) else False

def order_teams(n):
	'''
	Returns a dynamic sequence encoded as a RBST onject.
	Team i in the sequence should have beaten team i+1 in the sequence.
	'''

	T = RBST()

	T.insert(1, 1)

	team_1 = T.select(1).data

	count = 1

	# loop from 2 to n + 1
	for x in range(2, n + 1):
		# get the first team
		first_team = T.select(1).data

		# and get the last team
		last_team = T.select(len(T)).data

		if did_x_beat_y(x, first_team):
			T.insert(x, 1)

		elif did_x_beat_y(last_team, x):
			T.insert(x, len(T) + 1)

		else:
			# low boundary, which is just 1 (trees start at 1)
			low_boundary = 1

			# high boundary of T, which is just the end of T
			high_boundary = len(T)

			pos = len(T) + 1

			while (low_boundary <= high_boundary):
				# get the middle
				middle = (low_boundary + high_boundary) // 2

				# get the middle team
				middle_team = T.select(middle).data

				# if team x beat the middle_team
				if did_x_beat_y(x, middle_team):
					pos = middle
					high_boundary = middle - 1

				# otherwise the middle team beats x, place it after middle
				else:
					low_boundary = middle + 1

			T.insert(x, pos)
	return T


	# ------
	

n = 100_000
T = order_teams(n)
# Verifies if the sequence returned is valid.
if T is None or len(T) != n:
	print(f"Size of tree returned by order_teams({n}) is wrong.")
else:
	for i in range(1, len(T)):
		x = T.select(i).data
		y = T.select(i + 1).data
		if not did_x_beat_y(x, y):
			print(f"Invalid sequence: team {x} in position {i} lost to team {y} in position {i+1}.")
			print(did_x_beat_y(x, y), did_x_beat_y(y, x))
			sys.exit(1)

	print("Yay! Tree contains a valid ordering.")

	# Use ordering.inorder() to print the sequence. But realize that N = 100_000, so the ordering will fill your entire screen. Try to set N to something more manageable, like N = 100 and then print it out for testing purposes.



