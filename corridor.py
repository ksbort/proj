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
