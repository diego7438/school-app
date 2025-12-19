import datetime as dt
# This function needs helpers from our rotation blueprint, so we import them.
from .rotation import get_rotation_for_date, get_year_from_schedule

# TODO: This is a helper function that is not yet used in any API endpoint.
# It's a great idea for a future feature, like "find all the days I have rotation 6".
def get_blocks_in_range(target_rotation, m1, d1, m2, d2):
  year1 = get_year_from_schedule(m1)
  year2 = get_year_from_schedule(m2)
  start_date = dt.date(year1, m1, d1)
  end_date = dt.date(year2, m2, d2)

  if start_date > end_date:
    return [] # or raise an error for an invalid range
  
  results = []
  current_date = start_date
  while current_date <= end_date:
    rotation_info = get_rotation_for_date(current_date.month, current_date.day)
    if rotation_info and rotation_info[0] == target_rotation:
      results.append((f"{current_date.month}/{current_date.day}", rotation_info[1]))
    current_date += dt.timedelta(days=1)
  
  return results
