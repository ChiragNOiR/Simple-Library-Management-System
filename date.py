
def getDate(): # Declaring getDate Function
    import datetime
    now=datetime.datetime.now
    return str(now().date())

def getTime(): # Declaring getTime Function
    import datetime
    now=datetime.datetime.now
    return str(now().time())
