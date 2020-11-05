import datetime

mode = "menu"

# input variables:
name = ""
trump_votes = 0
biden_votes = 0
percent_reporting = 0

# calculation variables:
current_lead = 0
leader = ""

print("Welcome to the Uncounted Votes Projector\n")
print("This calculator predicts expected vote totals based on current preference trend")

while True:
	if mode == "menu":
		print('Enter "c" to calculate, or always "q" to quit\n')
	elif mode == "name":
		print("Enter county name:")
	elif mode == "tv":
		print("Enter current Trump votes:")
	elif mode == "bv":
		print("Enter current Biden votes:")
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
		print(f"As of: {datetime.datetime.now()} in {name} County")
		print(f"Method 1:\n----------------\n")


		expected_add = int((current_lead * 100 - current_lead * percent_reporting)/percent_reporting)
		print(f"{leader} is expected extend his lead by {expected_add} votes")

		print(f"Method 2:\n----------------\n")
		# method 2: get expected vote adds for both, compare results
		expected_biden_total = int(biden_votes * 100 / percent_reporting)
		expected_biden_add = expected_biden_total - biden_votes
		expected_trump_total = int(trump_votes * 100 / percent_reporting)
		expected_trump_add = expected_trump_total - trump_votes


		print(f"Biden is expected to extend his vote count of {biden_votes} by {expected_biden_add} to a total of {expected_biden_total}")
		print(f"Trump is expected to extend his vote count of {trump_votes} by {expected_trump_add} to a total of {expected_trump_total}")
		if leader == "Biden":
			print(f"This will extend Biden's lead by {expected_biden_add - expected_trump_add}")
		else:
			print(f"This will extend Trump's lead by {expected_trump_add - expected_biden_add}")

		mode = "menu"
		continue
	
	entry = input()

	if mode == "menu":
		if entry == "c":
			mode = "name"

	elif mode == "name":
		name = entry
		mode = "tv"

	elif mode == "tv":
		trump_votes = int(entry)
		mode = "bv"

	elif mode == "bv":
		biden_votes = int(entry)
		mode = "pr"

	elif mode == "pr":
		percent_reporting = int(entry)
		mode = "calc"

	if entry == "q":
		break
