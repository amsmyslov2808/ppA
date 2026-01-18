secs_from_midnight = int(input("введите кол-во секунд прошедших с начала суток: "))

secs = secs_from_midnight % 60

temp_min = secs_from_midnight // 60

hours = temp_min // 60

mins = temp_min % 60

secs_as_string = str(secs)
mins_as_string = str(mins)
hours_as_string = str(hours)

if secs < 10:
    secs_as_string = "0" + str(secs)

if mins < 10:
    mins_as_string = "0" + str(mins)

if hours < 10:
    hours_as_string = "0" + str(hours)

print(
    f"{secs_from_midnight} секунд = {hours_as_string}:{mins_as_string}:{secs_as_string}"
)
