# DjangoPiGPIO
Django PiGPIO is an easy way to program your Raspberry Pi's GPIO 
pins from a modern webinterface.

Googles excellent [Blockly](https://developers.google.com/blockly/) library is used to
create programs to allow everyone to get up and running quickly.

<u>Features</u>
- Super easy and fast to install using [Docker](https://www.docker.com/) and 
[Docker Compose](https://docs.docker.com/compose/)
- Highly customizable programming environment
- Modern Webinterface based on python django

## Installation
1. Clone this repository at your desired install location
2. Initialize submodules with `git submodule update --init --recursive`
3. Copy `.env.template` to `.env` and fill in every variable accordingly
4. Start the docker container using `docker-compose up -d`
5. Run `update.sh` script to create your database and collect static files
6. To create a user execute into the docker container (`docker-compose run web_pigpio python3 sh`) and run `manage.py createsuperuser`


### Manual Installation
To install PiGPIO without docker please refer to any generalizes installation tutorial for Django
applications. Make sure to **edit `settings.py`** or set the environment variables manually.  

To install all the packages you need run `pip install -r requirements.txt`

Use `manage.py migrate` and `manage.py collectstatic` to setup your database and collect the static files.

## Updating
If you are using Docker simply pull the latest code, start the container and run `update.sh`.

If not its basically the same but you need to run `migrate` and `collectstatic` manually and you
might have problems if you modified `settings.py`.

## Contributing
Feel free to [report bugs]() or create pull requests if you fix or improve something.

Dont forget to set the environment variables when working locally (and not using docker). 
The following environment variables are sufficient and recommended for development
```
DEBUG=1
ALLOWED_HOSTS=*
SECRET_KEY=<some random key>
DB_ENGINE=django.db.backends.sqlite3
POSTGRES_HOST=db.sqlite3
```

## License
Most of the Code in this repository is licensed under the MIT License which basically allows you to do whatever you want.
Click [here](https://github.com/vabene1111/Django-PiGPIO/blob/master/LICENSE.md) to see some actually useful information 
about what you can and cannot do.

Additionally the [Blockly](https://developers.google.com/blockly/) library by Google is used to create the programs. It is licensed under
the `Apache License 2.0` which also basically allows everything. For more details please
refer to [the original license](https://github.com/google/blockly/blob/master/LICENSE)