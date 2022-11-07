import requests
from bs4 import BeautifulSoup


URL = "https://www.usajobs.gov/Search/ExploreOpportunities?Series=1550"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="usajobs-opportunity__search-results-container")
#job_elements = results.find_all("div", class_="card-content")
# print(results.prettify())
job_elements = results.find_all("div", class_="usajobs-search-result--card")
for job_element in job_elements:
    title = job_element.find("h3", class_="usajobs-search-result__title")
    print(title)