import re

keywords = [
    "iphone", "samsung", "venta", "gsm", "celulares",
    "mayoreo", "reparación", "accesorios", "tecnología"
]

def filter_relevant_profiles(usernames, config):
    # This would typically include bio fetching; mocked here
    filtered = []

    for user in usernames:
        bio = mock_scrape_bio(user)  # Replace with actual scrape
        bio_lower = bio.lower()
        if any(keyword in bio_lower for keyword in keywords):
            filtered.append({
                "username": user,
                "bio": bio
            })

    return filtered

def mock_scrape_bio(username):
    # Simulate a scraped bio
    sample_bios = [
        "Venta de celulares y accesorios", "Servicio técnico iPhone",
        "Celulares Samsung al por mayor", "Reparación de teléfonos"
    ]
    import random
    return random.choice(sample_bios)
