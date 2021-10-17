class CookieHistory(object):
    """
    A class used to process a log file (csv),
    and analyze their visit history

    ...

    Attributes
    ----------
    filename : str
        the csv filename we wish to open

    cookie_log_dict : dict
        key is specific date,
        and values are {cookie name : visit count}


    Methods
    -------
    processLogFile()
        processes csv file, calls countCookieVisit method
    countCookieVisit(date, cookie)
        counts all the cookies visitation
    lookForMostActive(date)
        gets the most active cookies on that date
    """

    def __init__(self, filename):
        self.filename = filename
        self.cookie_log_dict = {}
        self.processLogFile()

    def processLogFile(self):
        """ Opens a csv file given in the CLI argument """

        with open(self.filename, 'r') as csv_file:

            # skips the first line in the csv file
            next(csv_file)

            for line in csv_file:
                line = line.split(',')
                cookie_name = line[0]
                time_stamp = line[1].split('T')

                date = time_stamp[0]
                clock = time_stamp[1]
                self.countCookieVisit(date, cookie_name)

    def countCookieVisit(self, date, cookie):
        """
        counts each cookie's log frequency,
        and store them in the dictionary cookie_log_dict

        Parameters
        ----------
        date : str
            the date of when the cookie logs

        cookie : str
            cookie name or their unique character
        """
        if date in self.cookie_log_dict:
            if cookie in self.cookie_log_dict[date]:
                self.cookie_log_dict[date][cookie] += 1
            else:
                self.cookie_log_dict[date][cookie] = 1
        else:
            self.cookie_log_dict[date] = {cookie:1}


    def lookForMostActive(self, date):
        """
        finds/returns the most active cookies
        on a given day/date, then
        append those cookies into most_active_cookies.

        Parameters
        ----------
        date : str
            the log day to search in dictionary

        Return
        ---------
        most_active_cookies : [str]
            all cookies that are most active
        """

        # get all the cookies logging on that date
        all_cookies = self.cookie_log_dict[date].keys()

        # get all number of visitations of those cookies
        all_visit_times = self.cookie_log_dict[date].values()

        max_visit = max(all_visit_times)

        # we retrieve all cookies that have the max visits by index
        cookies_max_idx = [idx for idx, j in enumerate(all_visit_times) if j == max_visit]

        most_active_cookies = []

        for cookie_index in cookies_max_idx:
            cookie = all_cookies[cookie_index]
            most_active_cookies.append(cookie)
        return most_active_cookies
