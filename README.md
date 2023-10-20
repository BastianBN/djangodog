### Django Dogs project

Implementation of the exercise [CYBR8470](https://mlhale.github.io/CYBR8470/modules/building-a-server/django-exercise.html)

Available API endpoints and methods managing them :
- `/api/dogs/` is handled by `DogList` and provides access to a list of the dogs existing in the database.
- `/api/dogs/[id]`is handled by `DogDetail` and provides access to all the information about a particular dog, defined by its id.
- `/api/breeds/` is handled by `BreedList` and provides access to the list of breeds existing in the database and is a ForeignKey of `Dogs`.
- `/api/breeds/[id]` is handled by `BreedDetail` and provides access to all the information about a particular breed, defined by its id.