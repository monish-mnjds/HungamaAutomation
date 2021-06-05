"""
Automation Script for adding the song to playlist
"""
from appium.webdriver.common.touch_action import TouchAction
from Library.config import Config
from Library.web_utilities import CommonUtility
from Library.file_library import ReadJson
from Pages.automate_hungama2 import Wishlist

read_json = ReadJson()
com_util = CommonUtility()
element = read_json.read_locators(Config.OBJECT_JSON)


class Playlist(Wishlist):
    """
    add a song to the playlist
    """
    def __init__(self, driver, playlist, track,
                 email, password, song,
                 label, music, artist, lyricist):
        self.playlist = playlist
        self.track = track
        super().__init__(driver, email, password, song)
        self.label = label
        self.music = music
        self.artist = artist
        self.lyricist = lyricist

    def enter_the_playlist(self):
        """
        entering the song in the field
        """
        com_util.send_to(self.driver, element['SearchBox'], self.playlist)

    def swipe_down(self):
        """
        scrolling down
        """
        com_util.swipe_it(self.driver, element['PlaylistImage'], element['TitleHeader'])

    def click_on_track(self):
        """
        waiting for the track to display
        """
        if self.track == 'Enjoy Enjaami':
            com_util.tap_on(self.driver, element['EnjoyEnjaami'])
        elif self.track == 'Inna Mylu':
            com_util.tap_on(self.driver, element['InnaMylu'])

    def click_on_disc(self):
        """
        clicking on the playing disc
        """
        com_util.tap_on(self.driver, element['Disc'])

    def click_on_pause(self):
        """
        clicking on the pause button
        """
        com_util.tap_on(self.driver, element['pause'])

    def tap_on_3dots(self):
        """
        clicking on the 3dots to get the options
        """
        com_util.tap_on(self.driver, element['3dots'])

    def click_on_view_details(self):
        """
        clicking on the view details
        """
        com_util.tap_on(self.driver, element['ViewDetails'])

    def verify_label(self):
        """
        verifying the label info
        """
        return com_util.find_text(self.driver, element['label'])

    def verify_music(self):
        """
        verifying the music info
        """
        return com_util.find_text(self.driver, element['music'])

    def verify_artist(self):
        """
        verifying the artist info
        """
        return com_util.find_text(self.driver, element['artist'])

    def verify_lyricist(self):
        """
        verifying the lyricist info
        """
        return com_util.find_text(self.driver, element['lyricist'])

    def click_login_text(self):
        """
        clicking on the login text to add the song to playlist
        """
        com_util.tap_on(self.driver, element['LoginText'])

    def swipe_right(self):
        """
        swiping towards the right
        """
        # com_util.swipe_it(self.driver, element['Shuffle'], element['Loop'])
        TouchAction(self.driver).press(x=888, y=573).move_to(x=112, y=544).release().perform()

    def swipe_left(self):
        """
        swiping towards the left
        """
        # com_util.swipe_it(self.driver, element['Loop'], element['Shuffle'])
        TouchAction(self.driver).press(x=29, y=728).move_to(x=841, y=747).release().perform()

    def click_add_playlist(self):
        """
        clicking on the add to play list
        """
        com_util.tap_on(self.driver, element['AddToPlaylist'])

    def enter_playlist_name(self):
        """
        entering the playlist name
        """
        com_util.send_to(self.driver, element['EnterThePlaylist'], 'My Songs')

    def click_on_save(self):
        """
        clicking on the save
        """
        com_util.tap_on(self.driver, element['SaveBtn'])

    def click_on_cancel(self):
        """
        clicking on the cancel
        """
        com_util.tap_on(self.driver, element['CancelBtn'])

    def click_down_arrow(self):
        """
        click on the down arrow button
        """
        com_util.tap_on(self.driver, element['DownArrow'])

    def click_on_my_playlists(self):
        """
        clicking on the my playlists button
        """
        com_util.tap_on(self.driver, element['MyPlaylist'])

    def click_on_mysongs(self):
        """
        clicking on the My Songs playlist
        """
        com_util.tap_on(self.driver, element['ClickMySongs'])

    def check_added(self):
        """
        checking whether the song is added to playlist
        """
        if self.track == 'Enjoy Enjaami':
            option = element['EnjoyEnjaami']
        elif self.track == 'Inna Mylu':
            option = element['InnaMylu']
        return com_util.find_text(self.driver, option)

    def click_on_music(self):
        """
        clicking on the music icon
        """
        com_util.tap_on(self.driver, element['Music'])
