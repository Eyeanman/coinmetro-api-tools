import requests
import uuid
import random
from getpass import getpass

random_id = ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])

apiRoot = "https://api.coinmetro.com"

def main():
    pin = generate_pin()
    deviceid = generate_deviceid()
    login = get_userinput("Email Address")
    password = getpass()
    devicename = get_userinput("Device Name")
    OTP = get_userinput("OTP")
    token = get_token(login, password, OTP, deviceid, devicename, pin)
    print(f"The PIN number was: {pin}")
    print(f"Your Token is: {token}")
    print(f"Your DeviceId is: {deviceid}")


def generate_deviceid():
    response = uuid.uuid4().hex
    return response


def get_userinput(data):
    response = input(f"Enter {data}:")
    return response


def generate_pin():
    random_id = str(random.randint(0, 999999))
    return random_id


def request_api(method, api, headers, payload):
    response = requests.request(method, f"{apiRoot}{api}", headers = headers, data = payload).json()
    return response


def get_token(login, password, OTP, deviceid, devicename, pin):
    payload = f'login={login}&password={password}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-OTP': OTP,
    'X-Device-Id': deviceid,
    }
    response = request_api("POST", "/jwtDevice", headers, payload)
    if response["message"] == "New Device":
        print("Token Generated, updating device info")
        token = response["token"]
        update_deviceinfo(token, deviceid, devicename, pin)
        return token
    else:
        print(f"Error: {response['message']}")
        raise SystemExit(0)


def update_deviceinfo(token, deviceid, devicename, pin):
    payload = f'deviceName={devicename}&accessToken={token}&PIN={pin}'
    headers = {
        'X-Device-ID': deviceid,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = request_api("POST", "/devices", headers, payload)
    if response["message"] == "PIN updated":
        return response
    else:
        print(f"Error: {response['message']}")
        raise SystemExit(0)
    return (response)


if __name__ == "__main__":
    main()



