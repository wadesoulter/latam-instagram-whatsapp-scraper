from modules.scraper import scrape_seed_users
from modules.filter import filter_relevant_profiles
from modules.classify import classify_accounts
from modules.export import export_to_csv
from config_loader import load_config

def main():
    config = load_config()
    raw_usernames = scrape_seed_users(config['seed_usernames'], config)
    filtered_profiles = filter_relevant_profiles(raw_usernames, config)
    classified = classify_accounts(filtered_profiles)
    export_to_csv(classified)

if __name__ == "__main__":
    main()
