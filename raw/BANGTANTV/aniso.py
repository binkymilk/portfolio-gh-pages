import aniso8601
import datetime

print(aniso8601.parse_duration('PT1M1S').total_seconds())
#print(datetime.timedelta(aniso8601.parse_duration('PT1M1S')))