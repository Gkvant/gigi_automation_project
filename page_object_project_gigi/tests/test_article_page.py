import time
import pytest
from page_object_project_gigi.pages.article_page import jwArticlePage
from page_object_project_gigi.tests.conftest import setup_jw_org
from page_object_project_gigi.tests.data_file import SCIENCE_SERIES, BIBLE_SERIES, HAPPINESS_SERIES, FAMILY_SERIES, \
    TEEN_SERIES, FAITH_SERIES, HISTORY_SERIES, SCIENCE_PUBLICATIONS


class TestArticlePage:

    @pytest.mark.parametrize("expected_article_name, index", SCIENCE_SERIES)
    def test_science_series_headers(self, setup_jw_org, expected_article_name, index):
        # Goal - Check if headers of series match actual landing page headers
        articles_page = jwArticlePage(setup_jw_org)
        articles_page.navigate_to_science_articles()
        articles_page.click_see_all_button_number_(index)
        article_name = articles_page.get_header_text()
        assert article_name == expected_article_name, f"mismatch between header-'{article_name}' and expected name-'{expected_article_name}'"

    @pytest.mark.parametrize("publication_name, expected_link", SCIENCE_PUBLICATIONS)
    def test_feature_publication_science(self, setup_jw_org, publication_name, expected_link):
        # Goal - Check if publication page matches actual landing page of that publication
        articles_page = jwArticlePage(setup_jw_org)
        articles_page.navigate_to_science_articles()
        publication = articles_page.get_item_by_(publication_name)
        publication.click()
        assert articles_page.page.url == expected_link, f"publication {publication_name} not leading to expected page: {expected_link}"

    def test_feature_publication_history(self, setup_jw_org):
        # Goal - Check if publication page matches actual landing page of that publication
        publication_name = "The Bible​—What Is Its Message?"
        expected_link = "https://www.jw.org/en/library/books/bible-message/"
        articles_page = jwArticlePage(setup_jw_org)
        articles_page.navigate_to_history_articles()
        publication = articles_page.get_item_by_(publication_name)
        publication.click()
        assert articles_page.page.url == expected_link, f"publication {publication_name} not leading to expected page: {expected_link}"

    @pytest.mark.parametrize("expected_article_name, index", BIBLE_SERIES)
    def test_bible_series_headers(self, setup_jw_org, expected_article_name, index):
        # Goal - Check if headers of series match actual landing page headers
        articles_page = jwArticlePage(setup_jw_org)
        articles_page.navigate_to_bible_articles()
        articles_page.click_see_all_button_number_(index)
        article_name = articles_page.get_header_text()
        assert article_name == expected_article_name, f"mismatch between header-'{article_name}' and expected name-'{expected_article_name}'"

    @pytest.mark.parametrize("expected_article_name, index", HAPPINESS_SERIES)
    def test_happiness_series_headers(self, setup_jw_org, expected_article_name, index):
        # Goal - Check if headers of series match actual landing page headers
        articles_page = jwArticlePage(setup_jw_org)
        articles_page.navigate_to_happiness_articles()
        articles_page.click_see_all_button_number_(index)
        article_name = articles_page.get_header_text()
        assert article_name == expected_article_name, f"mismatch between header-'{article_name}' and expected name-'{expected_article_name}'"

    @pytest.mark.parametrize("expected_article_name, index", FAMILY_SERIES)
    def test_family_series_headers(self, setup_jw_org, expected_article_name, index):
        # Goal - Check if headers of series match actual landing page headers
        articles_page = jwArticlePage(setup_jw_org)
        articles_page.navigate_to_family_articles()
        articles_page.click_see_all_button_number_(index)
        article_name = articles_page.get_header_text()
        assert article_name == expected_article_name, f"mismatch between header-'{article_name}' and expected name-'{expected_article_name}'"

    @pytest.mark.parametrize("expected_article_name, index", TEEN_SERIES)
    def test_teen_series_headers(self, setup_jw_org, expected_article_name, index):
        # Goal - Check if headers of series match actual landing page headers
        articles_page = jwArticlePage(setup_jw_org)
        articles_page.navigate_to_teen_articles()
        articles_page.click_see_all_button_number_(index)
        article_name = articles_page.get_header_text()
        assert article_name == expected_article_name, f"mismatch between header-'{article_name}' and expected name-'{expected_article_name}'"

    @pytest.mark.parametrize("expected_article_name, index", FAITH_SERIES)
    def test_faith_series_headers(self, setup_jw_org, expected_article_name, index):
        # Goal - Check if headers of series match actual landing page headers
        articles_page = jwArticlePage(setup_jw_org)
        articles_page.navigate_to_faith_articles()
        articles_page.click_see_all_button_number_(index)
        article_name = articles_page.get_header_text()
        assert article_name == expected_article_name, f"mismatch between header-'{article_name}' and expected name-'{expected_article_name}'"

    @pytest.mark.parametrize("expected_article_name, index", HISTORY_SERIES)
    def test_history_series_headers(self, setup_jw_org, expected_article_name, index):
        # Goal - Check if headers of series match actual landing page headers
        articles_page = jwArticlePage(setup_jw_org)
        articles_page.navigate_to_history_articles()
        articles_page.click_see_all_button_number_(index)
        article_name = articles_page.get_header_text()
        assert article_name == expected_article_name, f"mismatch between header-'{article_name}' and expected name-'{expected_article_name}'"
