"""Make methods to make life easier."""


def get_rounded_float(float_num, figures=3):
    """Return number rounded to X number of places."""
    precision = '{0:.%sf}' % figures
    # float means return the formatted string as an actual number type
    return float(precision.format(float_num))
