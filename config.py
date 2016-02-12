import os
import sys
import logging
import json


class Config:
    # create the cofig format
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

        word = [('One', 'This is the word One.'),
                ('Two', 'This is the word Two.'),
                ('Three', 'This is the word Three.')]

        quote = [('James Doel', 'In the words of James', '#ff0000', 'D:\James Doel\Test\2.jpg',
                  'Python is fun, it can do almost ANYTHING... almost.'),
                 ('Salvador Dali', 'As he says:', '#b3b3ff', 'D:\James Doel\Test\3.jpg',
                  'Have no fear of perfection, you\'ll never reach it.')]

        font = ('arial.ttf', 'calibri.ttf', 'comic.ttf')

        wordColour = (('#730099', '#3399FF'), ('#e60000', '#00cc00'), ('#ffffff', '#0000ff'))

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

        pauseOnErrors = False

        settings = {'key': key,
                    'status': status,
                    'queue': queue,
                    'word': word,
                    'quote': quote,
                    'font': font,
                    'wordColour': wordColour,
                    'oldPic': oldPic,
                    'fileType': fileType,
                    'maxSize': maxSize,
                    'pauseOnErrors': pauseOnErrors}

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
                f.close()
            except:
                f.close()
                logging.error('Congif file corrupted.')
                sys.exit(1)
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
                    dir = input('Not able to create config file, please try a new location: ')
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
        return self.settings['key']['accessTokenSecret']

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

    def get_word(self):
        return self.settings['word']

    def get_quote(self):
        return self.settings['quote']

    def get_font(self):
        return self.settings['font']

    def get_word_colour(self):
        return self.settings['wordColour']

    def error(self, error):
        if self.settings['pauseOnErrors'] == 'true':
            logging.error(error)
            os.system("Pause")
            sys.exit(1)
        else:
            logging.error(error)
            sys.exit(1)


    def __init__(self, dir):
        self.settings = self.__load(dir)
        self.dir = dir
