'''   A module comprising of test set for pricing

We will be testing various points in github pricing tab.

This module will automate all the manual test cases written
in the pricing test set.

'''
# By.XPATH
# By.ID
# By.CLASS-NAME
# By.TAG_NAME
# By.NAME
# By.CSS_SELECTOR

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


def pricing_click_link():
    'docstring'

    with open('github_pricing_test_set.log', 'a', encoding='utf-8') as github_log_file:
        github_log_file.write(f'Test started at: {datetime.now()} \n')

        github_log_file.write('Opening Edge Browser Instance ... \n')
        browser_chrome = webdriver.Chrome()

        github_log_file.write('Opening www.Github.com ... \n')
        browser_chrome.get('https://www.github.com')

        github_log_file.write(
            'Targeting Pricing Click Link On Main Menu ... \n')
        pricing_link = browser_chrome.find_element(
            By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[4]/a')

        github_log_file.write('Clicking on Pricing Link... \n')
        pricing_link.click()
        github_log_file.write('Closing Chrome Browser Instance... \n')
        browser_chrome.quit()
        github_log_file.write('Chrome Browser Instance Closed... \n\n')


pricing_click_link()
