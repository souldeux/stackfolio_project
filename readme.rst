#Stackfolio Four-Hour Project

This project was developed in four hours as part of a technical interview with Stackfolio.

This single-app Django project interacts with the Yelp search API to find and display businesses based on user-supplied
criteria (a "search term" and a location string).

The app uses a GET form in order to create a REST-ful interface - a POST-based search form would lose the querystrings in the
URL and make it more difficult for users to share interesting results with one another.

Styling is done via basic bootstrap with tweaks applied. The masonry layout of the search results uses the masonry library from http://masonry.desandro.com/. Hover effects over search results courtesy of https://miketricking.github.io/dist/. 