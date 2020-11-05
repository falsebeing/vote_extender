import datetime
from log import *

mode = "state"

# input variables:
state_name = ""
name = ""
trump_votes = 0
biden_votes = 0
percent_reporting = 0

# calculation variables:
current_lead = 0
current_votes = 0
leader = ""

def add_commas(number):
	number_s = str(number)
	limit = len(number_s)
	with_commas = []
	index = 0

	while index < limit:
		with_commas.append(number_s[index])

		if index != 0 and index + 1 != limit and (limit - index - 1) % 3 == 0:
			with_commas.append(',')

		index += 1

	return ''.join(with_commas)

class State:
	def __init__(self, name):
		self.name = name
		self.counties = []
		self.biden = 0
		self.trump = 0
		self.leader = '' 
		self.lead = 0

	def tally(self):
		if len(self.counties) == 1:
			log_result(f"Predictions accounted for in {self.counties[0]} county:")
		elif len(self.counties) > 1:
			log_result(f"Predictions accounted for in {', '.join(self.counties[:-1])}, and {self.counties[-1]} counties:\n")
		if self.biden > self.trump:
			self.leader = "Biden"
			self.lead = self.biden - self.trump
		else :
			self.leader = "Trump"
			self.lead = self.trump - self.biden

		log_result(f"\nExpected vote tally in {self.name} stands as:")
		log_result(f"Biden: {self.biden}")
		log_result(f"Trump: {self.trump}\n")
		log_result(f"{self.leader} leads by {self.lead}\n")

	def add_county(self, county, biden, trump):
		self.counties.append(county)
		self.biden += biden
		self.trump += trump

		log_result(f"Added {county} County to {self.name}")


print("Welcome to the Uncounted Votes Projector\n")
print("This calculator predicts expected vote totals based on the current vote trend, accounting for no other specific variables")
state = None

while True:
	if mode == "state":
		print("\nEnter state name:")
	elif mode == "state_biden":
		print("\nEnter Biden's current votes:")
	elif mode == "state_trump":
		print("\nEnter Trump's current votes")
	elif mode == "menu":
		print('\nEnter "c" to add a new county, "t" to display state-wide tally, or always "q" to quit:')
	elif mode == "name":
		print("Enter county name:")
	elif mode == "bv":
		print("Enter current Biden votes:")
	elif mode == "tv":
		print("Enter current Trump votes:")
	elif mode == "pr":
		print("Enter current percent reporting:")

	elif mode == "calc":
		if biden_votes > trump_votes:
			current_lead = biden_votes - trump_votes
			leader = "Biden"
		else:
			current_lead = trump_votes - biden_votes
			leader = "Trump"


		# method 1: just get expected lead change
		log_result(f"\nResults Report:")
		log_result(f"As of: {timestamp()} in {name} County\n")
		log_result(f"Biden: {biden_votes}\nTrump: {trump_votes}\n{leader} leads by {current_lead}")
		log_result(f"Method 1:\n----------------")


		expected_add = int((current_lead * 100 - current_lead * percent_reporting)/percent_reporting)
		total_expected_lead = current_lead + expected_add
		log_result(f"{leader} is expected extend his lead by {add_commas(expected_add)} votes to a total of {add_commas(total_expected_lead)}\n")

		log_result(f"Method 2:\n----------------")
		# method 2: get expected vote adds for both, compare results
		expected_biden_total = int(biden_votes * 100 / percent_reporting)
		expected_biden_add = expected_biden_total - biden_votes
		expected_trump_total = int(trump_votes * 100 / percent_reporting)
		expected_trump_add = expected_trump_total - trump_votes

		if leader == "Biden":
			expected_add = expected_biden_add - expected_trump_add
		else:
			expected_add = expected_trump_add - expected_biden_add


		log_result(f"Biden is expected to extend his vote count by {add_commas(expected_biden_add)} to a total of {add_commas(expected_biden_total)}")
		log_result(f"Trump is expected to extend his vote count by {add_commas(expected_trump_add)} to a total of {add_commas(expected_trump_total)}\n")

		# refresh with new expected add
		total_expected_lead = current_lead + expected_add

		log_result(f"This would extend {leader}'s lead by {add_commas(expected_add)} to a total of {add_commas(total_expected_lead)}\n")


		# Add county to state
		state.add_county(name, expected_biden_add, expected_trump_add)

		# Log raw data and clear input vars
		log_data(name, trump_votes, biden_votes, expected_biden_total, expected_trump_total, percent_reporting)
		name, biden_votes, trump_votes = '', 0, 0

		mode = "menu"
		continue
	
	entry = input()

	if entry == "q":
		break

	if mode == "state":
		state_name = entry
		state = State(state_name)
		mode = "state_biden"

	elif mode == "state_biden":
		state.biden = int(entry)
		mode = "state_trump"

	elif mode == "state_trump":
		state.trump = int(entry)
		mode = "menu"

	elif mode == "menu":
		if entry == "c":
			mode = "name"
		elif entry == "t":
			state.tally()

	elif mode == "name":
		name = entry
		mode = "bv"

	elif mode == "bv":
		biden_votes = int(entry)
		mode = "tv"

	elif mode == "tv":
		trump_votes = int(entry)
		mode = "pr"

	elif mode == "pr":
		percent_reporting = int(entry)
		mode = "calc"

