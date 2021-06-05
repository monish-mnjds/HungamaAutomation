"""
Automation Script for adding the song to playlist
"""
from Library.config import Config
from Library.web_utilities import CommonUtility
from Library.file_library import ReadJson
from Pages.view_details import ViewDetails

read_json = ReadJson()
com_util = CommonUtility()
element = read_json.read_locators(Config.OBJECT_JSON)


class Playlist(ViewDetails):
    """
    View the details of the song and validate
    """
    def __init__(self, driver, email, password, playlist, track):
        super().__init__(driver, email, password, playlist, track)

    def add_the_song_to_playlist(self):
        """
        click on add to playlist, click on the my songs playlist
        and if added already click cancel then go to main page.
        """
        com_util.tap_on(self.driver, element['AddToPlaylist'])
        # com_util.send_to(self.driver, element['EnterThePlaylist'], 'My Songs')
        com_util.tap_on(self.driver, element['ClickMySongs'])
        # com_util.tap_on(self.driver, element['SaveBtn'])
        com_util.tap_on(self.driver, element['CancelBtn'])
        com_util.tap_on(self.driver, element['DownArrow'])

    def open_my_playlist(self):
        """
        open the playlist, by clicking on the my music icon
        in the home page and select my playlist option
        """
        com_util.tap_on(self.driver, element['Music'])
        com_util.tap_on(self.driver, element['MyPlaylist'])
        com_util.tap_on(self.driver, element['ClickMySongs'])

    def validate_song_is_added_to_playlist(self):
        """
        checking whether the song is added to playlist
        """
        if self.track == 'Enjoy Enjaami':
            option = element['EnjoyEnjaami']
        elif self.track == 'Inna Mylu':
            option = element['InnaMylu']
        return com_util.find_text(self.driver, option)

