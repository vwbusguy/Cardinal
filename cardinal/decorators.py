import re


_RETYPE = type(re.compile('foobar'))


def command(triggers):
    if isinstance(triggers, str):
        triggers = [triggers]

    if not isinstance(triggers, list):
        raise TypeError("Command must be a trigger string or list of triggers")

    def wrap(f):
        f.commands = triggers
        return f

    return wrap


def regex(expression):
    if (not isinstance(expression, str) and
            not isinstance(expression, _RETYPE)):
        raise TypeError("Regular expression must be a string or regex type")

    def wrap(f):
        f.regex = expression
        return f

    return wrap


def help(lines):
    # For backwards compatibility
    if isinstance(lines, str):
        lines = [lines]

    if not isinstance(lines, list):
        raise TypeError("Help must be a help string or list of help strings")

    def wrap(f):
        # Create help list or prepend to it
        if not hasattr(f, 'help'):
            f.help = lines
        else:
            f.help = lines + f.help

        return f

    return wrap


def event(triggers):
    if isinstance(triggers, str):
        triggers = [triggers]

    if not isinstance(triggers, list):
        raise TypeError("Event must be a trigger string or list of triggers")

    def wrap(f):
        f.events = triggers
        return f

    return wrap
