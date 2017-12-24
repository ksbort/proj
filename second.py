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
print('\n\"Just how long have i been unconscious for?...\"')
two()
print('\n[You look around again, trying to find an answer to the many questions on your mind]')
one() #Overflow on above line on 80 long screens