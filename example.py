from csvParsely import parse_csv

if __name__ == "__main__":
	
	# Read test csv file,
	f = open("./sample.csv","r", encoding="utf-8")
	content = f.read()
	f.close()
	
	# Parse it
	data = parse_csv(content)
	
	# For each row,
	for row in data:
		# print(row) # Uncomment to see each row's dictionary printed.
		name = row['name']
		print(f'{row["name"]}: {row["quote"]}')