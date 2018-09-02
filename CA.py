# Cellular Automata
# by JX

import time # Delay

def main():
	# Find rule
	ruleBin = findRule()
	
	# Run
	runAutomaton(ruleBin)

# Ask rule from user
def findRule():
	# Compile rules
	rules = range(256)
	
	# Change rules to string to match user input
	for r in rules: # This works since rules is a range itself
		rules[r] = str(r)
	
	# Ask player for rule
	rule = ""
	
	while rule not in rules:
		rule = raw_input("Enter rule (0-255): ")
	
	# Convert rule to binary
	ruleBin = bin(int(rule))[2 : ]
	
	# Add leading 0s
	ruleBin = "0" * (8 - len(ruleBin)) + ruleBin
	
	return ruleBin

# Run program
def runAutomaton(rule):
	# Constant - length of grid
	LENGTH = 151
	
	# Constant - delay after making a row
	DELAY = 0.1
	
	# Create first row
	row = [" "] * LENGTH
	row[int(round(LENGTH * 0.5))] = "0"
	
	# Create new rule with " " and "0" instead of "0" and "1"
	newRule = []
	
	for char in rule:
		if char == "0":
			newRule.append(" ")
		
		else:
			newRule.append("0")
	
	# 8 possible 3-character strings
	ruleSet = {"000": newRule[0],
			   "00 ": newRule[1],
			   "0 0": newRule[2],
			   "0  ": newRule[3],
			   " 00": newRule[4],
			   " 0 ": newRule[5],
			   "  0": newRule[6],
			   "   ": newRule[7]}
	
	# Repeatedly print and create row
	while True:
		# Create row string
		rowStr = ""
		
		for space in row:
			rowStr += space
		
		# Print row string
		print(rowStr)
		
		# Create new row
		newRow = []
		
		# First element of new row
		newRow.append(ruleSet[" " + rowStr[ : 2]])
		
		# Second to second-to-last element of new row
		for space in range(1, len(row) - 1):
			newRow.append(ruleSet[rowStr[space - 1 : space + 2]])
		
		# Last element of new row
		newRow.append(ruleSet[rowStr[len(row) - 3 : ]])
		
		# Set row
		row = newRow
		
		# Delay
		time.sleep(DELAY)

if __name__ == "__main__":
	main()
