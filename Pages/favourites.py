"""
Automation Script for adding the song to wishlist
"""
from Library.config import Config
from Library.web_utilities import CommonUtility
from Library.file_library import ReadJson
from Pages.basepage import BasePage

read_json = ReadJson()
com_util = CommonUtility()
element = read_json.read_locators(Config.OBJECT_JSON)


class Favourites(BasePage):
    """
    add a song to the wishlist
    """
    def __init__(self, driver, email, password, song):
        self.song = song
        super().__init__(driver, email, password)

    def selecting_a_random_song(self):
        """
        click on search icon, send the song into the
        search box, and click on enter, click the
        desired song
        """
        com_util.tap_on(self.driver, element['clickOnSearchIcon'])
        com_util.send_to(self.driver, element['SearchBox'], self.song)
        com_util.send_and_enter(self.driver)
        com_util.tap_on(self.driver, element['clickOnSong'])

    def check_the_song_is_displayed(self):
        """
        Checking whether the song is displayed or not
        """
        return com_util.check_display(self.driver, element['TrackName'])

    def add_to_wishlist(self):
        """
        Check whether song is already added to wishlist
        """
        verify = com_util.check_select(self.driver, element['Wishlist'])
        if not verify:
            com_util.tap_on(self.driver, element['Wishlist'])

    def go_to_favourites_page(self):
        """
        click on My Music icon in home page, the click
        on favourites btn, click on Albums
        """
        com_util.tap_on(self.driver, element['MyMusic'])
        com_util.tap_on(self.driver, element['FavouritesBtn'])
        com_util.tap_on(self.driver, element['ClickOnAlbums'])

    def check_the_song_is_added_to_wishlist(self):
        """
        validate the song is added to wishlist
        """
        if self.song == 'Lahore':
            option = element['SongCheck']
        elif self.song == 'Suicide':
            option = element['SongCheck1']
        return com_util.find_text(self.driver, option)
