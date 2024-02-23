from datetime import datetime
from os.path import isfile


class Logger:
    """
    Placeholders:
        %date% - Current date in format {DD.MM.YYYY}\n
        %time24% - Current time in format {HH:MM}\n
        %time12% - Current time in format {HH:MM am/pm}\n
        %type% - Entry type\n
        %text% - Entry text\n
        %filename% - Log file name
    :param str filename: Log file name
    :param str _format: Entry format
    :param bool _print: Print entries to console
    :raise TypeError:
    """
    def __init__(self, filename: str, _format='%date% %time24% [%type%]: %text%', _print=False):
        if not isinstance(filename, str):
            raise TypeError(f'filename must be str, not {str(type(filename))[8:-2]}')
        if not isinstance(_format, str):
            raise TypeError(f'_format must be str, not {str(type(_format))[8:-2]}')
        if not isinstance(_print, bool):
            raise TypeError(f'_print must be bool, not {str(type(_print))[8:-2]}')
        self.__format = _format
        self.__filename = filename
        self.__print = _print

    def custom(self, _type: str, text: str) -> None:
        """
        Creates a custom entry
        :param str _type: Entry type
        :param str text: Entry text
        :raise TypeError:
        """
        if not isinstance(_type, str):
            raise TypeError(f'Type must be str, not {str(type(_type))[8:-2]}')
        if not isinstance(text, str):
            raise TypeError(f'Text must be str, not {str(type(text))[8:-2]}')
        __format = self.__format
        dt = datetime.now()
        while '%type%' in __format:
            __format = __format.replace('%type%', _type)
        while '%text%' in __format:
            __format = __format.replace('%text%', text)
        while '%date%' in __format:
            __format = __format.replace('%date%', dt.strftime('%d.%m.%Y'))
        while '%time12%' in __format:
            __format = __format.replace('%time12%', dt.strftime('%I:%M%p'))
        while '%time24%' in __format:
            __format = __format.replace('%time24%', dt.strftime('%H:%M'))
        while '%filename%' in __format:
            __format = __format.replace('%filename%', self.__filename)
        if isfile(self.__filename):
            with open(self.__filename, 'rt') as f:
                temp = f.readlines()
        else:
            temp = []
        temp.append(__format + '\n')
        with open(self.__filename, 'wt') as f:
            f.writelines(temp)
        if self.__print:
            print(__format)

    def info(self, text: str) -> None:
        """
        Creates an info entry
        :param text: Entry text
        :raise TypeError:
        """
        if not isinstance(text, str):
            raise TypeError(f'text must be str, not {str(type(text))[8:-2]}')
        self.custom('INFO', text)

    def warn(self, text: str) -> None:
        """
        Creates a warn entry
        :param text: Entry text
        :raise TypeError:
        """
        if not isinstance(text, str):
            raise TypeError(f'text must be str, not {str(type(text))[8:-2]}')
        self.custom('WARN', text)

    def error(self, text: str) -> None:
        """
        Creates an error entry
        :param text: Entry text
        :raise TypeError:
        """
        if not isinstance(text, str):
            raise TypeError(f'text must be str, not {str(type(text))[8:-2]}')
        self.custom('ERROR', text)
