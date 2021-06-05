"""
Automation Script for viewing the details
"""
from Library.config import Config
from Library.web_utilities import CommonUtility
from Library.file_library import ReadJson
from Pages.basepage import BasePage

read_json = ReadJson()
com_util = CommonUtility()
element = read_json.read_locators(Config.OBJECT_JSON)


class ViewDetails(BasePage):
    """
    View the details of the song and validate
    """
    def __init__(self, driver, email, password, playlist, track,):
        self.playlist = playlist
        self.track = track
        super().__init__(driver, email, password)

    def select_a_random_playlist(self):
        """
        search a trending playlist and open the playlist
        """
        com_util.tap_on(self.driver, element['clickOnSearchIcon'])
        com_util.send_to(self.driver, element['SearchBox'], self.playlist)
        com_util.send_and_enter(self.driver)
        com_util.tap_on(self.driver, element['clickOnSong'])

    def open_the_music_page(self):
        """
        After swiping down, select the song and open the music page
        then click on pause btn
        """
        com_util.swipe_it(self.driver, element['PlaylistImage'], element['TitleHeader'])
        if self.track == 'Enjoy Enjaami':
            com_util.tap_on(self.driver, element['EnjoyEnjaami'])
        elif self.track == 'Inna Mylu':
            com_util.tap_on(self.driver, element['InnaMylu'])
        com_util.tap_on(self.driver, element['Disc'])
        com_util.tap_on(self.driver, element['pause'])

    def view_the_details_and_validate(self):
        """
        click on the 3 vertical dots and click on
        the view details to validate
        """
        com_util.tap_on(self.driver, element['3dots'])
        com_util.tap_on(self.driver, element['ViewDetails'])

    def validate_the_label_name(self):
        """
        verifying the label info
        """
        return com_util.find_text(self.driver, element['label'])

    def validate_the_music_name(self):
        """
        verifying the music info
        """
        return com_util.find_text(self.driver, element['music'])

    def validate_the_artist_name(self):
        """
        verifying the artist info
        """
        return com_util.find_text(self.driver, element['artist'])

    def validate_the_lyricist_name(self):
        """
        verifying the lyricist info
        """
        return com_util.find_text(self.driver, element['lyricist'])
