import requests

def freeApi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data[data]
        Username = user_data["login"]["username"] 
        location = user_data["location"]["country"]
        return Username, location
    else:
        raise Exception("Failed to fetch to user data") 
    
    
def main():
    try:
        Username, location = freeApi()
        print(f"Username: {Username} \n location :{location}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()