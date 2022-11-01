import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

result = []
dict = [{'lastname': 'lastname', 'firstname': 'firstname', 'surname': 'surname', 'organization': 'organization',
         'position': 'position', 'phone': 'phone', 'email': 'email'}]
pattern = r"([А-Я]\w+).([А-Я]\w+).(([А-Я]\w+)|(,+)),+(([А-Яа-я]\w+)|),+(([^+78,a-zA-Z]+)|)(,+|)((\+7|8)?(\s|)(\(|)((" \
          r"?:\d{1,3}))(\)|)(\D|)((?:\d{1,3}))(\D|)((?:\d{1,2}))(\D|)((?:\d{1,2}))|)(\W|)((\(|)доб. (....)(\)|)|)(," \
          r"|)((\w+(.|)\w+@\w+(.|).\w+(.|))|) "

for line in contacts_list:
    line_text = ",".join(line)
    new_raw = re.sub(pattern, r"\1,\2,\4,\7,\9,+7(\15)\18-\20-\22 доб. \26,\30", line_text).split(',')

    if new_raw[-2] == '+7()-- доб. ':
        new_raw[-2] = ''

    new_raw_dict = {'lastname': new_raw[0], 'firstname': new_raw[1], 'surname': new_raw[2], 'organization': new_raw[3],
                    'position': new_raw[4], 'phone': new_raw[5], 'email': new_raw[6]}
    for contact in dict:
        if new_raw[0] == contact['lastname'] and new_raw[1] == contact['firstname']:
            if contact['email'] == '':
                contact['email'] = new_raw[6]
            if contact['phone'] == '':
                contact['phone'] = new_raw[5]
            if contact['position'] == '':
                contact['position'] = new_raw[4]
            if contact['organization'] == '':
                contact['organization'] = new_raw[3]
            trigger = 0

            break
        else:
            trigger = 1
    if trigger == 1:
        dict.append({'lastname': new_raw[0], 'firstname': new_raw[1], 'surname': new_raw[2], 'organization': new_raw[3],
                     'position': new_raw[4], 'phone': new_raw[5], 'email': new_raw[6]})
    else:
        pass

for contact in dict:
    result.append(
        [contact['lastname'], contact['firstname'], contact['surname'], contact['organization'], contact['position'],
         contact['phone'], contact['email']])

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result)
