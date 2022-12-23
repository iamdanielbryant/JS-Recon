import os
import requests
import re
from urllib.parse import urlparse

out_file = 'out.txt'

def extract_urls(file):
    print("Extracting urls from target source...")
    with open(file, 'r') as f:
        text = f.read()

    # Find all URLs in the text using a regular expression
    urls = re.findall(r'https?://\S+', text)

    # Strip out invalid characters from the URLs
    valid_urls = []
    for url in urls:
        url = re.sub(r'[\"\']', '', url)
        url = re.sub(r'[,]', '', url)
        parsed_url = urlparse(url)
        
        if all(parsed_url.netloc) and all(parsed_url.path):  # Check if netloc and path are present
            valid_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
            valid_urls.append(valid_url)
        

    with open(out_file, 'w') as f:
        for url in valid_urls:
            f.write(url + '\n')

    return valid_urls

def download_urls(file_path, directory):
    print("Downloading files from target...")
    # Check if the directory exists, and create it if it doesn't
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Open the file and read the URLs
    with open(file_path, 'r') as file:
        for url in file:
            # Strip the URL of leading and trailing whitespace
            url = url.strip()

            # Download the URL
            response = requests.get(url)
            content = response.content

            # Get the file name from the URL
            file_name = url.split("/")[-1]

            # Save the file to the directory
            with open(os.path.join(directory, file_name), 'wb') as f:
                f.write(content)

    print("Downloading files COMPLETE!")


