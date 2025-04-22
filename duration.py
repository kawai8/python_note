import argparse
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import sys

def d_from(str_date):
    try:
        str_date = str_date + ' 00:00:00'
        x = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
        return x.astimezone(ZoneInfo(key="Asia/Tokyo"))
    except ValueError:
        err_msg = "The Start Date is invalid"
    raise argparse.ArgumentTypeError(err_msg)


def d_till(str_date):
    try:
        str_date = str_date + ' 23:59:59'
        x = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
        return x.astimezone(ZoneInfo(key="Asia/Tokyo"))
    except ValueError:
        err_msg = "The End Date is invalid"
    raise argparse.ArgumentTypeError(err_msg)


def check_range(start, end):
    start_date = start
    if args.end:
        end_date = end
    else:
        end_date = start_date + timedelta(days=1) - timedelta(seconds=1)

    duration = end_date - start_date
    if start_date > end_date or duration.days > 60:
        print('Date is out of range')
        sys.exit(9)
    return start_date, end_date


parser = argparse.ArgumentParser(description='')
parser.add_argument(
    "-s", "--start", type=d_from, required=True,
    help="e.g.) yyyy-mm-dd",
)
parser.add_argument(
    "-e", "--end", type=d_till, required=False,
    help="e.g.) yyyy-mm-dd",
)


args = parser.parse_args()
start_date, end_date = check_range(args.start, args.end)
print(start_date, '-', end_date)
print(start_date.timestamp())
print(end_date.timestamp())
