"""
Module for testing signin and signout
"""
import pytest
from Pages.view_details import ViewDetails
from Library.config import Config
from Library.file_library import ReadJson
from Library.base_fixtures import DriverInit

ReadTestData = ReadJson()
test_data1, test_data2, test_data3, test_data4 = ReadTestData.read_test_data(Config.TEST_JSON)


@pytest.mark.parametrize(
    """email, password, playlist, track, label, music, artist, lyricist""",
    test_data3
)
@pytest.mark.verify
class TestViewDetails(DriverInit):
    """
    Testing for validation of the song's details
    """
    def testing_login(self, email, password,
                      playlist, track, label, music, artist, lyricist):
        """
        Checking the song's details
        """
        view_details = ViewDetails(self.driver, email, password, playlist, track)
        view_details.open_login_page()
        view_details.set_user_inputs()
        view_details.open_home_page()
        view_details.select_a_random_playlist()
        view_details.open_the_music_page()
        view_details.view_the_details_and_validate()
        assert view_details.validate_the_label_name() == label, "Not the label"
        assert view_details.validate_the_music_name() == music, "Not the Music"
        assert view_details.validate_the_artist_name() == artist, "Not the artist"
        assert view_details.validate_the_lyricist_name() == lyricist, "Not the lyricist"
