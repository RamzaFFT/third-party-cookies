import json


# ------------------ Functions ------------------ #

def generateQuery(source, target):
	edges = list(default_edges)

	for website in data:
		if website[0] != website[1]:
			if website[0] == source and not website[1] == target:
				edges.append("{};{};Directed;{};{};{}\n".format(website[0], website[1], website[4], website[5], website[6]))
			
	with open('{} | {}.csv'.format(source, target), 'w') as edges_file:
	    edges_file.writelines(edges) # guardar en el csv


def generateSource(source):
	edges = list(default_edges)

	for website in data:
		if website[0] != website[1]:			
			if website[0] == source and not website[5]:
				edges.append("{};{};Directed;{};{}\n".format(website[0], website[1], website[4], website[6]))

	with open('Source: {}.csv'.format(source), 'w') as edges_file:
	    edges_file.writelines(edges) # guardar en el csv


def generateTarget(target):
	edges = list(default_edges)

	for website in data:
		if website[0] != website[1]:
			if website[1] == target and not website[5]:
				edges.append("{};{};Directed;{};{}\n".format(website[0], website[1], website[4], website[6]))

	with open('Target: {}.csv'.format(target), 'w') as edges_file:
	    edges_file.writelines(edges) # guardar en el csv


def generateAll():
	edges = list(default_edges)

	for website in data:
		if website[0] != website[1]: #and not website[5]
			edges.append("{};{};Directed;{};{}\n".format(website[0], website[1], website[4], website[6]))

	with open('All.csv', 'w') as edges_file:
	    edges_file.writelines(edges) # guardar en el csv


# ------------------ Main code ------------------ #

with open('lightbeamDataELP.json', 'r') as data_file:
	data = json.load(data_file)

default_edges = []
default_edges.append("Source;Target;Type;Cookie;Secure\n")


generateAll()


queries = [
	['google.com', 'facebook.com'],
	['facebook.com', 'fbcdn.net',]
]

for query in queries:
	generateQuery(query[0], query[1])


samples = ['google.com', 'google.es', 'facebook.com']

for sample in samples:
	generateSource(sample)
	generateTarget(sample)