import requests
import re
import datetime
import operator
import os
from dotenv import load_dotenv


load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


def get_id_from_username(username):
    payload = {'access_token': ACCESS_TOKEN, 'user_ids': username, 'version': '5.92'}
    r = requests.get('https://api.vk.com/method/users.get', params=payload)
    if r.status_code != 200:
        return None
    ret = r.json()
    return ret["response"][0]["uid"]


def get_friend_list(uid):
    payload = {'access_token': ACCESS_TOKEN, 'user_id': uid, 'fields': ['bdate'], 'version': '5.92'}
    r = requests.get('https://api.vk.com/method/friends.get', params=payload)
    if r.status_code != 200:
        return r.status_code
    ret = r.json()
    return ret


def get_birth_dict(fr_list):
    birth_dict = {}
    for friend in fr_list["response"]:
        if 'bdate' not in friend:
            continue
        regex = r'(\d+).(\d+).(\d+)'
        match = re.search(regex, friend['bdate'])
        if match is None:
            continue
        # print("user: {} has birthday: {}".format(friend['last_name'], friend['bdate']))
        birth_dict[friend['last_name']] = match.group(3)
    return birth_dict


def sort_by_count(current_dict):
    temp_dict = {}
    for _,age in current_dict.items():
        if age not in temp_dict:
            temp_dict[age] = 1
        else:
            temp_dict[age] = temp_dict[age] + 1
    sorted_d = sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_d


def sort_cust(list):
    count = len(list)
    res_list = list
    tmp_list = []
    n = 0
    c = 0
    while True:
        if list[n][1] != list[n+1][1]:
            n += 1
            c = n
            continue
        tmp_list.append(list[n])
        tmp_list.append(list[n+1])
        while True:
            if count-2 == n:
                break
            if list[n+1][1] != list[n+2][1]:
                break
            tmp_list.append(list[n+2])
            n += 1
        sort_list = sorted(tmp_list, key=lambda x: x[0])
        for i in sort_list:
            res_list[c] = i
            c += 1
        n += 2
        tmp_list = []

        if count-2 <= n:
            break
    return res_list


def calc_age(user):
    uid = get_id_from_username(user)
    fr_list = get_friend_list(uid)
    birth_dict = get_birth_dict(fr_list)
    curent_year = datetime.date.today().year
    for fr,birth_year in birth_dict.items():
        age = int(curent_year) - int(birth_year)
        birth_dict[fr] = age
    return sort_cust(sort_by_count(birth_dict))


if __name__ == '__main__':

    print(calc_age('maxim_sych'))

