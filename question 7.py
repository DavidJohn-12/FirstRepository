def seconds_converter(seconds):
    # Convert total seconds to hours
    hours = int(seconds / 3600)

    # Remaining seconds after extracting hours
    remaining_hour = seconds - hours * 3600

    # Convert remaining seconds to minutes
    minutes = int(remaining_hour / 60)

    # Remaining seconds after extracting minutes
    remaining_minute = remaining_hour - minutes * 60
    seconds = remaining_minute  # Final remaining seconds

    # Used to check whether the computed time is valid
    time_validity = True

    # Invalid if seconds correspond to a negative time
    if hours < 0:
        return "Seconds cannot be negative"

    # Invalid if seconds exceed one full day
    if hours > 24:
        return "Number of seconds have exceeded the current day"

    # Determine whether time is AM or PM
    if time_validity == True:
        if hours < 11:
            meridian = "AM"
        if 11 < hours < 24:
            meridian = "PM"

        return str(f"{hours} {minutes} {seconds} {meridian}")


print(seconds_converter(7890))
