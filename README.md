Quorum
======

**Quorum** is an internet based knowledge sharing. Quorum is mainly focused on question answering web search engine founded in Jan 2014 by Capsone Software solutions Pvt, Ltd, Chennai, India.

Quorum is a question and answer website where questions are created ,answered and organized by its community of users. Quorum aggregates questions and answers under the topics. Users can collaborate by editing their answer and suggesting the users to answer the questions.

In first phase of release mainly focused only by asking the question and answer the question. User can edit their own answer which answered previously. User can follow any topics and questions. They can edit their profile and view the others profile too. Quorum contains built in search engine to search both question and answer in single place.

Quorum requires users to register with their details to login. Once they registered activation link will send to registered email. User needs to activate the link to login. 

Quorum uses the bootstrap as front-end, Django and python technologies as backend. Ubuntu Link as operating system with SQLlite3 as database.


## Quick start

#### Installation 


##### Requirements

+ Django==1.5.4
+ django-crispy-forms
+ django-haystack
+ Whoosh



##### Create virtual env and activate it(optional)

    virtualenv --no-site-packages quorumenv
    source quorumenv/bin/activate

#### Edit `settings.py`

##### Add `crispy_forms`,`quorum`, `registration`, `haystack` to your `INSTALLED_APPS` setting like this::

    INSTALLED_APPS = (
          ...
          ...
        'crispy_forms',
        'quorum',
        'registration',
        'haystack',
          ...
          ...        	
    )

    #crispy template tag settings
    CRISPY_TEMPLATE_PACK = 'bootstrap'

    LOGIN_REDIRECT_URL = '/quorum/'

##### Add request context processor

    from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
    TEMPLATE_CONTEXT_PROCESSORS += (

    	......

    	'django.core.context_processors.request',
    	'django.contrib.messages.context_processors.messages',

    	.....
    )


if there isn't any `TEMPLATE_CONTEXT_PROCESSORS` variable in settings.py then import and append it:

    from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.request',)

##### set Database and Staticfiles

    import os
    PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    dbpath=PROJECT_DIR
    STATICFILES_DIRS = (os.path.join(PROJECT_DIR,'..','..', 'static'),)

    ........

    DATABASES = {
    	'default': {
    		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    		'NAME':  os.path.join(dbpath, 'sqlite3.db'), # Or path to database file if using sqlite3.
    		'USER': '',
    		'PASSWORD': '',
    		'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
    		'PORT': '', # Set to empty string for default.
    	}
    }

    .......

    STATIC_ROOT = os.path.join(PROJECT_DIR, '..', 'static')

    

Run the `collectstatic` management command:

    python manage.py collectstatic

This will copy all files from `quorum/static` folders into the `STATIC_ROOT` directory.


#### Edit the URLconf

Include the `quorum` and `accounts` URLconf in your project `urls.py` like this::
    
    urlpatterns = patterns('',
    	.............
    	.............

        url(r'^quorum/', include('quorum.urls')),
        url(r'^accounts/', include('registration.urls')),
        url(r'^users/(?P<username>\w+)/$', 'quorum.views.quorumuser'),
        url(r'^search/', include('haystack.urls')),

        ................
        ...............
    )

    from haystack.query import SearchQuerySet
    sqs = SearchQuerySet()
    from haystack.views import SearchView, search_view_factory
    urlpatterns += patterns('haystack.views',

    	url(r'^quorum/search/$', search_view_factory(
    		view_class=SearchView,
    		template='quorum/search.html',
    		searchqueryset=sqs,
    		),
    	name='haystack_search'),
    )


#### HAYSTACK_CONNECTIONS

This setting controls which backends should be available. It should be a dictionary of dictionaries resembling the following..


	HAYSTACK_CONNECTIONS = {
		'default': {
			'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
			'PATH': os.path.join(dbpath, 'whoosh_index'),
		},
	}


#### Run the site.

`python manage.py syncdb` to create the models. 

Then start the development server(`python manage.py runserver`) and visit http://127.0.0.1:8000/quorum.


#### Add sample data

open python console by typing `python manage.py shell`

on console :

    >>> from quorum import sampledata
    >>> sampledata.initd()
    >>> exit()


## contribute

If you would like to make changes and contribute them back to the project, fork the GitHub project, 
make your changes, and submit a pull request. This process is beyond the scope of this documentation; 
for more information, see [GitHub’s documentation](http://help.github.com).

