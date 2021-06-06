"""
Module to drive data from json file
"""
import json


class ReadJson:
    """
    class to read object and test data
    """
    @staticmethod
    def read_locators(filelocation):
        """
        loading the object data
        """
        with open(filelocation) as file:
            json_obj = json.load(file)
            dict_ = {}
            for key, value in json_obj.items():
                dict_[key] = (value['locatorType'], value['locatorValue'])
        return dict_

    @staticmethod
    def read_with_unpacking(file):
        """
        loading the test data
        """
        with open(file) as fileobj:
            j_obj = json.load(fileobj)
            data1 = [(value['Email'], value['Password'])
                    for key, value in j_obj.items()]
            data2 = [(value['Email'], value['Password'], value['Song'])
                     for key, value in j_obj.items()]
            data3 = [(value['Email'], value['Password'],
                      value['Playlist'], value['Track'], value['Label'],
                      value['Music'], value['Artist'], value['Lyricist'])
                     for key, value in j_obj.items()]
            data4 = [(value['Email'], value['Password'],
                      value['Playlist'], value['Track'])
                     for key, value in j_obj.items()]
        return data1, data2, data3, data4