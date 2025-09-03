import re


class jwMeetingPage:
    def __init__(self, page):
        self.page = page
        self.go_to_meeting_page()

    def go_to_meeting_page(self):
        self.page.goto("https://apps.jw.org/ui/E/meeting-search.html#/weekly-meetings")

    def search_for_(self, input_value):
        # Fill search Field with desired text
        search_field = self.page.locator("#searchLocation")
        search_field.fill(input_value)

    def is_result(self, item_text):
        # Wait for the page to finish loading
        self.page.wait_for_load_state("networkidle")
        # Possible search result variations
        possible_results = [
            item_text,
            self.alternate_search_result_keep_just_text(item_text),
            self.alternate_search_result_capitalaize(item_text)
        ]
        # Check each variant for matching elements on the page
        for result in possible_results:
            matching_elements = self.page.query_selector_all(f"text={result}")
            if matching_elements:  # Equals to len(result_objects_on_site) > 0
                return True
        # No matches found
        return False

    @staticmethod
    def alternate_search_result_keep_just_text(input_value):
        # Replace all non-alphanumeric characters with a space
        cleaned = re.sub(r'[^a-zA-Z]', ' ', input_value)

        # Collapse multiple spaces and trim
        return ' '.join(cleaned.split())

    @staticmethod
    def alternate_search_result_capitalaize(input_value):
        # Split the input string into individual words - ['tel', 'aviv']
        words = input_value.split()

        # Capitalize the first letter of each word - ['Tel', 'Aviv']
        capitalized_words = [word.capitalize() for word in words]

        # Join the capitalized words back into a single string - "Tel Aviv"
        result = ' '.join(capitalized_words)
        return result

    def if_correct_tab_shown_after_clicking_(self, current_tab_name):
        # Checks (True/False) if correct tab is chosen
        visible_name = current_tab_name.split(' ')[1]
        self.click_tab_(visible_name)
        tab_title = self.page.get_by_text(visible_name)
        return tab_title.count() == 3  # On Page if correct Tab is selected it will find 3 elements, otherwise only 1 element is found

    def click_tab_(self, visible_name):
        # Click tab that has that name
        tab = self.page.get_by_text(visible_name).first
        tab.click()
