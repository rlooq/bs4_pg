''' This is a script to grab text from websites where main article is between <p> tags.
    Then it saves it to a text file with a timestamp.'''

import bs4
from bs4 import BeautifulSoup as soup
import requests
from requests.exceptions import HTTPError
import datetime

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
headers = {'User-Agent': user_agent}

my_url=""

try:
    response = requests.get(my_url, headers=headers)
    response.raise_for_status()
    # If the response is successful, no exception will be raised
    page=soup(response.text, "html.parser")
    
    with open("texto_{}.txt".format(str(datetime.date.today().strftime("%Y-%m-%d-%H-%M"))), "w") as file:
        for i in page.findAll("p"):
            file.write((i.text + "\n"))
        file.write("\n\n{} \n{}\n".format(my_url, str(datetime.datetime.today())[:-7]))

except HTTPError as http_err:
    print('HTTP error occurred: {}'.format(http_err))
except Exception as err:
    print('Other errors occurred: {}'.format(err))
else:
        print('Success!')

