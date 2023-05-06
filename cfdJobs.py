import requests
from bs4 import BeautifulSoup
import configparser

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

class cfdJobs():
    def __init__(self):
        # Read user-defined url from config file
        cfg = configparser.RawConfigParser()
        cfg.read('config.ini')
        self.url = cfg['DEFAULT']['URL']

        self.titles = []
        self.employers = []
        self.locations = []

    def checkUpdate(self):
        # Make a GET request to the webpage
        response = requests.get(self.url,headers=headers)
        
        self.titles = []
        self.employers = []
        self.locations = []
        
        if response.ok:
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            try:
                # Find all job listings and store them in a list
                job_table = soup.find('table', {'border': '2', 'cellpadding': '5', 'width': '100%'})
                job_listings = job_table.find_all('tr')
          
                # Iterate over the list of job listings
                for job_rows in job_listings:
                    job = job_rows.find_all('td')[0]
        
                    # Extract the job title
                    title = job.find('b').text
        
                    # Extract the employer and location of the job 
                    employer = job.find('i').text
                    location = job.text.split("\n")[3].lstrip()
                    #date = job.find('font').text.split(',')[1].strip()
        
                    # Print the job listing information
                    #print(f"Title: {title}\nEmployer: {employer}\nLocation: {location}\n")
        
                    # Put resuts to list
                    self.titles.append(title)
                    self.employers.append(employer)
                    self.locations.append(location)
            except AttributeError as e:
                self.titles.append("Request Error: Empty")
                self.employers.append("Request Error: Empty")
                self.locations.append("Request Error: Empty")

            return True
        else:
            # Handle the response error
            self.titles.append("Url Request Error")
            self.employers.append("Url Request Error")
            self.locations.append("Request Error")
            return False
