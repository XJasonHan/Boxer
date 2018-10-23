class HandleCookies:
    @staticmethod
    def dict():
        re_data = {}
        with open('Raw_Cookies', 'r') as file:
            d=file.read()
            split_data=d.split(';')
            for record in split_data:
                record_split=record.split('=')
                re_data[record_split[0]]=record_split[1]

        return re_data

    @staticmethod
    def get_raw():
        with open('Raw_Cookies', 'r') as file:
            raw = file.read()

        return raw


