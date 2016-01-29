import os
import sys
import logging
import json


class Config:
    def __create(self, dir):
        key = {'consumerKey': input('Enter your Consumer key: '),
               'consumerSecret': input('Enter your Consumer Secret: '),
               'accessToken': input('Enter your Access Token: '),
               'accessTokenSecret': input('Enter your Access Token Secret: ')
               }

        monday = ['I love Mondays', 'I cant believe its already Monday', 'It\'s Monday']
        tuesday = ['I love Tuesdays', 'I cant believe its already Tuesday', 'It\'s Tuesday']
        wednesday = ['I love Wednesdays', 'I cant believe its already Wednesday', 'It\'s Wednesday']
        thursday = ['I love Thursdays', 'I cant believe its already Thursday', 'It\'s Thursday']
        friday = ['I love Fridays', 'I cant believe its already Friday', 'It\'s Friday']
        saturday = ['I love Saturdays', 'I cant believe its already Saturday', 'It\'s Saturday']
        sunday = ['I love Sundays', 'I cant believe its already Sunday', 'It\'s Sunday']

        queue = ['last', 'fourth', 'third', 'second', 'first']

        status = {'Monday': monday,
                  'Tuesday': tuesday,
                  'Wednesday': wednesday,
                  'Thursday': thursday,
                  'Friday': friday,
                  'Saturday': saturday,
                  'Sunday': sunday}

        oldPic = ''

        fileType = 'jpeg', 'jpg', 'png', 'webp', 'gif'

        maxSize = 3

        settings = {'key': key,
                    'status': status,
                    'queue': queue,
                    'oldPic': oldPic,
                    'fileType': fileType,
                    'maxSize': maxSize}

        f = open(os.path.join(dir, 'config.json'), 'w')
        json.dump(settings, f, indent=4)
        logging.debug('Creating: ' + os.path.join(dir, 'config.json'))
        f.close()
        return settings

    def __load(self, dir):
        try:
            f = open(os.path.join(dir, 'config.json'), 'r')
            logging.debug('Opening: ' + os.path.join(dir, 'config.json'))

            try:
                settings = json.load(f)
            except:
                input('Config file corrupted.')
                f.close()
                sys.exit(1)
            f.close()
        except IOError:
            fileMade = False
            print('No config file in that location, creating one now..')
            while not fileMade:
                try:
                    settings = self.__create(dir)
                    fileMade = True

                    print('Config file created in : ' + dir)
                    print('Exit now and open the config.json file if you wish to customize your statuses.')
                    input('Otherwise continue with the defaults.')
                except:
                    dir = input('Not a valid file path, please try again: ')
        return settings

    def save(self):
        f = open(os.path.join(self.dir, 'config.json'), 'w')
        json.dump(self.settings, f, indent=3)
        f.close()

    def get_consumer_key(self):
        return self.settings['key']['consumerKey']

    def get_consumer_secret(self):
        return self.settings['key']['consumerSecret']

    def get_access_token(self):
        return self.settings['key']['accessToken']

    def get_access_token_secret(self):
        return self.settings['key']['accessToken']

    def get_file_types(self):
        return tuple(self.settings['fileType'])

    def get_max_size(self):
        return self.settings['maxSize']

    def get_old_pic(self):
        return self.settings['oldPic']

    def set_old_pic(self, pic):
        self.settings['oldPic'] = pic
        return

    def get_status_day(self, day):
        return self.settings['status'][day]

    def get_queue(self):
        return self.settings['queue']

    def __init__(self, dir):
        self.settings = self.__load(dir)
        self.dir = dir
