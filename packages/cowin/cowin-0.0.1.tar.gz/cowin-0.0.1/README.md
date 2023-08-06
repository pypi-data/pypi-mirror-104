# Cowin Tracker

Python API wrapper for CoWin, India's digital platform launched by the government to help citizens register themselves
for the vaccination drive by booking an appointment at the nearby vaccination centres

The process to look-up for available slots to take the vaccine is tedious as you need to log in to the portal every time

This wrapper is meant to enable folks to build their own versions of a system to lookup for vaccine availablity either
in a district or in a particular pin code.

Example:

```
from cowin_api import CoWinAPI
cowin = CoWinAPI()

states = cowin.get_states()
print(states)
```
