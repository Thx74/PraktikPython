from datetime import datetime as dt

def dateANDtime(a):
    print(dt.strptime(a, '%Y-%m-%d %H:%M:%S'))
    print(type(dt.strptime(a, '%Y-%m-%d %H:%M:%S')))

a = "2020-12-10 23:55:39"
dateANDtime(a)