from wepay import WePay


# CLIENT_ID of your app
CLIENT_ID = ''

# CLIENT_SECRET of your app
CLIENT_SECRET = ''

# Production, Stage, Stage-internal, VM
TARGET_ENVIRONMENT = 'Production'

# ACCESS_TOKEN of your app
ACCESS_TOKEN = ''

# ACCOUNT_ID of your app
ACCOUNT_ID = ''

# Internal calls, set to to True for making internal calls
INTERNAL_CALLS = False


# Create the wepay API instance
wepay = WePay(TARGET_ENVIRONMENT, ACCESS_TOKEN, INTERNAL_CALLS)

# Call /user
user_reps = wepay.call('/user')
print(user_reps)

# Call /app
params = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
app_reps = wepay.call('/app', params)
print(app_reps)

# Call /credit_card/create
params = {"client_id": CLIENT_ID, "user_name": "Bob Smith", "email": "test@example.com", "cc_number": "5496198584584769", "cvv": "123", "expiration_month": 4,  "expiration_year": 2020, "address": {"address1": "test", "city": "test", "state": "CA", "country": "US", "zip": "94025"}}
call_reps = wepay.call('/credit_card/create', params)
print(call_reps)

# Call /credit_card GET
if 'credit_card_id' in call_reps:
    params = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "credit_card_id": call_reps["credit_card_id"]}
    call_reps = wepay.call('/credit_card', params)
    print(call_reps)

# Call /checkout/create
if 'credit_card_id' in call_reps:
    params = {"account_id": ACCOUNT_ID, "short_description": "Donation to Smith Cancer Fund", "long_description": "This is a donation to help Bob Smith get the treatment", "type": "DONATION", "reference_id": "abc123", "amount": "100.75", "currency": "USD", "app_fee": "5.5", "fee_payer": "payee", "auto_capture": "false", "payment_method_id":  call_reps["credit_card_id"], "payment_method_type": "credit_card"}
    call_reps = wepay.call('/checkout/create', params)
    print(call_reps)

# Set up for Internal calls
INTERNAL_CALLS = True
wepay_internal = WePay(TARGET_ENVIRONMENT, ACCESS_TOKEN, INTERNAL_CALLS)

# Call /internal/user/sample
if 'user_id' in user_reps:
    params = {"user_id": user_reps["user_id"], "app_id": app_reps['client_id']}
    internal_resp = wepay_internal.call('/user/sample', params)
    print(internal_resp)
