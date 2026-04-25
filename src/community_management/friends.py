import json
import os

FRIENDS_FILE = "friends.json"
REQUESTS_FILE = "friend_requests.json"

friends = []
friend_requests = []

def load_friends():
    global friends
    if os.path.exists(FRIENDS_FILE):
        with open(FRIENDS_FILE, "r") as f:
            friends = json.load(f)
    else:
        friends = []

def save_friends():
    with open(FRIENDS_FILE, "w") as f:
        json.dump(friends, f, indent=4)

def load_requests():
    global friend_requests
    if os.path.exists(REQUESTS_FILE):
        with open(REQUESTS_FILE, "r") as f:
            friend_requests = json.load(f)
    else:
        friend_requests = []

def save_requests():
    with open(REQUESTS_FILE, "w") as f:
        json.dump(friend_requests, f, indent=4)

def get_mutual_friends(user1, user2):
    """Return mutual friends between two users."""
    load_friends()
    user1_friends = [f["name"] for f in friends if f["owner"].lower() == user1.lower()]
    user2_friends = [f["name"] for f in friends if f["owner"].lower() == user2.lower()]
    return list(set(user1_friends) & set(user2_friends))

def friends_tab():
    load_friends()
    load_requests()
    while True:
        print("\n=== Friends Menu ===")
        print("1. View Friends")
        print("2. Send Friend Request")
        print("3. View Friend Requests")
        print("4. Accept/Reject Request")
        print("5. View Mutual Friends")
        print("6. Back to Community")

        choice = input("Choose an option: ")

        if choice == "1":
            if not friends:
                print("No friends yet. Add someone!")
            else:
                for i, friend in enumerate(friends, start=1):
                    print(f"{i}. Owner: {friend['owner']} → Friend: {friend['name']} ({friend.get('contact','N/A')})")

        elif choice == "2":
            from_name = input("Enter your name: ")
            to_name = input("Enter the name of the person you want to send a request to: ")
            friend_requests.append({"from": from_name, "to": to_name, "status": "pending"})
            save_requests()
            print(f"📩 Friend request sent from {from_name} to {to_name}")

        elif choice == "3":
            if not friend_requests:
                print("No pending requests.")
            else:
                for i, req in enumerate(friend_requests, start=1):
                    print(f"{i}. {req['from']} → {req['to']} (Status: {req['status']})")

        elif choice == "4":
            if not friend_requests:
                print("No requests to process.")
            else:
                for i, req in enumerate(friend_requests, start=1):
                    print(f"{i}. {req['from']} → {req['to']} (Status: {req['status']})")
                try:
                    idx = int(input("Enter request number to process: "))
                    if 1 <= idx <= len(friend_requests):
                        decision = input("Accept (a) or Reject (r)? ").lower()
                        if decision == "a":
                            req = friend_requests[idx - 1]
                            # Add both sides to friends.json
                            friends.append({"owner": req["from"], "name": req["to"], "contact": "N/A"})
                            friends.append({"owner": req["to"], "name": req["from"], "contact": "N/A"})
                            save_friends()
                            friend_requests[idx - 1]["status"] = "accepted"
                            print(f"✅ {req['from']} and {req['to']} are now friends!")
                        elif decision == "r":
                            friend_requests[idx - 1]["status"] = "rejected"
                            print("❌ Request rejected.")
                        save_requests()
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            user1 = input("Enter first user name: ").strip()
            user2 = input("Enter second user name: ").strip()
            mutuals = get_mutual_friends(user1, user2)
            if mutuals:
                print(f"🤝 Mutual Friends between {user1} and {user2}: {mutuals}")
            else:
                print(f"No mutual friends found between {user1} and {user2}.")

        elif choice == "6":
            break
        else:
            print("Invalid choice, try again.")
