#!/usr/bin/env python

# The input tells us which bots have which microchips initially with lines such
# as:
#	value x goes to bot y
#
# Each bot has instructions telling it what to do with its chips. If a bot has
# two chips it proceeds to execute its instructions. The instructions are of
# the form:
#	bot x gives low to bot 0 and high to output 0
#
# The bot makes a comparison of the two values on its two chips, and gives each
# chip either to another bot or an output bin.

class Bot(object):
	def __init__(self, i):
		self.i = i
		self.low = None
		self.low_to_output = None
		self.high = None
		self.high_to_output = None
		self.chips = []

# bots[i] is the bot with id 'i'
bots = [Bot(i) for i in xrange(210)] # There are 210 bots

output = [None for _ in xrange(21)]

def read(line):
	words = line.split()

	if words[0]=="value":
		bot = int(words[-1])
		value = int(words[1])
		bots[bot].chips.append(value)

	elif words[0]=="bot":
		bot = int(words[1])
		loc_low = int(words[6])
		loc_high = int(words[-1])

		bots[bot].low = loc_low
		bots[bot].high = loc_high

		if words[5]!="bot":
			bots[bot].low_to_output = True

		if words[-2]!="bot":
			bots[bot].high_to_output = True

def get_input():
	while True:
		try:
			yield raw_input()
		except EOFError:
			return

def find_starter(bots):
	for bot in bots:
		if len(bot.chips)==2:
			return bot

def proceed(bot):
	# Part 1) find bot which compares chips 61 and 17
	if 17 in bot.chips and 61 in bot.chips:
		print "FOUND IT",bot.i

	if bot.low_to_output:
		output[bot.low] = min(bot.chips)
	else:
		bots[bot.low].chips.append(min(bot.chips))

	if bot.high_to_output:
		output[bot.high] = max(bot.chips)
	else:
		bots[bot.high].chips.append(max(bot.chips))

	bot.chips = []
	for consider in [bot.low, bot.high]:
		if len(bots[consider].chips) == 2:
			return bots[consider]

if __name__=="__main__":
	map(read, get_input())

	starter = find_starter(bots)

	while starter is not None:
		while starter is not None:
			starter = proceed(starter)

		starter = find_starter(bots)

	print output

	# Part 2) product of first three outputs
	r = 1
	for x in output[:3]:
		r *= x
	print r
