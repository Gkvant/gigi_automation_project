class jwMeetingPage:
    def __init__(self, page):
        self.page = page
        self.go_to_meeting_page()

    def go_to_meeting_page(self):
        self.page.goto("https://apps.jw.org/ui/E/meeting-search.html#/weekly-meetings")

    def search_for_(self, input_value):
        search_field = self.page.locator("#searchLocation")
        search_field.fill(input_value)
        first_search_result = self.page.locator("[class='autocomplete__item__link ng-isolate-scope']").first
        first_search_result.click()