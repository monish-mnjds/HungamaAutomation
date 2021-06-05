"""
Automation Script for adding the song to wishlist
"""
from Library.config import Config
from Library.web_utilities import CommonUtility
from Library.file_library import ReadJson
from Pages.automate_hungama import Hungama

read_json = ReadJson()
com_util = CommonUtility()
element = read_json.read_locators(Config.OBJECT_JSON)


class Wishlist(Hungama):
    """
    add a song to the wishlist
    """
    def __init__(self, driver, email, password, song):
        self.song = song
        super().__init__(driver, email, password)

    def click_on_search_icon(self):
        """
        clicking on the search icon
        """
        com_util.tap_on(self.driver, element['clickOnSearchIcon'])

    def enter_the_song(self):
        """
        entering the song in the field
        """
        com_util.send_to(self.driver, element['SearchBox'], self.song)

    def entering(self):
        """
        Enter
        """
        com_util.send_and_enter(self.driver)

    def click_the_song(self):
        """
        clicking on the song
        """
        com_util.tap_on(self.driver, element['clickOnSong'])

    def displaying_or_not(self):
        """
        is_displayed()
        """
        return com_util.check_display(self.driver, element['TrackName'])

    def add_2_wishlist(self):
        """
        adding the song to wishlist
        """
        verify = com_util.check_select(self.driver, element['Wishlist'])
        if not verify:
            com_util.tap_on(self.driver, element['Wishlist'])

    def click_on_my_music(self):
        """
        clicking on the My Music Icon
        """
        com_util.tap_on(self.driver, element['MyMusic'])

    def click_on_fav(self):
        """
        clicking on favourites button
        """
        com_util.tap_on(self.driver, element['FavouritesBtn'])

    def click_on_albums(self):
        """
        clicking on the albums
        """
        com_util.tap_on(self.driver, element['ClickOnAlbums'])

    def check_the_song(self):
        """
        checking the added song is Correct
        """
        if self.song == 'Lahore':
            option = element['SongCheck']
        elif self.song == 'Suicide':
            option = element['SongCheck1']
        return com_util.find_text(self.driver, option)
