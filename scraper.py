import csv
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Navigate to the about page
    page.goto("https://www.canoo.com/about/")
    page.wait_for_load_state()  # Wait for navigation to complete
    about_us = page.query_selector(
        f'//*[@id="gatsby-focus-wrapper"]/div/div/main/div/section[2]/div[1]').text_content()
    print(about_us)
    
    # Navigate to the Wikipedia page
    page.goto("https://en.wikipedia.org/wiki/Canoo")
    page.wait_for_load_state()  # Wait for navigation to complete
    about_wiki = page.query_selector(
        f'//*[@id="mw-content-text"]/div[1]/p[3]').text_content()
    print(about_wiki)
    
#######
    # Industry in which operates
    page.goto("https://tracxn.com/d/companies/canoo/__HfVDFR8zT4sJ0XU0CVBHJ1P1CTyblbW8viNKwk579vE#:~:text=What%20sectors%20and%20market%20segments,Tech%2C%20Environment%20Tech%20market%20segments.")
    page.wait_for_load_state()  # Wait for navigation to complete
    Industries = page.query_selector(
        f'//*[@id="__next"]/div/main/div/article/article/div[1]/section[2]/div[2]').text_content()
    print("inuds: ", Industries)
#######
    page.goto("https://www.fortunebusinessinsights.com/industry-reports/electric-vehicle-market-101678")
    page.wait_for_load_state()  # Wait for navigation to complete
    Key_market_size = page.query_selector(
        f'//*[@id="summury-sub"]/p[1]').text_content()
    print("Key market",Key_market_size)
    
########    
    page.goto("https://www.alliedmarketresearch.com/electric-vehicle-market")
    page.wait_for_load_state()  # Wait for navigation to complete
    growth_rate_and_trends = page.query_selector(
        f'//*[@id="report-overview"]/p[1]').text_content()  
    print(growth_rate_and_trends)
    
    page.goto("https://www.mordorintelligence.com/industry-reports/electric-vehicle-parts-and-components-market")
    page.wait_for_load_state()  # Wait for navigation to complete
    key_players = page.query_selector(
        f'//*[@id="component-4"]/div[1]/ul/li[5]').text_content() 
    print(key_players)

############
    page.goto("https://www.globaldata.com/company-profile/canoo-inc/competitors/?scalar=true&pid=45659&sid=29")
    page.wait_for_load_state()  # Wait for navigation to complete
    competitors = page.query_selector(
        f'/html/body/main/div[2]/div/div[2]/div[2]/div[2]/div').text_content()
    print(competitors)

############ 
    page.goto("https://www.iea.org/reports/global-ev-outlook-2021/trends-and-developments-in-electric-vehicle-markets")
    page.wait_for_load_state()  # Wait for navigation to complete
    trends_and_devlopment = page.query_selector(
        f'//*[@id="content"]/div[6]/div[7]/div/div[2]').text_content()    
    print(trends_and_devlopment)
#############
    page.goto("https://www.prnewswire.com/news-releases/canoo-inc-announces-second-quarter-2023-results-301900170.html")
    page.wait_for_load_state()  # Wait for navigation to complete
    canoos_financial_performance = page.query_selector(
        f'//*[@id="main"]/article/section/div/div/ul[3]').text_content()
    print(canoos_financial_performance)

    print( Key_market_size, growth_rate_and_trends, key_players, trends_and_devlopment)

    context.close()
    browser.close()
    
    # Write the data to a CSV file
    with open('about_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write header row
        writer.writerow(['Source', 'Content'])
        # Write data rows
        writer.writerow(['About Us', about_us])
        writer.writerow(['About Wiki', about_wiki])
        writer.writerow(['key market size', Key_market_size])

        writer.writerow(['Growth rate and trends', growth_rate_and_trends])
        writer.writerow(['Trends and devlopment', trends_and_devlopment])
        writer.writerow(['canoos financial performance', canoos_financial_performance])

with sync_playwright() as playwright:
    run(playwright)
