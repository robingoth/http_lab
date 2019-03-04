import requests
import time

def main():
    url = "http://192.168.4.69:80/"
    data = {"username": "grumpy_cat", "password": "Im_not_grumpy_you_are"}
    while 1:
        response = requests.post(url=url, params=data)
        print(response)
        time.sleep(1)

if __name__ == "__main__":
    main()
