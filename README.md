# coinmetro-api-tools
Tools which can be used with the Coinmetro API which are documented here: https://documenter.getpostman.com/view/3653795/SVfWN6KS

## get_token.py
Create a long lived token to be used on future API calls.

### How to use
* Execute get_token.py using Python3
* When Prompted, complete the following:
    * Email Address: Your Coinmetro Email Address used to login
    * Password: Your Coinmetro Password
    * Device Name: Friendly Name you are using this token for (e.g. Home Assistant)
    * OTP: Your 6 digit On-Time-Passcode from your authenticator app
* Take note of your Token and DeviceId as these are both required for all API calls
* Check your Email or goto your Coinmetro Settings to authorise app (make sure to compare the PIN number provided as they should match)

### TODO
* API available to auto authorise device however was not working, appears to be newly listed so may not yet be active