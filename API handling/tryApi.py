import requests

def random_books_freeapi():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data[data]
        volumeinfo = user_data["title"]["subtitle"]
        authors = user_data["publisher"]["publishedDate"]
        return volumeinfo , authors
    else:
        raise Exception("Failed to fetch user data ")
    
    
def main():
    try:
        volumeinfo, authors = random_books_freeapi()
        print(f"Volumeinfo: {volumeinfo} \n authors :{authors}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
         