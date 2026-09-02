from datetime import datetime
from os.path import dirname, join

from city_scrapers_core.constants import BOARD
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.ind_housing_boc import IndHousingBocSpider

upcoming_response = file_response(
    join(dirname(__file__), "files", "ind_housing_boc_upcoming.html"),
    url="https://www.indyhousing.org/calendar/boc-meeting-september-15-2026",
)
archive_response = file_response(
    join(dirname(__file__), "files", "ind_housing_boc_archive.html"),
    url="https://www.indyhousing.org/news-archives/board-of-commissioners-meeting-february-2026",  # noqa
)
spider = IndHousingBocSpider()

freezer = freeze_time("2026-08-31")
freezer.start()

upcoming_items = [item for item in spider.parse(upcoming_response)]
archive_items = [item for item in spider.parse(archive_response)]

freezer.stop()


def test_upcoming_title():
    assert upcoming_items[0]["title"] == "BOC Meeting"


def test_upcoming_description():
    assert upcoming_items[0]["description"] == ""


def test_upcoming_start():
    assert upcoming_items[0]["start"] == datetime(2026, 9, 15, 13, 0)


def test_upcoming_end():
    assert upcoming_items[0]["end"] is None


def test_upcoming_time_notes():
    assert upcoming_items[0]["time_notes"] == ""


def test_upcoming_id():
    assert upcoming_items[0]["id"] == "ind_housing_boc/202609151300/x/boc_meeting"


def test_upcoming_status():
    assert upcoming_items[0]["status"] == "tentative"


def test_upcoming_location():
    assert upcoming_items[0]["location"] == {
        "name": "Indianapolis Housing Agency",
        "address": "1935 N. Meridian Street, Indianapolis, IN 46202",
    }


def test_upcoming_source():
    assert (
        upcoming_items[0]["source"]
        == "https://www.indyhousing.org/calendar/boc-meeting-september-15-2026"
    )


def test_upcoming_links():
    assert upcoming_items[0]["links"] == [
        {
            "href": "https://www.indyhousing.org/calendar/boc-meeting-september-15-2026",  # noqa
            "title": "Meeting Attachment",
        }
    ]


def test_upcoming_classification():
    assert upcoming_items[0]["classification"] == BOARD


def test_upcoming_all_day():
    assert upcoming_items[0]["all_day"] is False


def test_archive_title():
    assert archive_items[0]["title"] == "Board of Commissioners Meeting"


def test_archive_description():
    assert archive_items[0]["description"] == ""


def test_archive_start():
    assert archive_items[0]["start"] == datetime(2026, 2, 17, 13, 0)


def test_archive_end():
    assert archive_items[0]["end"] is None


def test_archive_time_notes():
    assert archive_items[0]["time_notes"] == ""


def test_archive_id():
    assert (
        archive_items[0]["id"]
        == "ind_housing_boc/202602171300/x/board_of_commissioners_meeting"
    )


def test_archive_status():
    assert archive_items[0]["status"] == "passed"


def test_archive_location():
    assert archive_items[0]["location"] == {
        "name": "Indianapolis Housing Agency",
        "address": "1935 N. Meridian Street, Indianapolis, IN 46202",
    }


def test_archive_source():
    assert (
        archive_items[0]["source"]
        == "https://www.indyhousing.org/news-archives/board-of-commissioners-meeting-february-2026"  # noqa
    )


def test_archive_links():
    assert archive_items[0]["links"] == [
        {
            "href": "https://www.indyhousing.org/news-archives/board-of-commissioners-meeting-february-2026",  # noqa
            "title": "Meeting Attachment",
        }
    ]


def test_archive_classification():
    assert archive_items[0]["classification"] == BOARD


def test_archive_all_day():
    assert archive_items[0]["all_day"] is False
