class LogLevels:
    api = 0
    feature = 1
    test = 2
    critical = 9


def log_color(s, fg, bg): return "\033[{s};{fg};{bg}m ".format(s=s, fg=fg, bg=bg)


class ForegroundColors:
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    purple = 35
    cyan = 36
    white = 37


class BackgroundColors:
    black = 40
    red = 41
    green = 42
    yellow = 43
    blue = 44
    purple = 45
    cyan = 46
    white = 47


class TextStyle:
    no_style = 0
    bold = 1
    underline = 2
    negative1 = 3
    negative2 = 5


class LogColors:
    level_color = {
        LogLevels.api: log_color(TextStyle.bold, ForegroundColors.yellow, 0),
        LogLevels.feature: log_color(TextStyle.bold, ForegroundColors.blue, 0),
        LogLevels.test: log_color(TextStyle.bold, ForegroundColors.purple, 0),
        LogLevels.critical: log_color(TextStyle.bold, ForegroundColors.red, 0)
    }

    end = log_color(TextStyle.no_style, 0, 0)
