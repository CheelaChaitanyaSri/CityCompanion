import json
import os
from datetime import datetime
from src.community_management.friends import friends_tab, load_friends, friends

POSTS_FILE = "community_posts.json"
posts = []

def load_posts():
    global posts
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, "r") as f:
            posts = json.load(f)
    else:
        posts = []

def save_posts():
    with open(POSTS_FILE, "w") as f:
        json.dump(posts, f, indent=4)

def community_tab():
    load_posts()  # load posts at start
    while True:
        print("\n=== Community Board ===")
        print("1. View Posts")
        print("2. Add Post")
        print("3. Delete Post")
        print("4. Search Posts")
        print("5. Edit Post")
        print("6. Friends")
        print("7. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            if not posts:
                print("No posts yet. Be the first to share!")
            else:
                for i, post in enumerate(posts, start=1):
                    tag_info = f" [Tagged: {post['tagged']}]" if "tagged" in post else ""
                    print(f"{i}. {post['author']} ({post['timestamp']}): {post['content']}{tag_info}")
        elif choice == "2":
            author = input("Enter your name: ")
            content = input("Write your post: ")

            # Tagging a friend
            load_friends()
            tag_friend = input("Tag a friend? (enter name or leave blank): ").strip()
            tagged = None
            if tag_friend:
                for f in friends:
                    if f["name"].lower() == tag_friend.lower():
                        tagged = f["name"]
                        break
                if not tagged:
                    print("⚠️ Friend not found in your list. Post will be saved without tagging.")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            post = {"author": author, "content": content, "timestamp": timestamp}
            if tagged:
                post["tagged"] = tagged
            posts.append(post)
            save_posts()
            print("✅ Post added successfully!")
        elif choice == "3":
            if not posts:
                print("No posts to delete.")
            else:
                for i, post in enumerate(posts, start=1):
                    print(f"{i}. {post['author']} ({post['timestamp']}): {post['content']}")
                try:
                    idx = int(input("Enter post number to delete: "))
                    if 1 <= idx <= len(posts):
                        deleted = posts.pop(idx - 1)
                        save_posts()
                        print(f"🗑️ Deleted post by {deleted['author']}")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "4":
            keyword = input("Enter keyword, author, or tagged friend: ").lower()
            results = [p for p in posts if keyword in p['author'].lower() or keyword in p['content'].lower() or ("tagged" in p and keyword in p['tagged'].lower())]
            if results:
                print("\n🔍 Search Results:")
                for i, post in enumerate(results, start=1):
                    tag_info = f" [Tagged: {post['tagged']}]" if "tagged" in post else ""
                    print(f"{i}. {post['author']} ({post['timestamp']}): {post['content']}{tag_info}")
            else:
                print("No matching posts found.")
        elif choice == "5":
            if not posts:
                print("No posts to edit.")
            else:
                for i, post in enumerate(posts, start=1):
                    print(f"{i}. {post['author']} ({post['timestamp']}): {post['content']}")
                try:
                    idx = int(input("Enter post number to edit: "))
                    if 1 <= idx <= len(posts):
                        new_content = input("Enter new content: ")
                        posts[idx - 1]["content"] = new_content
                        posts[idx - 1]["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        save_posts()
                        print("✏️ Post updated successfully!")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "6":
            friends_tab()
        elif choice == "7":
            break
        else:
            print("Invalid choice, try again.")
