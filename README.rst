Referly
========

An awesome referral app http://referly.herokuapp.com/


Developer Installation
-----------------------

For getting this running on your local machine:

1. Set up a virtualenv.
2. Install all the supporting libraries into your virtualenv::

    pip install -r requirements/local.txt

3. Install Grunt Dependencies.

    npm install

4. Run development server. (For browser auto-reload, use Livereload_ plugins.)

    grunt serve


Usage
------

JSON fixtures is used to generate test data.
For login:
    username: 'timlee'
    password: 'timlee'


REST API
--------

``django-rest-framework`` is used for REST API.

1. ``/apiv1/referrals/`` - API endpoint for list of referrals. ``GET, POST, HEAD, OPTIONS`` are allowed http methods.

2. ``/apiv1/referral/{{referral_id}}`` - API endpoint for particular referral. ``referral_id`` must
provided. ``GET, PUT, PATCH, DELETE, HEAD, OPTIONS``` http methods are allowed.

3. ``/apiv1/user/{{username}}``` - API endpoint for an user. ``GET, HEAD, OPTIONS`` are allowed.