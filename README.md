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
- Usable without internet access (trough ad-hoc WiFi network or wired connection)

## Intended use
This program is designed to allow for easy and on the fly programming of a raspberry pi.
Although it supports having multiple users it is not intended to be used by multiple users at the
same time (this is mainly because one Pi only has one set of GPIO pins).

PiGPIO is designed to work offline with the raspberry being accessed either via an ad-hoc WiFi network 
or a wired connection. For this reason all resources (CSS, JS, ...) are included in this repository.

PiGPIO was not designed with a focus on security. Even though Django is pretty secure by default
there are several places where an attacker could compromise the security of the PiGPIO app. This is 
no problem if used in local environment, should you plan to use this on a public network consider 
using a firewall.

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

1. Clone the repository and init the submodules `git submodule update --init --recursive`
2. Dont forget to set the environment variables when working locally (and not using docker). In PyCharm this can be done in the run configuration.
    The following environment variables are sufficient and recommended for development
    ```
    DEBUG=1
    ALLOWED_HOSTS=*
    SECRET_KEY=<some random key>
    DB_ENGINE=django.db.backends.sqlite3
    POSTGRES_DB=db.sqlite3
    ```

3. When working on a machine that does not have the GPIO python library installed (basically anything but the pi itself)
   it might be useful to install the [RPi.GPIO-def package](https://github.com/Def4l71diot/RPi.GPIO-def) to prevent errors.
   Do note that this package just makes the interpreter think you have the required library's, no code is
   actually executed.
4. Install requirements `pip install -r requirements.txt` (or with PyCharm open `requirements.txt` and click on banner)
5. Setup database with `manage.py migrate`.
   > NOTE: You need to either set the environment variables globally or when using PyCharm set them under `Settings | Languages and Frameworks | Django`


## License
Most of the Code in this repository is licensed under the MIT License which basically allows you to do whatever you want.
Click [here](https://github.com/vabene1111/Django-PiGPIO/blob/master/LICENSE.md) to see some actually useful information 
about what you can and cannot do.

Additionally the [Blockly](https://developers.google.com/blockly/) library by Google is used to create the programs. It is licensed under
the `Apache License 2.0` which also basically allows everything. For more details please
refer to [the original license](https://github.com/google/blockly/blob/master/LICENSE)