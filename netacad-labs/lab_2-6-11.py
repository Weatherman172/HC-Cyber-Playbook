hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

end_hour = (hour + (mins + dura) // 60) % 24
end_minute = (mins + dura) % 60

print(str(end_hour) + ":" + str(end_minute))
