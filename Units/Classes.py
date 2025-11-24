from datetime import *
class problem_deadline:
    issue_name = None
    day_deadline = None      # int
    month_deadline = None    # int
    year_deadline = None     # int
    hour_deadline = None     # int
    minute_deadline = None   # int
    importance = None        # int,
    hard = None              # int
    status=0;#0 если в процессе, 1 если выполнено, -1 если прошел дедлайн

    def __init__(self, time_to_set, important, hard, issue="unknown"):

        if len(time_to_set) != 5:
            raise ValueError("Wrong data from programmer")
        day, month, year, hour, minute = time_to_set

        try:
            datetime(year=year, month=month, day=day, hour=hour, minute=minute)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Wrong datetime format: {e}")

        if not check_time(time_to_set):
            raise ValueError("Deadline must be in the future or now. Please rewrite the date.")

        self.importance = max(1, min(100, important))
        self.hard = max(1, min(100, hard))

        self.issue_name = issue
        self.day_deadline = day
        self.month_deadline = month
        self.year_deadline = year
        self.hour_deadline = hour
        self.minute_deadline = minute

def get_time():
    current_moment = datetime.now()
    return [
        current_moment.day,
        current_moment.month,
        current_moment.year,
        current_moment.hour,
        current_moment.minute
    ]


def check_time(input_time):
    d1, m1, y1, h1, min1 = input_time
    d2, m2, y2, h2, min2 = get_time()
    time_input = (y1, m1, d1, h1, min1)
    time_now = (y2, m2, d2, h2, min2)
    return time_input >= time_now
