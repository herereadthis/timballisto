from datetime import timedelta


def get_uptime(readable=True):
    """Return the uptime in seconds or human-readable format."""
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        if readable:
            uptime_string = str(timedelta(seconds = uptime_seconds))
            return uptime_string
        else:
            return uptime_seconds


if __name__ == '__main__':
    print(get_uptime())
    print(get_uptime(False))
