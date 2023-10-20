# Django Dogs project

This project implements the exercise [CYBR8470](https://mlhale.github.io/CYBR8470/modules/building-a-server/django-exercise.html) from [@MLHale](https://github.com/MLHale)

Available API endpoints and their corresponding methods for managing them are as follows :
- `/api/dogs/` is handled by `DogList` and provides access to a list of the dogs existing in the database.
- `/api/dogs/[id]`is handled by `DogDetail` and provides access to all the information about a particular dog, defined by its `id`.
- `/api/breeds/` is handled by `BreedList` and provides access to the list of breeds existing in the database and is a ForeignKey of `Dogs`.
- `/api/breeds/[id]` is handled by `BreedDetail` and provides access to all the information about a particular breed, defined by its `id`.

This project served as a valuable way to learn **Django** and **Django Rest Framework** through practical implementation and to understand best practices for creating a backend.

### Requirements :
This projects requires `django` and the `djangorestframework`.
One can install the environment used to run this project by using `pip install -r requirements.txt`

### TODO :
- Add a frontend in Vue.js to process data and learn how to establish the connection between the backend and frontend in a full-stack project.
- Consider adding additional functionalities to the backend.
