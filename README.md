# DjangoPiGPIO
Django PiGPIO is an easy way to program your Raspberry Pi's GPIO 
pins from a modern webinterface.

Googles excellent [Blockly](https://developers.google.com/blockly/) library is used to
create programs to allow everyone to get up and running quickly.

<u>Features</u>
- Super easy and fast to install using Docker and Docker Compose
- Highly customizable programming environment
- Modern Webinterface based on python django

## Installation
1. Clone this repository at your desired install location
2. Initialize submodules with `git submodule update --init --recursive`
3. Copy `.env.template` to `.env` and fill in every variable accordingly
4. Start the docker container using `docker-compose up -d`

## License
Most of the Code in this repository is licensed under the MIT License which basically allows you to do whatever you want.
Click [here](https://github.com/vabene1111/Django-PiGPIO/blob/master/LICENSE.md) to see some actually useful information 
about what you can and cannot do.

The code used for the **interpreter** is taken and modified from Jay Conrod. Please see the
copyright information provided [here](https://github.com/vabene1111/Django-PiGPIO/blob/master/PiGPIO/interpreter/COPYRIGHT.md)