import datetime
date=datetime.datetime.now()
print(date.strftime("%B %d,%Y %I:%M %p"))
# # print(type(time),time)

# def time_str(fmt=None):
#   if fmt is None:
#     fmt = '%Y-%m-%d_%H:%M:%S'
#   return datetime.datetime.today().strftime(fmt)
