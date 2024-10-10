from pymongo import MongoClient

client = MongoClient("mongodb+srv://youtubeManager:Chirote6266@cluster0.s03ww.mongodb.net/", tlsallowinvalidcertificates=True)

db = client["ytmanager"]
video_collection = db["videos"]
# print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}" )

def add_video(name, time):
    video_collection.insert_one({"name": name, "time" : time})

def update_video(video_id , new_name, new_time):
    video_collection.update_one(
        {'_id' : video_id},{"$set":{"name" : new_name, "time" : new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({'_id' : video_id})

def main():
    while True:
        print("\n YouTube Manger Video ")
        print("1. List all videos")
        print("2. Add videos ")
        print("3. Update videos ")
        print("4. Delete videos ")
        print("5. Exit App")
        choice  = input("Enter your Choice : ")
        
        if choice == "1":
            list_videos()
            
        elif choice == '2':
            name = input("Enter your video name : ")
            time = input("Enter your video time : ")
            add_video(name, time)
        
        elif choice == '3':
            video_id = input("Enter your video id : ")
            name = input("Enter your updated video name : ")
            time = input("Enter your updated video time : ")
            update_video(video_id, name, time)
            
        elif choice == '4':
            video_id = input("Enter your video id : ")
            delete_video(video_id)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid number select try again..")
   
if __name__ == "__main__":
    main()