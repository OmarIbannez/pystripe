# django1.9 template

Creating your project
=====================

    $ django-admin startproject --template=https://github.com/OmarIbannez/django1.9_template/archive/master.zip --extension=py,rst,html project_name

Installing virtualenv
=====================

    $ sudo apt-get install python-virtualenv

Installing nginx
=====================

    $ sudo apt-get install nginx

Installing postgresql
=====================

    $ sudo apt-get install libpq-dev python-dev
    $ sudo apt-get install postgresql postgresql-contrib


Creating virtualenv
=====================

    $ virtualenv -p /usr/bin/python3 venv

Installing dependencies
=====================

    $ source venv/bin/activate
    $ pip install -r requirements/requirements.txt
