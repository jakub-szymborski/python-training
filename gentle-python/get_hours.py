# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:38:03 2023

@author: Kuba
Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. The
argument for this parameter will be the number of seconds to be translated into the number of hours,
minutes, and seconds. If the amount for the hours, minutes, or seconds is zero, don’t show it: the
function should return '10m' rather than '0h 10m 0s'. The only exception is that
getHoursMinutesSeconds(0) should return '0s'.
"""


def getHoursMinutesSeconds(totalSeconds):
    hours   = 0
    minutes = 0
    seconds = 0
    hms = []
    
    if totalSeconds == 0:
        return '0s'
    else: 
        
        if totalSeconds >= 3600:
            hours = int(totalSeconds/3600)
            totalSeconds = totalSeconds - 3600*hours
            minutes = int(totalSeconds/60)
            totalSeconds = totalSeconds - 60*minutes
            seconds = totalSeconds
            
        elif totalSeconds >= 60:
            minutes = int(totalSeconds/60)
            totalSeconds = totalSeconds - 60*minutes
            seconds = totalSeconds
        else:
            seconds = totalSeconds
    
        if hours > 0:
            hms.append(str(hours) +'h')
        if minutes > 0:
            hms.append(str(minutes) +'m')
        if seconds > 0:
            hms.append(str(seconds) +'s')              
        
        return ' '.join(hms)


assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'