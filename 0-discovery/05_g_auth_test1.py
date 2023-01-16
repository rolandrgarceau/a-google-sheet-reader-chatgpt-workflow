import google.auth

'''simple test from https://google-auth.readthedocs.io/en/latest/reference/google.auth.html

This script should print the credentials to the console, but it does not. This is where the concept of ADC (Application Default Credentials) might be introduced

Really we probably need to verify that the credential file is in a properly consumable format.'''

credentials, project = google.auth.default()

print(credentials)