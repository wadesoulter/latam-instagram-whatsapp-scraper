import re

def extract_whatsapp(text):
    pattern = r"(?:\+?\d{1,3})?[\s\-]?\(?\d{1,4}\)?[\s\-]?\d{3,4}[\s\-]?\d{3,4}"
    match = re.findall(pattern, text)
    return match

def extract_group_links(text):
    group_pattern = r"(https?://chat\.whatsapp\.com/[a-zA-Z0-9]+)"
    return re.findall(group_pattern, text)
