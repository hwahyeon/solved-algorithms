def whatday(num):
    if num < 0 or num > 7:
        num = 0
    return ["Wrong, please enter a number between 1 and 7",
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"][num]
