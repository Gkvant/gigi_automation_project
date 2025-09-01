import time

from page_object_project_gigi.pages.meeting_page import jwMeetingPage
from page_object_project_gigi.tests.conftest import setup_jw_org



class TestMeetingPage:

    def test_search_meeting(self, setup_jw_org):
        meeting_page = jwMeetingPage(setup_jw_org)
        meeting_page.search_for_("Tel-Aviv")
        # time.sleep(5)