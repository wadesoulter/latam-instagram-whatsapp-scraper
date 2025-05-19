import instaloader
import time
import random

def scrape_seed_users(seed_usernames, config):
    L = instaloader.Instaloader()
    scraped_usernames = set()

    for username in seed_usernames:
        try:
            profile = instaloader.Profile.from_username(L.context, username)

            limit = config['scrape_limit']
            delay_min = config['delay_range']['min']
            delay_max = config['delay_range']['max']

            for follower in profile.get_followers():
                scraped_usernames.add(follower.username)
                if len(scraped_usernames) >= limit:
                    break
                time.sleep(random.uniform(delay_min, delay_max))

            for following in profile.get_followees():
                scraped_usernames.add(following.username)
                if len(scraped_usernames) >= limit:
                    break
                time.sleep(random.uniform(delay_min, delay_max))

        except Exception as e:
            print(f"[!] Error scraping {username}: {e}")

    return list(scraped_usernames)
