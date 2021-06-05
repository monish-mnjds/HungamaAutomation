"""
Module for testing adding the song to playlist and validating
"""
import pytest
from Pages.playlist import Playlist
from Library.config import Config
from Library.file_library import ReadJson
from Library.base_fixtures import DriverInit

ReadTestData = ReadJson()
test_data1, test_data2, test_data3, test_data4 = ReadTestData.read_test_data(Config.TEST_JSON)


@pytest.mark.parametrize(
    """email, password, playlist, track""",
    test_data4
)
@pytest.mark.playlist
class TestPlaylist(DriverInit):
    """
    Testing the adding a song to playlist and validating it
    """
    def testing_playlist(self, email, password, playlist, track):
        """
        checking the song is added or not
        """
        create_playlist = Playlist(self.driver, email, password, playlist, track)
        create_playlist.open_login_page()
        create_playlist.set_user_inputs()
        create_playlist.open_home_page()
        create_playlist.select_a_random_playlist()
        create_playlist.open_the_music_page()
        create_playlist.add_the_song_to_playlist()
        create_playlist.open_my_playlist()
        assert create_playlist.validate_song_is_added_to_playlist() == track, 'Not the track'
