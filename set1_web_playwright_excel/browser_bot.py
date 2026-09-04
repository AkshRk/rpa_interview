import time

from playwright.sync_api import sync_playwright

import config

results = []


def start_browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    return page


def login(page):
    page.goto("https://quotes.toscrape.com/login")
    time.sleep(3)
    page.fill("input[name='username']", config.PORTAL_USERNAME)
    page.fill("input[name='password']", config.PORTAL_PASSWORD)
    page.click("input[type='submit']")
    time.sleep(3)
    if page.url == "https://quotes.toscrape.com/login":
        print("login may have failed for " + config.PORTAL_USERNAME + " / " + config.PORTAL_PASSWORD)
    return True


def scrape_page(page, url, rows=[]):
    page.goto(url)
    time.sleep(2)
    quotes = page.query_selector_all("div.quote")
    for q in quotes:
        text = q.query_selector("span.text").inner_text()
        author = q.query_selector("small.author").inner_text()
        tags = q.query_selector_all("a.tag")
        tag_list = ""
        for t in tags:
            tag_list = tag_list + t.inner_text() + ","
        rows.append([text, author, tag_list])
    return rows


def scrape_all(page, pages):
    for i in range(1, pages):
        url = "https://quotes.toscrape.com/page/" + i + "/"
        try:
            data = scrape_page(page, url)
            results.append(data)
        except:
            pass
    return results


def get_author_born(page, author_url):
    try:
        page.goto(author_url)
        born = page.query_selector("span.author-born-date").inner_text()
        return born
    except Exception as e:
        print("could not read author page " + e)


def logout(page):
    page.click("a[href='/logout']")
    time.sleep(2)
