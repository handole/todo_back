### TODO LIST BACKEND

Please used virtualenvironment with python3.6
>> virtualenv ven -p python3.6

activation virtualenvironment
>> source ven/binactivation

install the requirments, go to directory
>> pip install -r requirements.txt

run migration
>> python manage.py makemigrations

>> python manage.py migrate

create super user
>> python manage.py createsuperuser

run application
>> python manage.py runserver