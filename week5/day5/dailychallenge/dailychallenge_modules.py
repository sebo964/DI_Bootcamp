# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

import datetime as dt
import requests as req


def timeforsitetoload(websiteurl):
    now_time = dt.datetime.now()
    req.get(websiteurl)
    time_after = dt.datetime.now()
    timetoload = time_after - now_time
    print(timetoload)


timeforsitetoload(
    "http://learn.di-learning.com/courses/collection/18/course/13/section/65/chapter/1354.com"
)
