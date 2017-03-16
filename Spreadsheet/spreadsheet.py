from urllib import request


def spreadsheet(url):
	response  = request.urlopen(url)
	csv  = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\n")
	dist = "goo.csv"
	fw = open(dist,"w")
	for line in lines:
		fw.write(line+ " \n")
	fw.close()

print("Enter the Url")

url = input()

print("Downloading")
spreadsheet(url)
