import requests
import secrets
import math

from PIL import Image
from StringIO import StringIO

def get_access_token():
	"""
	Make a POST call to https://api.yelp.com/oauth2/token with the client ID and
	secret key, then get the access token from the response body
	"""
	data = {
		'grant_type': 'client_credentials',
		'client_id': secrets.YELP_APP_ID,
		'client_secret': secrets.YELP_SECRET
	}
	r = requests.post('https://api.yelp.com/oauth2/token', data=data)
	return r.json()['access_token']

def quick_search(access_token, search_term, location):
	"""
	API Endpoint documentation: https://www.yelp.com/developers/documentation/v3/business_search
	The interesting bit here is construction the Authorization HTTP header using our access_token

	Returns a JSON object full of up to 50 businesses
	"""
	endpoint_url = 'https://api.yelp.com/v3/businesses/search?term={}&location={}&limit=50'.format(search_term, location)
	headers = {"Authorization": "bearer " + access_token}
	return requests.get(endpoint_url, headers=headers).json()['businesses']

def average_price(business_list):
	"""
	Yelp indicates the "price" of a business with a series of $ characters. $ is cheapest, $$$$ is most expensive.
	Some businesses may not have a price, so we can't assume there will always be something there!
	"""
	prices = []
	try:
		for b in business_list:
			prices.append(len(b['price']))
	except KeyError:
		pass

	avg_float = float(sum(prices))/float(len(prices))
	#ceiling function to "round" the float
	return math.ceil(avg_float*100)/100

def average_rating(business_list):
	"""
	Yelp lets reviewers rate a business on a 1-5 scale. We use a try-catch block in case we encounter an unrated business,
	and a ceiling function to round off the average.
	"""
	ratings = []
	try:
		for b in business_list:
			ratings.append(b['rating'])
	except KeyError:
		pass

	avg_float = float(sum(ratings)) / float(len(ratings))
	return math.ceil(avg_float*100)/100