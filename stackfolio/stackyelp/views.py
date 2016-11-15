from django.shortcuts import render
from stackfolio import yelphelp as yh

def home(request):

	if request.method == "POST":
		token = yh.get_access_token()
		search_term = request.POST['search_term']
		location = request.POST['location']
		results = yh.quick_search(token, search_term, location)

		average_price = yh.average_price(results)
		average_rating = yh.average_rating(results)
		
		image_dict = {}
		for r in results:
			image_dict[r['name']] = r['image_url']


		return render(request, 'stackyelp/home.html', {
				'image_dict':image_dict,
				'average_price':average_price,
				'average_rating':average_rating,
				'search_term':search_term,
				'location':location,
				})

	return render(request, 'stackyelp/home.html')
