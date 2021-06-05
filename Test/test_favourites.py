"""
Module for testing adding the song to favourites or wishlist
"""
import pytest
from Pages.favourites import Favourites
from Library.config import Config
from Library.file_library import ReadJson
from Library.base_fixtures import DriverInit

ReadTestData = ReadJson()
test_data1, test_data2, test_data3, test_data4 = ReadTestData.read_test_data(Config.TEST_JSON)


@pytest.mark.parametrize(
    """email, password, song""",
    test_data2
)
@pytest.mark.wishlist
class TestFavourites(DriverInit):
    """
    Testing the adding to fovourites
    """
    def testing_favourites(self, email, password, song):
        """
        checking the adding to favourites
        """
        add_to_favourites = Favourites(self.driver, email, password, song)
        add_to_favourites.open_login_page()
        add_to_favourites.set_user_inputs()
        add_to_favourites.open_home_page()
        add_to_favourites.selecting_a_random_song()
        assert add_to_favourites.check_the_song_is_displayed() is True, 'Song is not displaying'
        add_to_favourites.add_to_wishlist()
        add_to_favourites.go_to_favourites_page()
        assert add_to_favourites.check_the_song_is_added_to_wishlist() == song, 'Not the song'
