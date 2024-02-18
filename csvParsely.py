"""
	# CSV Parsing Library
	Version 1.0
	By Joseph M. Juma
	
	## Description
	A very simple implementation of comma seperated value (csv) text parsing. 
	This produces a "data-table": a list of rows where each value has a key 
	based on the header row of the csv. This automatic keying nature is the 
	benefit of using this library over the standard csv library provided by 
	Python.
	
	## Copyright
	Copyright Joseph M. Juma, 2024. All rights reserved.
"""


def parse_delimited_string(value, opening_delimiter = '"', closing_delimiter = '"'):
	"""
		Handles the parsing of a string with delimiters, most often quotes.
		Incidentally, this is currently unused.
	"""
	
	# Find the opening delimiter
	i = value.find(opening_delimiter)
	
	# If that delimiter wasn't found, error - return none.
	if(i == -1):
		return None
	
	# Else, if it was found,
	else:
		# For each character in the string after the first,
		for j in range(i,len(value) - 1):
			# If you find a '\' then the next character is skipped,
			if value[j] == '\\':
				j += 1
			# Else, if you find a closing delimiter,
			elif value[j] == closing_delimiter:
				# Return the substring between open and close
				return value[i:j]
	
	# Finally, if you got this far, malformed string - return None.
	return None

def clean_line_endings(content):
	'''
		Turns windows \r\n line-endings into the more universal \n, by removing 
		the \r.
	'''
	return content.replace("\r","")
	
def split_lines(content):
	'''
		Given a multi-line string, splits into a list where each entry is one 
		line.
	'''
	
	# Clean line endings
	content = clean_line_endings(content)
	
	# Split on line endings
	return content.split("\n")

def parse_csv_line(line):
	'''
		Parses a single comma seperated value (csv) line of text into a 
		list of ordered values.
	'''
	
	# Allocate some variables,
	data = []
	value = ""
	inQuotes = False
	skipNext = False
	
	# For each character in the line,
	for ch in line:
		if skipNext == True:
			skipNext = False
			value += ch
			continue
		
		if ch == '\\':
			skipNext = True
		elif ch == '"':
			inQuotes = not inQuotes
			value += ch
		elif ch == ',' and not inQuotes:
			data.append(strip_leading_whitespace(value))
			value = ""
		else:
			value += ch
	
	# Append the remaining data,
	if len(value) != 0:
		data.append(strip_leading_whitespace(value))
	
	# Return the data list,
	return data
	
def dict_from_key_value_lists(keys, values):
	'''
		Creates a dictionary from two lists of ordered keys and values where 
		the n-th value has the n-th key in the dictionary.
	'''
	
	# If there's a length mismatch, error - return an empty dictionary, 
	if len(keys) != len(values):
		print("[ERROR] in dict_from_key_value_lists(): Length mismatch between keys and values lists.")
		return None
	
	# Else, if no length mismatch,
	else:
		# Build the dictionary and return it
		data = {}
		for i in range(0,len(keys)):
			data[keys[i]] = values[i]
		return data
	
	# If we reached here, error - return None.
	print("[ERROR] in dict_from_key_value_lists(): An unexpected error occured.")
	return None

def strip_leading_whitespace(value):
	'''
		Removes whitespace up to the start of non-whitespace characters in a 
		string.
	'''
	for i in range(0,len(value)):
		if value[i] == ' ':
			continue
		else:
			return value[i:]
	
def parse_csv(content):
	'''
		Parses a multi-line csv formatted string, into a list of dictionaries 
		with the key-value schema based on the first row in the text.
	'''
	# Split content into lines
	lines = split_lines(content)
	
	# Get the first row so we can figure out the header,
	header_keys = parse_csv_line(lines[0])
	
	# Create the data variable,
	data = []
	
	# For each remaining line of text,
	for line in lines[1:]:
		values = {}
		line_values = parse_csv_line(line)
		row = dict_from_key_value_lists(header_keys, line_values)
		data.append(row)
	
	# Return the data table!
	return data
	
def parse_csv_file(filepath):
	'''
		Loads a CSV file from on-disk, then parses it into a data table.
	'''
	
	f = open(filepath, "r", encoding="utf-8")
	data = f.read()
	f.close()
	
	return parse_csv(data)