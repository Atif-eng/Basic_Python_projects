import requests

def shorten_url(long_url):
    try:
        response = requests.get(f"http://tinyurl.com/api-create.php?url={long_url}")
        if response.status_code == 200:
            return response.text
        else:
            return "Failed to shorten URL"
    except Exception as e:
        return f"Error: {e}"

# Get the long URL from the user
long_url = input("Enter the long URL: ")

# Shorten the URL
short_url = shorten_url(long_url)

# Print the shortened URL
print(f"Shortened URL: {short_url}")

