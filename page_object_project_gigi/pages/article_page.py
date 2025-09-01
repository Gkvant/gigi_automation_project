import time


class jwArticlePage:
    def __init__(self, page):
        self.page = page

    def navigate_to_science_articles(self):
        self.page.goto("https://www.jw.org/en/bible-teachings/science/")

    def navigate_to_bible_articles(self):
        self.page.goto("https://www.jw.org/en/bible-teachings/questions/")

    def navigate_to_happiness_articles(self):
        self.page.goto("https://www.jw.org/en/bible-teachings/peace-happiness/")

    def navigate_to_teen_articles(self):
        self.page.goto("https://www.jw.org/en/bible-teachings/teenagers/")

    def navigate_to_faith_articles(self):
        self.page.goto("https://www.jw.org/en/bible-teachings/faith-in-god/")

    def navigate_to_history_articles(self):
        self.page.goto("https://www.jw.org/en/bible-teachings/history/")

    def navigate_to_family_articles(self):
        self.page.goto("https://www.jw.org/en/bible-teachings/family/")

    def get_see_all_buttons(self):
        return self.page.query_selector_all(".sect-syn-header-button")

    def get_header_text(self):
        self.page.wait_for_selector("h1")
        return self.page.query_selector("h1").inner_text()

    def get_item_by_(self, name):
        return self.page.locator("a", has_text=name)

    def click_see_all_button_number_(self, index):
        see_all_buttons = self.get_see_all_buttons()
        button = see_all_buttons[index]
        button.click()
