import re
from datetime import datetime

def is_fake_account(profile):
    score = 0

    created_date = datetime.strptime(profile["created_on"], "%Y-%m-%d")
    age_days = (datetime.now() - created_date).days
    if age_days < 30:
        score += 1
    if profile["followers"] < 10:
        score += 1
    if profile["posts"] < 5:
        score += 1
    if re.match(r"user\d+", profile["username"]):
        score += 1

    return score >= 3

def get_profiles_from_input():
    profiles = []
    print("Enter user profile details. Type 'done' when finished.\n")

    while True:
        username = input("Username: ")
        if username.lower() == "done":
            break
        bio = input("Bio: ")
        followers = int(input("Number of followers: "))
        posts = int(input("Number of posts: "))
        created_on = input("Account creation date (YYYY-MM-DD): ")

        profiles.append({
            "username": username,
            "bio": bio,
            "followers": followers,
            "posts": posts,
            "created_on": created_on
        })
        print("Profile added. Type another or 'done' to finish.\n")
    return profiles

# Get dynamic input
profiles = get_profiles_from_input()

# Analyze all profiles
print("\nFake Account Detection Results:\n")
for profile in profiles:
    if is_fake_account(profile):
        print(f"⚠  Suspicious: {profile['username']} (Followers: {profile['followers']}, Posts: {profile['posts']})")
    else:
        print(f"✅ Genuine:   {profile['username']} (Followers: {profile['followers']}, Posts: {profile['posts']})")
