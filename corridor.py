#everything below def should be indented as whole thing is imported
#usual timing rules apply
def cont():
	import time
	def one():
		time.sleep(1)
	def two():
		time.sleep(2)
	print('\n\"So it appears I am in some sort of clinic or hospital...')
	one()
	print('\n...and my name is...\"')
	two()
	print('\n[As you look up you see a long shadow moving through the hallway]')
	one()
	print('\n"Hello, is someone there?\"')
	two()
	print('\n[You walk up to the door and open it slowly]')
	one()
	print('\n[You come across a corridor]')
	one()
	print('\n\"Judging from the angle of the shadow, the person was on the left.\"')
	two()
	print('\n\"Should I go look for or avoid the person?\"')
	two()
	def thrch():
		print('Press A to go left, press D to go right.')
		second = str(input('Input: '))
		if(second == 'a'):
			print('\n.....')
			one()
			from left import con
			con()
		elif(second == 'd'):
			print('\n.....')
			from right import con
			con()
		else:
			print('\nInput failed.')
			thrch()
	thrch()