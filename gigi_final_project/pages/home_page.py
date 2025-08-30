class jwHomePage:
    def __init__(self, page):
        self.page = page

    def reset_home_page(self):
        self.page.goto("https://www.jw.org/en/")

    def get_number_of_languages_that_site_is_translated(self):
        language_button = self.page.locator("[class='tertiaryButton siteFeaturesItem jsChooseSiteLanguage']")
        language_button_link = language_button.get_attribute("href")
        self.page.goto("https://www.jw.org/" + language_button_link)

        paragraph = self.page.locator("p")
        language_number = paragraph.locator("span").text_content().replace(",","")
        return int(language_number)

    def get_jw_copyright(self):
        # Returns copyright year that is on site
        jw_copyright = self.page.locator("[class='ml-E dir-ltr ms-ROMAN']")
        jw_copyright_text = jw_copyright.text_content()
        year_index = jw_copyright_text.find('2')
        return jw_copyright_text[year_index:year_index + 4]

    def get_footer_link_with_(self, name=""):
        # Returns footer locator object
        jw_footer = self.page.locator("[class='sitemapLinks']")
        if len(name) > 0:
            return jw_footer.get_by_role("link", name=str(name), exact=True)
        else:
            return jw_footer.get_by_role("link")

    def get_footer_links(self):
        # Returns all href from footer section as list
        jw_footer_links = self.get_footer_link_with_("")
        count = jw_footer_links.count()
        link_list = []
        for i in range(count):
            current_link = jw_footer_links.nth(i).get_attribute("href")
            if current_link[0] == '/':
                link_list.append("https://www.jw.org" + current_link)
            else:
                link_list.append(current_link)
        return link_list

    def get_footer_texts(self):
        # Returns all text from footer section as list
        jw_footer_links = self.get_footer_link_with_()
        count = jw_footer_links.count()
        text_list = []
        for i in range(count):
            current_text = jw_footer_links.nth(i).inner_text()
            text_list.append(current_text)
        return text_list

    def get_url_after_click(self, link):
        # Returns final URL
        link.click()
        final_url = self.page.url
        # Covers scenario of link that opens in new tab
        if link.get_attribute("target") == "_blank":
            with self.page.expect_popup() as popup:
                new_tab = popup.value
                new_tab.wait_for_load_state()
                final_url = new_tab.url
                new_tab.close()
        return final_url

    def get_about_us_text(self):
        # Returns about us text
        paragraph = self.page.locator("p#p2.disableActiveState")
        return paragraph.text_content()
