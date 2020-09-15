from datetime import datetime

ATOMIC_TIME = datetime.now()
convert_atomic_time_to_string = str(ATOMIC_TIME)


def reset_time(atomic_time):
    reset_seconds = convert_atomic_time_to_string[:17] + ("0" * 2) + convert_atomic_time_to_string[19:]
    reset_milliseconds = reset_seconds[:20] + ("0" * 6) + reset_seconds[26:]
    return reset_milliseconds


print(f"Original Atomic Time: {ATOMIC_TIME}")
print(f"Resetted Atomic Time: {reset_time(ATOMIC_TIME)}")
print("/===============/")

real_time = datetime.strptime(convert_atomic_time_to_string, "%Y-%m-%d %H:%M:%S.%f")

user_input = input("Press enter when the second hand hits 12: ")
watch_time = datetime.strptime(reset_time(ATOMIC_TIME), "%Y-%m-%d %H:%M:%S.%f")


print(real_time-watch_time)

