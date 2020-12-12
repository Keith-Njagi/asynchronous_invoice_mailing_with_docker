This is a sample asynchronous invoice mailing python app that uses celery and redis backend to carry out asynchronous mailing.
As the focus wasn't on making a python backend but on the asynchronous program, you will need to have a database with a sample *username* and *email*.

The asynchronous program uses [celery](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html) and _redis_ as its backend.

## To start the server

- docker-compose build

Then:

- docker-compose up

Or run it in just one line 

- docker-compose up --build

### Requirements

You will need to have _docker_ and _docker compose_ installed.

Also generate your own *config.env* file in the _mailing_ folder.

