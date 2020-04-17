import argparse
import os

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import json

from JobParser import settings


def parsing():
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", action='store',
                        dest="verbose",
                        type=bool,
                        default=False,
                        help="Set verbose True/False")

    parser.add_argument("-o", action="store",
                        default="",
                        type=str,
                        dest="file_path",
                        help="JSON file path to store results")

    parser.add_argument("-u", action="store",
                        default="",
                        type=str,
                        required=True,
                        dest="url",
                        help="URL to start scraping")
    parser.add_argument('-l',
                        type=int,
                        dest="url",
                        help='provide number parsed posts')
    return parser.parse_args()


def get_jobs_glassdoor(num_jobs, verbose):
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''

    # Initializing the webdriver
    options = webdriver.ChromeOptions()

    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')

    # Change the path to where chromedriver is in your home folder.
    # Mac chromedriver
    # chrome_driver_path = os.path.join(settings.BASE_DIR, 'chromedriver_2')
    # Windows chromedriver
    chrome_driver_path = os.path.join(settings.BASE_DIR, 'chromedriver.exe')

    driver = webdriver.Chrome(
        executable_path=chrome_driver_path,
        options=options)
    driver.set_window_size(1120, 1000)

    url = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=N&locId=142&jobType='
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  # If true, should be still looking for new jobs.

        # Let the page load. Change this number based on your internet speed.
        # Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(2)

        # Test for the "Sign Up" prompt and get rid of it.
        try:
            driver.find_element_by_class_name("selected").click()
        except ElementClickInterceptedException:
            pass

        time.sleep(1)

        try:
            driver.find_element_by_class_name("modal_closeIcon-svg").click()  # clicking to the X.
        except NoSuchElementException:
            pass

        # Going through each job in this page
        job_buttons = driver.find_elements_by_class_name(
            "jl")  # jl for Job Listing. These are the buttons we're going to click.
        for job_button in job_buttons:

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click()  # You might
            time.sleep(1)
            collected_successfully = False

            while not collected_successfully:
                try:
                    company_name = driver.find_element_by_xpath('.//div[@class="employerName"]').text
                    location = driver.find_element_by_xpath('.//div[@class="location"]').text
                    job_title = driver.find_element_by_xpath('.//div[contains(@class, "title")]').text
                    job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                    collected_successfully = True
                except:
                    time.sleep(3)

            try:
                salary_estimate = driver.find_element_by_xpath('.//span[@class="gray small salary"]').text
            except NoSuchElementException:
                salary_estimate = -1  # You need to set a "not found value. It's important."

            try:
                rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
            except NoSuchElementException:
                rating = -1  # You need to set a "not found value. It's important."

            # Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            # Going to the Company tab...
            # clicking on this:
            # <div class="tab" data-tab-type="overview"><span>Company</span></div>
            try:
                driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()

                try:
                    # <div class="infoEntity">
                    #    <label>Headquarters</label>
                    #    <span class="value">San Francisco, CA</span>
                    # </div>
                    headquarters = driver.find_element_by_xpath(
                        './/div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
                except NoSuchElementException:
                    headquarters = -1

                try:
                    size = driver.find_element_by_xpath(
                        './/div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
                except NoSuchElementException:
                    size = -1

                try:
                    founded = driver.find_element_by_xpath(
                        './/div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
                except NoSuchElementException:
                    founded = -1

                try:
                    type_of_ownership = driver.find_element_by_xpath(
                        './/div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
                except NoSuchElementException:
                    type_of_ownership = -1

                try:
                    industry = driver.find_element_by_xpath(
                        './/div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
                except NoSuchElementException:
                    industry = -1

                try:
                    sector = driver.find_element_by_xpath(
                        './/div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
                except NoSuchElementException:
                    sector = -1

                try:
                    revenue = driver.find_element_by_xpath(
                        './/div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
                except NoSuchElementException:
                    revenue = -1

                try:
                    competitors = driver.find_element_by_xpath(
                        './/div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
                except NoSuchElementException:
                    competitors = -1

            except NoSuchElementException:  # Rarely, some job postings do not have the "Company" tab.
                headquarters = -1
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1
                competitors = -1

            if verbose:
                print("Headquarters: {}".format(headquarters))
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("Competitors: {}".format(competitors))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title": job_title,
                         "Salary Estimate": salary_estimate,
                         "Job Description": job_description,
                         "Rating": rating,
                         "Company Name": company_name,
                         "Location": location,
                         "Headquarters": headquarters,
                         "Size": size,
                         "Founded": founded,
                         "Type of ownership": type_of_ownership,
                         "Industry": industry,
                         "Sector": sector,
                         "Revenue": revenue,
                         "Competitors": competitors})
            # add job to jobs

        # Clicking on the "next page" button
        try:
            driver.find_element_by_xpath('.//li[@class="next"]//a').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs,
                                                                                                         len(jobs)))
            break

    return jobs

def get_jobs_stepstone(num_jobs, verbose):
    options = webdriver.ChromeOptions()
    # Free proxy from https://free-proxy-list.net/
    options.add_argument('--proxy-server=154.16.202.22:8080')


    # TO_FIX: take out from function
    # Change the path to where chromedriver is in your home folder.
    # Mac chromedriver
    # chrome_driver_path = os.path.join(settings.BASE_DIR, 'chromedriver_2')
    # Windows chromedriver
    chrome_driver_path = os.path.join(settings.BASE_DIR, 'chromedriver.exe')

    driver = webdriver.Chrome(
        executable_path=chrome_driver_path,
        options=options)
    driver.set_window_size(1120, 1000)

    url = 'https://www.stepstone.de/5/job-search-simple.html'
    driver.get(url)
    jobs = []
    while len(jobs) < num_jobs:
        time.sleep(1)

        job_list = driver.find_elements_by_class_name(
            "styled__TitleWrapper-sc-7z1cau-1")
        
        for job_link in job_list:
            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_link.click() 
            time.sleep(4)
            collected_successfully = False

            try:
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/div[4]/div/div/div/div/a/span/svg").click()
            except NoSuchElementException:
                pass

            while not collected_successfully:
                try:
                    company_name = driver.find_elements_by_class_name("at-listing-nav-company-name-link")
                    #print('company_name', company_name)
                    #location = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[3]/ul/li[2]/a/span[2]').text
                    location = driver.find_elements_by_class_name('listing-list at-listing__list-icons_location')
                    #print('location', location)
                    job_title = driver.find_element_by_xpath('.//h1[contains(@class, "listing__job-title")]').text
                    #print('job title', job_title)
                    #job_description = driver.find_element_by_xpath('.//div[@class="jjs-app-ld-ContentBlock"]').text
                    job_description = driver.find_elements_by_class_name('js-app-ld-ContentBlock')
                    #print('job desc', job_description)
                    collected_successfully = True

                except:
                    time.sleep(3)
            #return []

    return []