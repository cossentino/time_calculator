import re
import pdb
# Ex: t1: 11:30 AM
#     t2: 2:32

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def extract_time(t: str):
  hour = int(re.findall(r"\A\d+", t)[0])
  minute = int(re.findall(r":(\d+)", t)[0])
  return (hour, minute)

def time_to_string(t: list):
  my_time = [str(t[0]), None]
  if t[1] < 10:
    my_time[1] = "0" + str(t[1])
  else:
    my_time[1] = str(t[1])
  return f"{my_time[0]}:{my_time[1]}"

def calculate_new_day(start_day: str, extra_days):
  start_day_index = WEEKDAYS.index(start_day)
  return WEEKDAYS[(start_day_index + extra_days) % 7]


def format_output_string(my_time: str, my_day: str, extra_days: int, am_pm: str):
  return_string = my_time + " " + am_pm
  if my_day:
    my_day = my_day[0].upper() + my_day[1:]
    return_string += f", {my_day}"
  if extra_days > 1:
    my_comment = f" ({extra_days} days later)"
    return_string += my_comment
  elif extra_days == 1:
    my_comment = " (next day)"
    return_string += my_comment
  return return_string
  


def add_time(t1_str: str, t2_str: str, day: str=None) -> str:
  t1 = extract_time(t1_str)
  t2 = extract_time(t2_str)
  new_day = False
  am_pm = "AM"
  extra_days = 0
  my_day = day.lower() if day else None
  new_time = [t1[0] + t2[0], t1[1] + t2[1]]
  if t1_str[-2] == "P":
    new_time[0] += 12
  if new_time[1] >= 60:
    new_time[0] += 1
    new_time[1] -= 60
  if new_time[0] >= 24:
    new_day = True
    extra_days = new_time[0] // 24
    new_time[0] = new_time[0] % 24
  if new_time[0] >= 12:
    am_pm = "PM"
  if my_day and extra_days > 0:
    my_day = calculate_new_day(my_day, extra_days)
  new_time[0] = new_time[0] % 12
  if new_time[0] == 0:
    new_time[0] = 12
  my_time = time_to_string(new_time)
  
  return format_output_string(my_time, my_day, extra_days, am_pm)


print(add_time('10:10 PM', '3:30'))