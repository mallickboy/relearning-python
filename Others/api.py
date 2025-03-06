import requests
from mylib.runtime import runtime

@runtime
def fetch_random_user():
    url= "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response= requests.get(url)
    data= response.json()
    if data["success"] and "data" in data:
        user_data= data["data"]
        user_name= user_data["login"]["username"]
        user_country= user_data["location"]["country"]
        return user_name, user_country
    else:
        raise Exception("Failed to fetch user data")
# fetch_random_user()

def main():
    try:
        user_name, user_country= fetch_random_user()
        print(f"Username: {user_name}, Country: {user_country}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()