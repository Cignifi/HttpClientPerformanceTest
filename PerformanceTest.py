
import requests
import datetime



session = requests.Session()

def singleHttpRequests():

    print("Starting SingleHttpClient")
    totalValue = 0;
    median = 0.0;
    for item in range(10):
        before = datetime.datetime.now()
        r = requests.get("URL")
        after = datetime.datetime.now()
        span = after - before
        print(f"{r.status_code}  -  {span.microseconds / 1000}") 
        totalValue += span.microseconds
        median = totalValue / (item + 1)

    print("Connections done")
    print(f"total time: {totalValue / 1000}")
    print(f"Average: {median / 1000}")

def multipleHttpRequests():
    
    print("Starting MultipleHttpClient")
    totalValue = 0;
    median = 0.0;
    
    for item in range(10):
        before = datetime.datetime.now()
        r = session.get("URL")
        after = datetime.datetime.now()
        span = after - before
        print(f"{r.status_code}  -  {span.microseconds / 1000}") 
        totalValue += span.microseconds
        median = totalValue / (item + 1)

    print("Connections done")
    print(f"total time: {totalValue / 1000}")
    print(f"Average: {median / 1000}")

singleHttpRequests()
multipleHttpRequests()