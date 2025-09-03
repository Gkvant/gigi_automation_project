
class jwVideoPage:
    def __init__(self, page):
        self.page = page
        self.go_to_video_page()

    def go_to_video_page(self):
        self.page.goto("https://www.jw.org/en/library/videos/#en/home")

    def get_video_category_by_name_(self, category_name):
        self.page.wait_for_load_state("networkidle")
        categories_panel = self.page.locator("[class='sectionSynopsis jsDirection dir-ltr']")
        return categories_panel.get_by_text(category_name, exact=True)

    def click_and_get_url_of_(self, current_category):
        current_category.click()
        return self.page.url

    def get_language_dropdown(self):
        return self.page.locator("input#mediaLanguageID")

    def in_language_dropdown_search_for_(self, language):
        self.page.wait_for_load_state("networkidle")
        dropdown = self.get_language_dropdown()
        dropdown.click()
        dropdown.fill(language)
        self.page.wait_for_load_state("networkidle")
        results = self.page.locator(".jsAutoCompleteSelector").locator(
            "li")  # If Language is found is shown in <LI> tag
        return results.count() != 0

    def click_share_button(self):
        share_button = self.page.locator("[class='secondaryButton articleShareButton']")
        share_button.click()

    def get_featured_link(self):
        field = self.page.locator("input.shareLink").nth(1)
        field_value = field.input_value()
        return field_value

    def get_result_after_clicking_copy_button(self):
        copy_button = self.page.get_by_text("Copy Link").nth(1)
        field = self.page.locator("input.shareLink").nth(1)
        copy_button.click()
        field.fill("")
        field.click()
        self.page.keyboard.press("Control+V")
        copy_value = field.input_value()
        return copy_value
