#!/usr/bin/python3
import json
import requests

api_url = 'http://127.0.0.1:5000/employees'
create_row_data = {"Address":"11ghgf11 6 Ave SW","BirthDate":"1973-08-29 00:00:00","City":"Calgfdary","Country":"Candfada","Email":"jane@chinookcorp.com","EmployeeId":3,"Fax":"+1 (403) 262-6712","FirstName":"Janfe","HireDate":"2002-04-01 00:00:00","LastName":"Pefcffock","Phone":"+1 (403) 262-3443","PostalCode":"T2P 5M5","ReportsTo":2,"State":"AB","Title":"Sales Support Agent"}
r = requests.post(url=api_url, json=create_row_data)
print(r.status_code, r.reason, r.text)
