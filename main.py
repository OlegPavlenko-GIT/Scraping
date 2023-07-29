import requests
from bs4 import BeautifulSoup

def get_email_addresses(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        email_addresses = set()

        for tag in soup.find_all('a'):
            if tag.get('href') and 'mailto:' in tag.get('href'):
                email = tag.get('href').replace('mailto:', '')
                email_addresses.add(email)

        return email_addresses

    else:
        print("Error: Unable to access the website.")
        return None

def save_emails_to_file(emails, file_name):
    with open(file_name, 'w') as file:
        for email in emails:
            file.write(email + '\n')

if __name__ == '__main__':
    url = 'https://mon.gov.ua/ua/ministerstvo/pro-ministerstvo/kontaktna-informaciy'
    output_file = 'email_addresses.txt'

    email_addresses = get_email_addresses(url)

    if email_addresses:
        print("Found email addresses:")
        for email in email_addresses:
            print(email)

        save_emails_to_file(email_addresses, output_file)
        print(f"Email addresses saved to {output_file}")
    else:
        print("No email addresses found.")
