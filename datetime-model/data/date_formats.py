
# uses datetime strptime behavior - https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
DATE_FORMATS = [
    # month year
    "%B %Y",  # January 2020
    "%b %Y",  # Jan 2020

    # standalone month and year
    "%Y",  # 2020
    "%B",  # January
    "%b",  # Jan

    # month day, year
    "%B %d, %Y",  # January 01, 2020
    "%b %d, %Y",  # Jan 01, 2020
    "%B %-d, %Y",  # January 1, 2020
    "%b %-d, %Y",  # Jan 1, 2020
    "%m %d, %Y",  # 01 01, 2020
    "%-m %-d, %Y",  # 1 1, 2020

    # day month, year
    "%d %B, %Y",  # 01 January, 2020
    "%d %b, %Y",  # 01 Jan, 2020
    "%-d %B, %Y",  # 1 January, 2020
    "%-d %b, %Y",  # 1 Jan, 2020

    # day month year
    "%d{}%B{}%Y",  # 01 January 2020
    "%d{}%b{}%Y",  # 01 Jan 2020
    "%-d{}%B{}%Y",  # 1 January 2020
    "%-d{}%b{}%Y",  # 1 Jan 2020
    # default is month day year for these ambiguous cases
    # "%d %m %Y", # 01 01 2020 TODO: Toggle option for desired behavior in these cases
    # "%-d %-m %Y", # 1 1 2020 TODO: Toggle option for desired behavior in these cases

    # year month day
    "%Y{}%B{}%d",  # 2020 January 01
    "%Y{}%b{}%d",  # 2020 Jan 01
    "%Y{}%B{}%-d",  # 2020 January 1
    "%Y{}%b{}%-d",  # 2020 Jan 1

    # month day year, month/day/year, month-day-year, month.day.year, month|day|year, month~day~year, month`day`year
    "%m{}%d{}%Y",  # 01/01/2020, 01-01-2020, 01.01.2020, 01|01|2020, 01~01~2020, 01`01`2020
    "%-m{}%-d{}%Y",  # 1/1/2020, 1-1-2020, 1.1.2020, 1|1|2020, 1~1~2020, 1`1`2020
    "%B{}%d{}%Y",  # January/01/2020, January-01-2020, January.01.2020, January|01|2020, January~01~2020, January`01`2020
    "%B{}%-d{}%Y",  # January/1/2020, January-1-2020, January.1.2020, January|1|2020, January~1~2020, January`1`2020
    "%b{}%d{}%Y",  # Jan/01/2020, Jan-01-2020, Jan.01.2020, Jan|01|2020, Jan~01~2020, Jan`01`2020
    "%b{}%-d{}%Y",  # Jan/1/2020, Jan-1-2020, Jan.1.2020, Jan|1|2020, Jan~1~2020, Jan`1`2020
]