import pytest

from page_object_project_gigi.pages.video_page import jwVideoPage
from page_object_project_gigi.tests.conftest import setup_jw_org
from page_object_project_gigi.tests.data_file import section_test_cases, AVAILABLE_LANGUAGES


class TestVideoPage:

    @pytest.mark.parametrize("category_name, expected_url", section_test_cases)
    def test_video_categories(self, setup_jw_org, category_name, expected_url):
        video_page = jwVideoPage(setup_jw_org)
        current_category = video_page.get_video_category_by_name_(category_name)
        current_url = video_page.click_and_get_url_of_(current_category)
        assert current_url == expected_url, f"Category - {category_name} is expected to lead to - {expected_url}\nOn fact it is leading to {current_url}"

    @pytest.mark.parametrize("language, expected_result", AVAILABLE_LANGUAGES)
    def test_video_language_dropdown(self, setup_jw_org, language, expected_result):
        video_page = jwVideoPage(setup_jw_org)
        is_language_found = video_page.in_language_dropdown_search_for_(language)
        assert is_language_found == expected_result, f"Language {language} not acting as expected"

    def test_share_button(self, setup_jw_org):
        video_page = jwVideoPage(setup_jw_org)
        video_page.click_share_button()
        featured_link = video_page.get_featured_link()
        copied_link = video_page.get_result_after_clicking_copy_button()
        assert copied_link == featured_link, f"copied link - {copied_link} not matching featured link - {featured_link}"
