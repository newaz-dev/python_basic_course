# from datetime import datetime

# now = datetime.now()

# codes
#     ("%a", "Weekday short name  -> Mon"),
#     ("%A", "Weekday full name   -> Monday"),
#     ("%w", "Weekday as number   -> 0=Sunday ... 6=Saturday"),
#     ("%u", "ISO weekday number  -> 1=Monday ... 7=Sunday"),
#     ("%d", "Day of month        -> 01 to 31"),
#     ("%b", "Month short name    -> Jan"),
#     ("%B", "Month full name     -> January"),
#     ("%m", "Month as number     -> 01 to 12"),
#     ("%y", "Year, 2 digit       -> 26"),
#     ("%Y", "Year, 4 digit       -> 2026"),
#     ("%G", "ISO year            -> ISO week based year"),
#     ("%H", "Hour, 24 hour clock -> 00 to 23"),
#     ("%I", "Hour, 12 hour clock -> 01 to 12"),
#     ("%p", "AM or PM"),
#     ("%M", "Minute              -> 00 to 59"),
#     ("%S", "Second              -> 00 to 59"),
#     ("%f", "Microsecond         -> 000000 to 999999"),
#     ("%z", "UTC offset          -> +0600 (empty if naive datetime)"),
#     ("%Z", "Timezone name       -> empty if naive datetime"),
#     ("%j", "Day of the year     -> 001 to 366"),
#     ("%U", "Week number, Sunday as first day -> 00 to 53"),
#     ("%W", "Week number, Monday as first day -> 00 to 53"),
#     ("%V", "ISO week number     -> 01 to 53"),
#     ("%c", "Locale date and time"),
#     ("%x", "Locale date only"),
#     ("%X", "Locale time only"),
#     ("%%", "A literal percent sign"),


# # Common ready made combinations
# combos
#     ("%d/%m/%Y", "Day/Month/Year"),
#     ("%Y-%m-%d", "ISO style date"),
#     ("%Y-%m-%d %H:%M:%S", "Date with 24 hour time"),
#     ("%d %B %Y", "Day with full month name"),
#     ("%A, %d %B %Y", "Weekday with full date"),
#     ("%I:%M %p", "12 hour time with AM/PM"),
#     ("%H:%M:%S.%f", "Time with microseconds"),
#     ("%b %d, %Y %I:%M %p", "Common log style"),
#     ("%Y-%m-%dT%H:%M:%S%z", "ISO 8601 full"),

# # Reverse work: string to datetime using the same codes
# text = "21/10/2026 11:55"
# parsed = datetime.strptime(text, "%d/%m/%Y %H:%M")
# print("\nstrptime:", parsed)