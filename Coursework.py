from datetime import datetime
def read_file(filename: str) -> str:
    with open(filename, "r") as txt_file:
        data = txt_file.read()
    return data
filename = "test_logs.txt"
data_dict = {"username": [],
        "email": [],
        "date_connected": [],
        "ip": [],
        "connection_duration": []}
data = read_file(filename)
lines = data.split(",")
keys = ['username', 'email', 'date_connected', 'ip', 'connection_duration']
dates = []
users_dict = {}
for line in lines:
    split1 = line.splitlines()
    for key in keys:
        for item in split1:
            data_dict_user = {}
            if key in line:
                if "username: " in item:
                    value = item.split("username: ", 1)[1].strip()
                    value_key = value
                    data_dict["username"].append(value)
                    if value_key not in users_dict.keys():
                        users_dict[value_key] = {"email": [], "date_connected": [], "ip": [], "connection_duration": []}
                elif "email: " in item:
                    value = item.split("email: ", 1)[1].strip()
                    data_dict["email"].append(value)
                    if value not in users_dict[value_key]["email"]:
                        users_dict[value_key]["email"].append(value)
                elif "date_connected: " in item:
                    value = item.split("date_connected: ", 1)[1].strip()
                    data_dict["date_connected"].append(value)
                    if value not in users_dict[value_key]["date_connected"]:
                        users_dict[value_key]["date_connected"].append(value)
                elif "ip: " in item:
                    value = item.split("ip: ", 1)[1].strip()
                    data_dict["ip"].append(value)
                    if value not in users_dict[value_key]["ip"]:
                        users_dict[value_key]["ip"].append(value)
                elif "connection_duration: " in item:
                    value = item.split("connection_duration: ", 1)[1].strip()
                    data_dict["connection_duration"].append(value)
                    if value not in users_dict[value_key]["connection_duration"]:
                        users_dict[value_key]["connection_duration"].append(value)




def period(data_base_dict: dict, key: str):
    for date in data_base_dict[key]:
        dates.append(date.split()[0])
    dates_sorted = sorted(dates, key=lambda date: datetime.strptime(date, "%d/%m/%Y"))
    periods = [dates_sorted[0], dates_sorted[-1]]
    return periods
date_period = period(data_dict, "date_connected")


def users(data_base_dict: dict, key: str):
    unique = list(set(data_base_dict[key]))
    count = len(unique)
    return count
unique_users = users(data_dict, "username")


def connections_users(data_base_dict: dict, key: str) -> dict:
    connections_dict = {}
    unique = list(set(data_base_dict[key]))
    for keys in unique:
        for value in data_base_dict[key]:
            connections = data_base_dict[key].count(value)
            if keys == value:
                connections_dict[value] = connections
    return connections_dict
connections_time = connections_users(data_dict, "username")


def unique_ip(data_base_dict: dict, key: str) -> dict:
    ips_dict = {}
    for user, data in data_base_dict.items():
        ips_list = data[key]
        unique_ips = list(set(ips_list))
        ips_dict[user] = unique_ips
    return ips_dict
unique_ips_for_users = unique_ip(users_dict, "ip")

def unique_ip_count(data_base_dict: dict, key: str) -> dict:
    ips_count_dict = {}
    for user, data in data_base_dict.items():
        unique_ips = set(data[key])
        unique_ips_count = len(unique_ips)
        ips_count_dict[user] = unique_ips_count
    return ips_count_dict
unique_ips_for_users_count = unique_ip_count(users_dict, "ip")


def time_spent(data_base_dict: dict, key: str) -> dict:
    time_dict = {}
    for user, data in data_base_dict.items():
        time_count = 0
        for time_str in data[key]:
            time_str_split = time_str.split(":")
            time_str1 = time_str_split[0]
            time_str2 = time_str_split[1]
            time_str3 = time_str_split[2]
            time_count += int(time_str1) * 3600 + int(time_str2) * 60 + int(time_str3)
            time_dict[user] = time_count
    return time_dict

users_time_spent = time_spent(users_dict, "connection_duration")





