from datetime import datetime

atomic_time = datetime.now()
convert_atomic_time_to_string = str(atomic_time)

print(f"Old Atomic Time: {atomic_time}")


# new_atomic_time = convert_atomic_time_to_string[17:18] + "0" + convert_atomic_time_to_string[18:]
# new_atomic_timeb = new_atomic_time[:18] + "0" + new_atomic_time[19:]


print(f"New Atomic Time: {reset_time(atomic_time)}")


def reset_time(atomic_time):
    reset_seconds = convert_atomic_time_to_string[:17] + ("0" * 2) + convert_atomic_time_to_string[19:]
    reset_milliseconds = reset_seconds[:20] + ("0" * 6) + reset_seconds[26:]
    return reset_milliseconds

# #
# t1 = datetime.strptime(shit, "%b %d %H:%M:%S %Y")
# t2 = datetime.strptime(new_atomic_timeb, "%b %d %H:%M:%S %Y")
#
#
# print(t1-t2)

