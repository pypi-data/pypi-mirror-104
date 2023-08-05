import logging
import platform
from custom_loggers.Colors import Foreground255,SequenceName,FontStyles
from typing import Union
import inspect
from pathlib import Path


class ColoredFormatter(logging.Formatter):
    """
    ColoredFormatter simplifies designating colors for different log levels
    WINDOWS_OVERRIDE by default is set to False
    By default we prevent colored formatting on Windows machines as the CMD doesn't natively support
    color sequences

    set to True to allow on Windows machines
    ColoredFormatter.WINDOWS_OVERRIDE=True

    """
    WINDOWS_OVERRIDE = False
    _COLORS_ASSIGNMENTS = {
        'WARNING': Foreground255(208),
        'INFO': Foreground255(249),
        'DEBUG': Foreground255(8),
        'CRITICAL': Foreground255(11),
        'ERROR': Foreground255(196),
        'TRACE': Foreground255(14)
    }
    use_script_location=False

    @classmethod
    def assign_level_color(cls, levelname: str, color: Union[str, SequenceName]) -> None:
        """
        add/modifies a level to the color_assignments dictionary

        :param levelname: string representation of a level.
        :param color: this is expected to be either a sequence string or a SequenceName from colors
            SequenceNames can be concatenated to make hybrid styles.
            ForeGroundColors.WHITE+BackgroundColors.RED+FontStyles.ITALIC == the three string sequences together
        :return: None
        """
        cls._COLORS_ASSIGNMENTS[levelname.upper()] = color

    def __init__(self, msg, datefmt=None, style='%', use_color=True):
        super().__init__(msg, datefmt, style)
        self.use_color = use_color

    def format(self, record):
        """
        adds colored formatting to standard formatting from the super class
        this is done via the _COLORS_ASSIGNMENTS dictionary

        if a level doesn't exist in the dictionary we'll return the standard formatted string
        by default we skip colored formatting on WINDOWS machines see notes in class documentation

        :param record:
        :return: fully formated message
        """
        levelname = record.levelname

        def get_instance_from_frame(fr):
            import inspect
            insp_args, _, _, value_dict = inspect.getargvalues(fr)
            # we check the first parameter for the frame function is
            # named 'self' this 98% means it's a class
            if len(insp_args) and insp_args[0] == 'self':
                instance = value_dict.get('self', None)
                return instance
            return None

        frame = inspect.currentframe()
        while True:
            from logging import Logger
            instance = get_instance_from_frame(frame)
            if Path(frame.f_code.co_filename).name=="__init__.py":
                pass
            elif not isinstance(instance,ColoredFormatter) and not isinstance(instance,Logger):
                break
            frame = frame.f_back

        func = frame.f_code

        script_path=Path(func.co_filename)
        record.scriptpath=str(script_path)
        record.scriptname=script_path.name
        record.scriptline=frame.f_lineno

        s=super().format(record)

        if self.use_color and (not platform.system() == 'Windows' or ColoredFormatter.WINDOWS_OVERRIDE):
            if levelname in ColoredFormatter._COLORS_ASSIGNMENTS.keys():
                return ColoredFormatter._COLORS_ASSIGNMENTS[levelname] + s + FontStyles.RESET
            else:
                return Foreground255(249) + s + FontStyles.RESET
        else:
            return s
