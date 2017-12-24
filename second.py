import time
#one after dialogue and two after speech
def one():
	time.sleep(1)
def two():
	time.sleep(2)
#Delimiter
print('\n------------------------')
time.sleep(.1)
print('\n*DING DONG DING DONG*')
one()
print('\n\"..........\"')
two()
print('\n\"uuuuurrrrrrrrrggg....\"')
two()
print('\n[You wake up from the sound of an alarm bell.]')
one()
print('\n[You look around and find yourself in a dark room.]')
one()
print('\n\"Where am I? What is this place? What am I doing here?\"')
two()
print('\n[You feel your limbs bound by leather to the bed that you are lying on...')
one()
print('\n...and an IV tube sticking out from your left hand.]')
two() #impact
print('\n[You struggle a little and manage to free yourself from the worn out straps.]')
one()
print('\n\"Just how long have I been unconscious for?...\"')
two()
print('\n[You look around again, trying to find an answer to the many questions on your mind]')
one() #Overflow on above line on 80 long screens
print('\n[On a table to your left you find a document]')
one()
def fstch():
	print('\nPress E to pick up.')
	first = str(input('Input: '))
	if(first == 'e'):
		print('\n.....')
		one()
		print('\nIt says...')
		one()
		print('\nNAME: KongRJ')#change name
		time.sleep(.5)
		print('AGE: 16')
		time.sleep(.5)
		print('DOCTOR IN CHARGE: Dr Nat')
		time.sleep(.5)
		print('NOTES: Patient still shows no signs of waking after ingesting no. 3796...')
		time.sleep(.5)
		print('\t...been 15 days since then. Drug classified as a failure...')
		time.sleep(.5)
		print('\t...Patient\'s vital signs are stable. High probability patient...')
		time.sleep(.5)
		print('\t...will be able to take more drugs upon awakening. Patient will be...')
		time.sleep(.5)
		print('\tleft alone until then.')
		two()
		def secch():
			print('\nPress E to place it back.')
			first = str(input('Input: '))
			if(first == 'e'):
				print('\n.....')
				one()
				from corridor import cont
				cont()
			else:
				print('\nInput failed.')
				secch()
		secch()
	else:
		print('Input failed.')
		fstch()
fstch()