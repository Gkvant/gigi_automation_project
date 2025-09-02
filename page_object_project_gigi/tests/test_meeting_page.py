import time

import pytest

from page_object_project_gigi.pages.meeting_page import jwMeetingPage
from page_object_project_gigi.tests.conftest import setup_jw_org


class TestMeetingPage:
    @pytest.mark.parametrize("search_term, expected_result", [
        ("tel-aviv", True),
        ("Tel-aviv", True),
        ("Tel-Aviv", True),
        ("tel aviv", True),
        ("Haifa", True),
        ("Holon", True),
        ("asdfgh", False),
        ("Fictional City", False)
    ])
    def test_search_result(self, setup_jw_org, search_term, expected_result):
        meeting_page = jwMeetingPage(setup_jw_org)
        meeting_page.search_for_(search_term)
        search_result = meeting_page.is_result(search_term)
        assert search_result == expected_result, f"Search term {search_term} caused wrong behavior"

    def test_weekly_meetings_tab(self, setup_jw_org):
        meetings_tab = "Weekly Meetings"
        meeting_page = jwMeetingPage(setup_jw_org)
        is_correct_tab_shown = meeting_page.if_correct_tab_shown_after_clicking_(meetings_tab)
        assert is_correct_tab_shown, f"Meetings Tab not showing up after click"

    def test_regional_conventions_tab(self, setup_jw_org):
        conventions_tab = "Regional Conventions"
        meeting_page = jwMeetingPage(setup_jw_org)
        is_correct_tab_shown = meeting_page.if_correct_tab_shown_after_clicking_(conventions_tab)
        assert is_correct_tab_shown, f"Conventions Tab not showing up after click"

    def test_circuit_assemblies_tab(self, setup_jw_org):
        assembly_tab = "Circuit Assemblies"
        meeting_page = jwMeetingPage(setup_jw_org)
        is_correct_tab_shown = meeting_page.if_correct_tab_shown_after_clicking_(assembly_tab)
        assert is_correct_tab_shown, f"Assemblies Tab not showing up after click"
