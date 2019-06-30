Assignment 

The API key need before start, but I add a default one in case not been set
	export MY_KEY="5394c9bc"
Build it

	docker build -t my-image .

Run it

	docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image 'Toy Story'

Delete container
	docker container prune

Delete images
	docker image rm <image id>


Test Report
----------
$ export MY_KEY="abcd"

$ docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image 'Toy story'

"Toy story" Invalid API key!

$ export MY_KEY="5394c9bc"

$ docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image 'Toy story'

"Toy story" Rotten Tomatoes rating is: 100%

$ docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image 'not Toy story'

"not Toy story" Movie not found!

$ docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image 'Yesterday'
	"Yesterday" don't have 'Rotten Tomatoes' rating, but it has 'Internet Movie Database' value which is: 9.2/10

$ docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image 'Annabelle Comes Home'
	"Annabelle Comes Home" have no Ratings available



