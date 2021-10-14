# shop
shopping website with Django

For start the project , the first step is to create venv in main directory of the project:

* in linux:
* 
    sudo apt install python3-venv
* 
    python3 -m venv venv
* 
    source venv/bin/activate
------------------------------------------
* in windows :
* 
    pip install virtualenv
* 
    2-virtualenv --python C:\Path\To\Python\python.exe venv
* 
    .\venv\Scripts\activate

after activate venv you should instal requirments:

    pip install -r requirements.txt

then you should create postgres db and then connect to the django and in shop.settings you should add db specs like this :



  	DATABASES = {  
		'default': {
        	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        	'NAME': 'shop',
        	'USER': 'postgres',
			'PASSWORD':'new.admin.',
        	'HOST': 'localhost',
        	'PORT': '5432',
    	}
	}

then run these commands by steps:

	1- python manage.py makemigrations
	2- python mange.py migrate
	3- pythn manage.py createsuperuser
	4- python manage.py runserver
