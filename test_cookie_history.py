import unittest
from CookieHistory import CookieHistory

class TestCookieHistory(unittest.TestCase):

    # sample file of csv
    SAMPLE_CSV = "cookie_log.csv"

    COOKIE_DICT = {
        '2018-12-07' : {'4sMM2LxV07bPJzwf' : 1},
        '2018-12-08' : {
            'fbcn5UAVanZf6UtG' : 1,
            '4sMM2LxV07bPJzwf' : 1,
            'SAZuXPGUrfbcn5UA' : 1,
        },
        '2018-12-09' : {
            'AtY0laUfhglK3lC7' : 2,
            '5UAVanZf6UtGyKVS' : 1,
            'SAZuXPGUrfbcn5UA' : 1,
        },
    }

    def test_cookieLogDict(self):
        """ Testing CookieHistory's data structure (dict) """
        # want to see if the cookie has the right frequency,
        # based on their visitation date.
        ch = CookieHistory(self.SAMPLE_CSV)
        self.assertEqual(self.COOKIE_DICT, ch.cookie_log_dict)
        pass


    def test_lookForMostActive(self):
        """ Testing lookForMostActive method """
        # want to see if we're able to get the correct
        # most active cookies based on their respective date.

        ch = CookieHistory(self.SAMPLE_CSV)

        date1 = '2018-12-07'
        date2 = '2018-12-08'
        date3 = '2018-12-09'

        expected_result1 = ['4sMM2LxV07bPJzwf']
        expected_result2 = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
        expected_result3 = ['AtY0laUfhglK3lC7']

        actual_result1 = ch.lookForMostActive(date1)
        actual_result2 = ch.lookForMostActive(date2)
        actual_result3 = ch.lookForMostActive(date3)

        self.assertItemsEqual(actual_result1, expected_result1)
        self.assertItemsEqual(actual_result2, expected_result2)
        self.assertItemsEqual(actual_result3, expected_result3)
        pass




if __name__ == '__main__':
    unittest.main()
