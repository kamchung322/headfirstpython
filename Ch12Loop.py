import csv, pprint, requests
from datetime import datetime

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

def print_csv():
    """Read csv file in one go"""
    with open('buzzers.csv') as raw_data:
        print(raw_data.read())

def read_csv_to_list() -> list:
    """Use csv to read csv file line by line to list"""
    with open('buzzers.csv') as data:
        list_line = []
        for line in csv.reader(data):
            list_line.append(line)

    return list_line

def read_csv_to_listcomp() -> list:
    """Use csv to read csv file line by line to list"""
    with open('buzzers.csv') as data:
        listcomp = [line for line in csv.reader(data)]

    return listcomp

def print_csv_by_dict():
    """Use csv to read csv file line by line to dict"""
    with open('buzzers.csv') as data:
        for line in csv.DictReader(data):
            print(line)

def read_csv_to_dictcomp() -> dict:
    """doesn't work.  only read one line"""
    with open('buzzers.csv') as data:
        dictcomp = {k:v for k, v in csv.DictReader(data)}

    return dictcomp

def read_csv_to_dict() -> dict:
    with open('buzzers.csv') as data:
        ignore = data.readline()
        flights = {}
        for line in data:
            time, flight = line.strip().split(',')
            flights[time] = flight.title()
    
    return flights

def print_csv_to_dict_manually():
    """csv to dict manually"""
    flights = read_csv_to_dict()
    pprint.pprint(flights)

    flights2 = {}
    for k, v in flights.items():
        flights2[convert2ampm(k)] = v.title()

    pprint.pprint(flights2)

def print_listcomp():
    """Comprehension to List"""
    flights = read_csv_to_dict()
    dest1 = []
    for dest in flights.values():
        dest1.append(dest)
    
    dest2 = [dest.title() for dest in flights.values()]
    
    print(dest1)
    print(dest2)

def print_dictcomp():
    flights = read_csv_to_dict()
    more_flights = {convert2ampm(k): v.title()
                    for k, v in flights.items()
                    if v == 'FREEPORT'}

    pprint.pprint(more_flights)

def print_group_by_flight():
    fts = read_csv_to_dict()
    when = {}
    for dest in set(fts.values()):
        when[dest] = [k for k, v in fts.items() if v == dest]
    
    print(when)

def print_group_by_flight2():
    fts = read_csv_to_dict()
    when = {dest: [k for k, v in fts.items() if v == dest]
            for dest in set(fts.values()) }

    print(when)

def list_to_dict() -> dict:
    fts = read_csv_to_listcomp()
    when = {k: v for k, v in fts}
    return when

def print_url():
    urls = ('http://headfirstlabs.com', 
            'http://oreilly.com',
            'http://twitter.com')

    print("list.  Process all and run")
    for resp in [requests.get(url) for url in urls]:
        print(len(resp.content), '->', resp.status_code, 
                '->' , resp.url)
    print("generator.  Process and run one by one.")
    for resp in (requests.get(url) for url in urls):
        print(len(resp.content), '->', resp.status_code, 
                '->' , resp.url)

def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url

def print_url_by_func():
    urls = ('http://headfirstlabs.com', 
            'http://oreilly.com',
            'http://twitter.com')

    print("generator.  Process and run one by one.")
    for resp_len, status, url, in gen_from_urls(urls):
        print(resp_len, '->', status, '->' , url)

    url_resps = {url: size for url, _, size in gen_from_urls(urls)}
    print(url_resps)

print_url_by_func()
#print(list_to_dict())
#print(read_csv_to_dictcomp())
#print_group_by_flight()
#print_group_by_flight2()
#  print_dictcomp()
#  print_listcomp()
#  pprint.pprint(read_csv_to_listcomp())
#  print_csv_to_dict_manually()
#  comprehension_list()
#  csv_to_dict_manually()
#  read_csv_to_list()