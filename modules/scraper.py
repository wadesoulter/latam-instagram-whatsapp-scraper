import instaloader

def init_loader(username):
    L = instaloader.Instaloader()
    try:
        L.load_session_from_file(username)
        print(f"[+] Logged in as {username}")
    except FileNotFoundError:
        print(f"[!] Session file for {username} not found.")
    return L

def scrape_user_data(username):
    L = init_loader("your_instagram_username")  # Replace this with your IG username
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        print(f"[+] Scraped {profile.username}: {profile.full_name}, {profile.followers} followers")
        return {
            "username": profile.username,
            "full_name": profile.full_name,
            "followers": profile.followers
        }
    except Exception as e:
        print(f"[!] Error scraping {username}: {e}")
        return None
