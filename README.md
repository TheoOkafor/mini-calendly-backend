# mini-calendly-backend
The Django-based backend of the mini version of calendly
## About
This backend has 3 models `user` (which I use to store the mentors' and users' information), `openings` (which I shall use to store the openings that the mentor has made available), and `bookings` (which I use to store the openings that the user booked).
#### API routes
1. http://127.0.0.1:8000/api/user - Create user
2. http://127.0.0.1:8000/api/mentor/1/bookings - Create bookings
3. http://127.0.0.1:8000/api/mentor/1 - Get mentor/user

#### Known Improvement Areas
1. In the booking endpoint, I do not check whether an opening has been made available by the mentor. Also, I do not check whether the opening has been booked.
2. Add an endpoint for creating openings.
3. 

## Getting Started

Clone this [repo](https://github.com/TheoOkafor/mini-calendly-backend.git)

```bash
git clone https://github.com/TheoOkafor/mini-calendly-backend.git
```
#### Requirements
You need Python 3.7.2 and above to run this app. Start by installing it (if you do not have it installed already).


#### Virtual Environment
Setup virtualenv in your workspace before you run any of the following commands. ([A nice GitHub gist on using virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b))

#### Dependencies
To install the dependencies run
```venv
pip3 install -r requirements.txt
```

### Migration
If you have everything set up correctly, run migrations

```venv
python3 manage.py migrate
```

### Seeding the Database
```venv
python3 manage.py loaddata user
python3 manage.py loaddata openings
python3 manage.py loaddata bookings
```

### Running the app
To run the app
```venv
python3 manage.py runserver
```

### Testing on Postman
To test some of the endpoints on Postman, use
[mini-calendly Postman Collection](https://www.getpostman.com/collections/b05bfdae2f28def0f08a)

### Running tests
To run test
```venv
python3 manage.py test
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT