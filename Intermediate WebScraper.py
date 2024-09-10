import requests
from bs4 import BeautifulSoup
import json
import os

# URL of the new website to scrape
url = "https://www.python.org/"

# File path for the JSON file
json_file_path = "python_org_data.json"

# Check if the JSON file already exists
if os.path.exists(json_file_path):
    # If the JSON file exists, load existing data from it
    with open(json_file_path, "r") as json_file:
        existing_data = json.load(json_file)
else:
    # If the JSON file doesn't exist, initialize an empty dictionary
    existing_data = {}

try:
    # Sending a GET request to the URL
    page = requests.get(url)

    # Checking if the request was successful (status code 200)
    if page.status_code == 200:
        # Parsing the HTML content of the page
        soup = BeautifulSoup(page.text, "html.parser")

        # Scrape news items with error checking
        news_items = soup.find_all("li", class_="menu-item")
        if news_items:
            existing_data["news"] = [
                {"title": item.find("a").text.strip(), "link": item.find("a")["href"]}
                for item in news_items if item.find("a")
            ]
        else:
            existing_data["news"] = []

        # Scrape upcoming events with error checking
        shrubbery_div = soup.find("div", class_="shrubbery")
        if shrubbery_div:
            events = shrubbery_div.find_all("li")
            existing_data["events"] = [
                {"event": event.find("a").text.strip(), "date": event.find("time").text.strip()}
                for event in events if event.find("a") and event.find("time")
            ]
        else:
            existing_data["events"] = []

        # Scrape the latest Python release version with error checking
        latest_release = soup.find("div", class_="latest-release")
        if latest_release:
            release_version = latest_release.find("span", class_="release-version")
            release_date = latest_release.find("span", class_="release-date")
            existing_data["latest_release"] = {
                "version": release_version.text.strip() if release_version else "N/A",
                "release_date": release_date.text.strip() if release_date else "N/A"
            }
        else:
            existing_data["latest_release"] = {"version": "N/A", "release_date": "N/A"}

        # Printing scraped data
        print("News Items:")
        for news in existing_data["news"]:
            print(f"Title: {news['title']}, Link: {news['link']}")

        print("\nUpcoming Events:")
        for event in existing_data["events"]:
            print(f"Event: {event['event']}, Date: {event['date']}")

        print(f"\nLatest Python Release: {existing_data['latest_release']['version']}, "
              f"Released on: {existing_data['latest_release']['release_date']}")

        # Save updated data back to the JSON file
        with open(json_file_path, "w") as json_file:
            json.dump(existing_data, json_file)

        print("\nData updated and saved to 'python_org_data.json' successfully.")

    else:
        print("Failed to retrieve the page. Status Code:", page.status_code)

except requests.RequestException as e:
    # Handling network-related errors
    print("An error occurred:", e)

except Exception as e:
    # Handling unexpected errors
    print("An unexpected error occurred:", e)
