This is a sample asynchronous invoice mailing python app that uses celery and redis backend to carry out asynchronous mailing.
As the focus wasn't on making a python backend but on the asynchronous program, you will need to have a database with a sample *username* and *email*.

The asynchronous program uses [celery](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html) and _redis_ as its backend and Nginx as the reverse proxy.

## To start the server

- docker-compose build

Then:

- docker-compose up

Or run it in just one line 

- docker-compose up --build

### Requirements

You will need to have _docker_ and _docker compose_ installed.

Also generate your own *config.env* file in the _mailing_ folder.

### Routes

You can verify everything runs correctly at your home route: [http://127.0.0.1](http://127.0.0.1)

Now initiate your invoice mailing at [http://127.0.0.1/my_username]()

You can now also access it via your wifi network. Just replace _127.0.0.1_ with your ip address within the wifi network.

If you can manage port fowarding to your internet router, then it is possible to view it from the outside world.