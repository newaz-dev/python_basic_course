from datetime import datetime, date, time, timedelta

now = datetime.now()
print("Now:", now)

# ---------- ADD ----------
print("\nADD")
print("+10 seconds :", now + timedelta(seconds=10))
print("+30 minutes :", now + timedelta(minutes=30))
print("+5 hours    :", now + timedelta(hours=5))
print("+1 day      :", now + timedelta(days=1))
print("+2 weeks    :", now + timedelta(weeks=2))
print("mixed       :", now + timedelta(days=3, hours=4, minutes=20))

# ---------- SUBTRACT ----------
print("\nSUBTRACT")
print("-1 day      :", now - timedelta(days=1))
print("-90 minutes :", now - timedelta(minutes=90))
print("-365 days   :", now - timedelta(days=365))

# ---------- DIFFERENCE between two datetime ----------
exam = datetime(2026, 12, 25, 10, 0, 0)
diff = exam - now          # result is a timedelta object
print("\nDIFFERENCE")
print("timedelta   :", diff)
print("days        :", diff.days)
print("seconds     :", diff.seconds)          # only the leftover seconds, not total
print("total_seconds:", diff.total_seconds()) # full gap in seconds
print("total hours :", diff.total_seconds() / 3600)

# ---------- COMPARE ----------
print("\nCOMPARE")
print("exam is future?", exam > now)
print("same day?      :", exam.date() == now.date())

# ---------- REPLACE: change one part only ----------
print("\nREPLACE")
print("year changed :", now.replace(year=2030))
print("midnight     :", now.replace(hour=0, minute=0, second=0, microsecond=0))

# ---------- date and time alone ----------
print("\nDATE / TIME PARTS")
print("date only :", now.date())
print("time only :", now.time())
print("combine   :", datetime.combine(date(2026, 1, 1), time(9, 30)))