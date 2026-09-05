import json
import os
import sys
import webbrowser
from pathlib import Path

import bs4
import requests


DOWNLOAD_FOLDER = Path("web_downloads")
DOWNLOAD_FOLDER.mkdir(exist_ok=True)


def inspect_webpage():
    url = input("\nURL to inspect: ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\nDownloading {url}...")

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Could not download page: {exc}")
        return

    print(f"HTTP status: {response.status_code}")
    print(f"Downloaded {len(response.text):,} characters.")

    soup = bs4.BeautifulSoup(response.text, "html.parser")

    if soup.title:
        print(f"\nTitle: {soup.title.get_text(strip=True)}")
    else:
        print("\nTitle: No <title> element found.")

    headings = soup.select("h1, h2, h3")
    print("\nHeadings:")
    if headings:
        for heading in headings[:10]:
            print(f"  {heading.name}: {heading.get_text(' ', strip=True)}")
    else:
        print("  No headings found.")

    links = soup.select("a[href]")
    print("\nFirst links:")
    if links:
        for link in links[:10]:
            text = link.get_text(" ", strip=True) or "(no text)"
            href = link.get("href")
            print(f"  {text} -> {href}")
    else:
        print("  No links found.")

    save = input("\nSave the downloaded HTML? (y/n): ").strip().lower()
    if save == "y":
        output_file = DOWNLOAD_FOLDER / "downloaded_page.html"

        with open(output_file, "wb") as file:
            file.write(response.content)

        print(f"Saved to {output_file.resolve()}")


def download_file():
    url = input("\nFile URL: ").strip()

    if not url.startswith(("http://", "https://")):
        print("Please enter a full http:// or https:// URL.")
        return

    filename = input("Save as filename: ").strip()

    if not filename:
        print("Filename cannot be empty.")
        return

    output_file = DOWNLOAD_FOLDER / Path(filename).name

    print(f"\nDownloading {url}...")

    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        with open(output_file, "wb") as file:
            for chunk in response.iter_content(100000):
                if chunk:
                    file.write(chunk)

    except requests.RequestException as exc:
        print(f"Download failed: {exc}")
        return

    print(f"Saved to {output_file.resolve()}")


def open_map():
    address = input("\nAddress or place: ").strip()

    if not address:
        print("No address entered.")
        return

    url = "https://www.openstreetmap.org/search?query=" + address
    print(f"Opening: {url}")
    webbrowser.open(url)


def weather_api():
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        print(
            "\nSet the OPENWEATHER_API_KEY environment variable first.\n"
            'Example on macOS/Linux:\n'
            'export OPENWEATHER_API_KEY="your_key_here"'
        )
        return

    city = input("\nCity: ").strip()
    country = input("Country code, for example GB, CL, BR, US: ").strip().upper()

    if not city or not country:
        print("City and country code are required.")
        return

    geo_url = (
        "https://api.openweathermap.org/geo/1.0/direct"
        f"?q={city},{country}&appid={api_key}"
    )

    try:
        geo_response = requests.get(geo_url, timeout=15)
        geo_response.raise_for_status()

        geo_data = json.loads(geo_response.text)

        if geo_data == []:
            print("City not found.")
            return

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

        weather_url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?lat={lat}&lon={lon}&appid={api_key}"
        )

        weather_response = requests.get(weather_url, timeout=15)
        weather_response.raise_for_status()
        weather_data = json.loads(weather_response.text)

    except (requests.RequestException, KeyError, json.JSONDecodeError) as exc:
        print(f"Could not get weather: {exc}")
        return

    temp_kelvin = weather_data["main"]["temp"]
    feels_kelvin = weather_data["main"]["feels_like"]

    temp_celsius = round(temp_kelvin - 273.15, 1)
    feels_celsius = round(feels_kelvin - 273.15, 1)

    description = weather_data["weather"][0]["description"]
    humidity = weather_data["main"]["humidity"]

    print(f"\nWeather for {city}:")
    print(f"  Conditions: {description}")
    print(f"  Temperature: {temp_celsius} °C")
    print(f"  Feels like: {feels_celsius} °C")
    print(f"  Humidity: {humidity}%")


def selenium_demo():
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
    except ImportError:
        print("\nSelenium is not installed.")
        print("Run: python3 -m pip install selenium")
        return

    browser = None

    try:
        print("\nOpening Selenium browser...")
        browser = webdriver.Firefox()
        browser.get("https://autbor.com/example3.html")

        username = browser.find_element(By.ID, "login_user")
        password = browser.find_element(By.ID, "login_pass")
        checkbox = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
        paragraphs = browser.find_elements(By.TAG_NAME, "p")

        username.send_keys("chapter13_user")
        password.send_keys("practice_password")

        checkbox.click()

        print(f"Found {len(paragraphs)} <p> elements.")
        if paragraphs:
            print("First paragraph:", paragraphs[0].text)

        input("\nSelenium is controlling the browser. Press Enter to close it.")

    except Exception as exc:
        print(f"Selenium demo failed: {exc}")

    finally:
        if browser is not None:
            browser.quit()


def playwright_demo():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("\nPlaywright is not installed.")
        print("Run:")
        print("  python3 -m pip install playwright")
        print("  python3 -m playwright install")
        return

    try:
        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False, slow_mo=100)
            page = browser.new_page()
            page.goto("https://autbor.com/example3.html")

            print("\nPage title:", page.title())

            paragraphs = page.locator("p")
            print("Number of <p> elements:", paragraphs.count())

            if paragraphs.count() > 0:
                print("First paragraph:", paragraphs.nth(0).inner_text())

            username = page.locator("
            password = page.locator("
            checkbox = page.locator('input[type="checkbox"]')

            if username.is_visible():
                username.fill("chapter13_user")

            if password.is_visible():
                password.fill("practice_password")

            if checkbox.is_visible():
                checkbox.check()

            input("\nPlaywright is controlling the browser. Press Enter to close it.")
            browser.close()

    except Exception as exc:
        print(f"Playwright demo failed: {exc}")


def open_url():
    url = input("\nURL to open: ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    webbrowser.open(url)


def print_menu():
    print(
        """
===============================
 CHAPTER 13 WEB TOOLKIT
===============================
1. Inspect a webpage
2. Download a file
3. Open a place in OpenStreetMap
4. Get current weather from an API
5. Selenium browser-control demo
6. Playwright browser-control demo
7. Open any URL in my browser
8. Quit
"""
    )


def main():
    while True:
        print_menu()
        choice = input("Choose 1-8: ").strip()

        if choice == "1":
            inspect_webpage()
        elif choice == "2":
            download_file()
        elif choice == "3":
            open_map()
        elif choice == "4":
            weather_api()
        elif choice == "5":
            selenium_demo()
        elif choice == "6":
            playwright_demo()
        elif choice == "7":
            open_url()
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Please choose a number from 1 to 8.")


if __name__ == "__main__":
    main()