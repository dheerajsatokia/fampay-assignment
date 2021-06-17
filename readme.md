# FamPay Assignment

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/dheerajsatokia/fampay-assignment.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Then Migrate the database:

```sh
(env)$ python3 manage.py migrate
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd famPAyYoutubeAssignment
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/admin`.

Default credential for Admin panel is :
`Username - Root`
`Password - Root@123`

or you can create one using.

```sh
(env)$ python manage.py createsuperuser
```


Add an API key in order to use YouTube APIs.
API key can be added from admin dashboard or using API.

## Walkthrough

Before interacting with application we need to add API key. Multiple API key can be added so,
if API limit of one exceeds we can use another.

## Auto Fetch Videos

To fetch the video in async way we need to set up cron tab using:

```sh
(env)$ python manage.py crontab add
```
to check the cron tab :

```sh
(env)$ python manage.py crontab show
```

To remove the cron tab :

```sh
(env)$ python manage.py crontab remove
```


## PostMan collection


`https://www.getpostman.com/collections/496a3e978803df87277c`



