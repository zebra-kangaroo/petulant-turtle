WePay Python SDK
================

WePay's API allows you to easily add payments into your application.

For full documentation, see [WePay's developer documentation](https://www.wepay.com/developer).

For current and previous versions, see [PyPI](https://pypi.python.org/pypi/wepay).

Installation
-----
Create a Python 3.4.3 virtual environment

    pyenv virtualenv 3.4.3 wepaysdk

Active virtual environment

    pyenv activate wepaysdk

Install the Wepay module

	pip install -e git+ssh://git@github.devops.wepay-inc.com/api-team/python_sdk.git@master#egg=wepay
	
OR, from sources by cloning ``git@github.devops.wepay-inc.com:api-team/python_sdk.git``. Install the dependencies

	pip install -r config/requirements.txt

Testing
-----
Run tests 
	
	python -m unittest test/test_api.py
	
Usage
-----
Run the test file provided with the sources

	python sdk_test.py

Setup
-----
Import the module:

    from wepay import WePay

Instantiate
-----

Create a new ``WePay`` instance. With no arguments, it will use the production
version of WePay ([www.wepay.com](https://www.wepay.com/)). If called with ``production=False`` then
it will use the staging version ([stage.wepay.com](https://stage.wepay.com/)) for testing:

    wepay = WePay()

If your user has already authorized your application and you still have the
access token, you can instantiate the SDK with the optional ``access_token``
parameter. Afterwards, ``wepay.call()`` will use the given token for the
authorization header:

    wepay = WePay(access_token=USERS_ACCESS_TOKEN)

To set an [API-Version](https://www.wepay.com/developer/reference/versioning) in the header with your call request, use::

    wepay = WePay(production=False, access_token=USERS_ACCESS_TOKEN, api_version=API_VERSION)

Make some calls
-----

You are now ready to do anything on behalf of your user. Let's start by making
few calls:

    # Call /user
	call_reps = wepay.call('/user')
	print(call_reps)

Now call ``/app`` endpoint

	# Call /app
	params = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
	call_reps = wepay.call('/app', params)
	print(call_reps)

Now let's create a credit card!:

    # Call /credit_card/create
	params = {"client_id": CLIENT_ID, "user_name": "Bob Smith", "email": "test@example.com", "cc_number": "5496198584584769", "cvv": "123", "expiration_month": 4,  "expiration_year": 2020, "address": {"address1": "test", "city": "test", "state": "CA", "country": "US", "zip": "94025"}}
	call_reps = wepay.call('/credit_card/create', params)
	print(call_reps)



Try it!
-----

These examples are put together into a working test file
``sdk_test.py``.

License
-----

MIT License
