"""main.py scrapes emails from Google search results"""
import sys
import time
from datetime import timedelta

try:
    from packages.utils import (
        get_emails,
        store_urls
    )

    from fake_useragent import UserAgent

except ModuleNotFoundError as e:
    print(e)
    print("Please install dependencies from requirements.txt")


async def scrape(searches_items, count):
    ua=UserAgent()
    unique_emails = []
    file_name = store_urls(searches_items, count)
    with open(file_name, "r", encoding="utf-8") as url_file:
        for url_no, url in enumerate(url_file):
            url = url.strip()
            if not url.endswith(".pdf"):
                
                emails, msg = get_emails(url.strip(), ua.random)
                if msg == "break":
                    return unique_emails
                print(f"url number {url_no + 1} Status: {msg}")
                if emails:
                    for email in emails:
                        if email not in unique_emails:
                            if email.endswith((".com", ".net", ".org")):
                                unique_emails.append(email)
                else:
                    continue

    return unique_emails   
