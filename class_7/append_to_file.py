from datetime import datetime as dt
log = open("log_file.log", "a", encoding="utf_8")
log.write("\n{} INFO: Second log entry".format(dt.now()))
log.close()
log = open("log_file.log", "r")
print(log.read())
log.close()
