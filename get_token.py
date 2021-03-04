import requests
import uuid
import random
from getpass import getpass

apiRoot = "https://api.coinmetro.com"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

def main():
    pin = generate_pin()
    login = get_userinput("Email Address")
    password = getpass()
    devicename = get_userinput("Device Name")
    headers["X-Device-Id"]= generate_deviceid()
    headers["X-OTP"] =  get_userinput("OTP")
    token = get_token(login, password, devicename, pin)
    print(f"The PIN number was: {pin}")
    print(f"Your Token is: {token}")
    print(f"Your DeviceId is: {headers['X-Device-Id']}")


def generate_deviceid():
    response = uuid.uuid4().hex
    return response


def get_userinput(data):
    response = input(f"Enter {data}:")
    return response


def generate_pin():
    random_id = str(random.randint(0, 999999))
    return random_id


def request_api(method, api, payload):
    response = requests.request(method, f"{apiRoot}{api}", headers = headers, data = payload).json()
    return response


def get_token(login, password, devicename, pin):
    payload = f'login={login}&password={password}'
    response = request_api("POST", "/jwtDevice", payload)
    if response["message"] == "New Device":
        print("Token Generated, updating device info")
        token = response["token"]
        update_deviceinfo(token, devicename, pin)
        return token
    else:
        print(f"Error: {response['message']}")
        raise SystemExit(0)


def update_deviceinfo(token, devicename, pin):
    payload = f'deviceName={devicename}&accessToken={token}&PIN={pin}'
    response = request_api("POST", "/devices", payload)
    if response["message"] == "PIN updated":
        return response
    else:
        print(f"Error: {response['message']}")
        print(f"You will need to Decline/Remove this device from your account before trying again")
        raise SystemExit(0)
    return (response)


if __name__ == "__main__":
    main()



