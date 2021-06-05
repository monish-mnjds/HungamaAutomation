"""
Module for test scripts of Hungama
"""
import pytest
from Pages.automate_hungama import Hungama
from Pages.automate_hungama2 import Wishlist
from Pages.automate_hungama3 import Playlist
from Library.config import Config
from Library.file_library import ReadJson
from Library.base_fixtures import DriverInit

ReadTestData = ReadJson()
test_data = ReadTestData.read_test_data(Config.TEST_JSON)


@pytest.mark.parametrize(
    """email, password, song, playlist, track, label, music, artist, lyricist""",
    test_data
)
@pytest.mark.tc1
class TestHungama(DriverInit):
    """
    Testing the automation Scripts
    """
    def testing_hungama(self, email, password, song,
                        playlist, track, label,
                        music, artist, lyricist):
        """
        Running all the tests from Pages
        """
        hungama = Hungama(self.driver, email, password)
        hungama.click_on_at()
        hungama.enter_email()
        hungama.enter_password()
        hungama.click_on_login()
        hungama.wait_to_load()
        hungama.click_on_continue()

        wishlist = Wishlist(self.driver, email, password, song)
        wishlist.click_on_search_icon()
        wishlist.enter_the_song()
        wishlist.entering()
        wishlist.click_the_song()
        assert wishlist.displaying_or_not() is True, 'Song is not displaying'
        wishlist.add_2_wishlist()
        wishlist.click_on_my_music()
        wishlist.click_on_fav()
        wishlist.click_on_albums()
        assert wishlist.check_the_song() == song, 'This is not the song'

        play = Playlist(self.driver, playlist, track,
                             email, password, song, label,
                             music, artist, lyricist)
        play.click_on_search_icon()
        play.enter_the_playlist()
        play.entering()
        play.click_the_song()
        play.swipe_down()
        play.click_on_track()
        play.click_on_disc()
        play.click_on_pause()
        play.tap_on_3dots()
        play.click_on_view_details()
        assert play.verify_label() == label, "Not the label"
        assert play.verify_music() == music, 'Not the music'
        assert play.verify_artist() == artist, "Not the artist"
        assert play.verify_lyricist() == lyricist, "Not the lyricist"
        play.click_on_disc()
        play.click_add_playlist()
        # play.enter_playlist_name()
        play.click_on_mysongs()
        # play.click_on_save()
        play.click_on_cancel()
        play.click_down_arrow()
        play.click_on_my_music()
        play.click_on_my_playlists()
        play.click_on_mysongs()
        assert play.check_added() == track, "Not the track"
        play.click_on_music()
        play.swipe_left()
        play.swipe_right()
        play.click_on_profile()
        play.click_on_more()
        play.click_on_logout()
        play.click_on_yes()
