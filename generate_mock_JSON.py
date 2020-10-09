import json
import uuid
import string
import random
import struct
import socket
from random import randint
from datetime import datetime, timedelta


def random_with_N_digits(n):
    # generate a random number with 'n' digits
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def gen_rand_string(n):
    # generate a random string with 'n' characters
    return ''.join(random.choices(string.ascii_uppercase +
                                  string.digits, k=n))


def gen_datetime(min_year=1900, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


def generate_mock_JSON(N=1):
    # input: number of mock JSON objects that has to be created
    # output: mock JSON array
    result = []
    for k in range(N):
        interface_obj = {"id": random.randint(
            0, 10), "name": gen_rand_string(5), "type": "transport"}

        ip_addresses = []
        for x in range(random.randint(1, 5)):
            ip_addresses.append(socket.inet_ntoa(
                struct.pack('>I', random.randint(1, 0xffffffff))))

        location = {"lat": round(random.uniform(-90, 90), 7),
                    "lon": round(random.uniform(-180, 180), 7)}

        site_ids = []
        for x in range(random.randint(1, 5)):
            site_ids.append(random_with_N_digits(10))

        device_obj = {"id": random.randint(
            0, 10), "name": gen_rand_string(5), "type": "router", "vendor": "Cisco Systems",
            "ipAddresses": ip_addresses, "location": location, "countryCode": None,
            "countryName": random.choice(["India", "China", "Sri Lanka", "Canada", "Germany"]),
            "regionCode": None, "regionName": None, "city": None, "siteIds": site_ids, "interface": interface_obj}

        tenant_id = random.choice(
            ["aankleshwaria", "tjabez", "ankumar", "ahardikar", "pmongia"])

        date_time = str(gen_datetime())

        _source_obj = {"tenantId": tenant_id, "sourceId": "viptela-collector-" + tenant_id, "sourceType": "viptela-collector",
                       "statistic": "raw", "metricId": "state", "metricName": "Device State",
                       "units": "number", "durationMs": 0, "datetime": date_time,
                       "datetimeReceived": date_time, "datetimeProcessed": date_time,
                       "datetimePublished": date_time, "value": date_time, "device": device_obj}

        fields_obj = {"datetimeProcessed": [date_time], "datetime": [
            date_time], "datetimePublished": [date_time], "datetimeReceived": [date_time]}

        sort = []
        for x in range(random.randint(1, 5)):
            sort.append(random_with_N_digits(10))

        doc_obj = {"_index": "metric-samples_"+tenant_id, "_type": "_doc", "_id": uuid.uuid1().hex, "_version": random.randint(1, 100),
                   "_score": None, "sort": sort, "fields": fields_obj, "_source": _source_obj,
                   "fieldRand": random.choice(["field1", "field2", "field3", "field4", "field5"]),
                   "groupRand": random.choice(["group1", "group2", "group3", "group4", "group5"]),
                   "attributeRand": random.choice(["attribute1", "attribute2", "attribute3", "attribute4", "attribute5"])}

        data = {"type": "device", "doc": doc_obj}

        result.append(data)

    return result


if __name__ == "__main__":
    number_of_JSON_elements = input("Enter your value: ")
    result = generate_mock_JSON(int(number_of_JSON_elements))
    print(result)
