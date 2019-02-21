import util

#TODO: Timing issues are actually control flags!

#main data
data = util.Samus()


for animation_number in range(len(data.animations)):
	if data.animations[animation_number].used:
		try:
			data.animations[animation_number].gif(f"images/test{hex(animation_number)}.gif", data.palettes['standard'],zoom=2)
		except AssertionError as e:
			print(f"AssertionError on animation {hex(animation_number)}: {e.args}")