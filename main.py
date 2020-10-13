import requests
import json

def makeRequestForJson(currency):
	with open("./apikey.txt") as file:
		for line in file:
			apiKey = line

	url = 'https://v6.exchangerate-api.com/v6/{}/latest/{}'.format(apiKey,currency)
	# Making our request
	response = requests.get(url)
	data = response.json()
	return data['conversion_rates']

def readFromFile():
	d = []
	with open('./data.json') as inf:
		for line in inf:
			d.append(eval(line))
	return d[0]

if __name__ == '__main__':
	b = input("Enter a base currency : ")
	f = input("Enter a final currency : ")
	a = input("Enter an amount : ")
	d = makeRequestForJson(str(b))
	t = float(d[b]) * float(d[f]) * float(a)
	print(t)
