
"""
Day 30 - Pyhton milestone
A small python program to write tosay's achivement.


"""

from pathlib import Path
from datetime import datetime 

with open("date_time.txt", "a+") as f:
  f.write(f"{datetime.now()}")
  f.seek(0)
  print(f.readlines())