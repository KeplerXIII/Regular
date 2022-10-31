from collections import OrderedDict
import re
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

result = []
# result.append(contacts_list[0])
pattern = r"([А-Я]\w+).([А-Я]\w+).(([А-Я]\w+)|(,+)),+(([А-Яа-я]\w+)|),+(([^+78,a-zA-Z]+)|)(,+|)((\+7|8)?(\s|)(\(|)((?:\d{1,3}))(\)|)(\D|)((?:\d{1,3}))(\D|)((?:\d{1,2}))(\D|)((?:\d{1,2}))|)(\W|)((\(|)доб. (....)(\)|)|)(,|)((\w+(.|)\w+@\w+(.|).\w+(.|))|)"
for line in contacts_list:
  line_text = ",".join(line)
  new_raw = re.sub(pattern, r"\1,\2,\4,\7,\9,+7(\15)\18-\20-\22 доб. \26,\30", line_text)

  result.append(new_raw.split(','))

for contact in result:
    if contact[-2] == '+7()-- доб. ':
        contact[-2] = ''


def remove_duplicates(list_: list) -> list:
    k = 0
    while k < len(list_) - 1:
        for list1, list2 in zip(list_[k], list_[k + 1]):
            if list1 == list2:
                new_list = list(OrderedDict.fromkeys(list_[k] + list_[k + 1]))
                list_.remove(list_[k + 1])
                list_.remove(list_[k])
                list_.append(new_list)
            break
        k += 1
    return list_

unique_data_list = remove_duplicates(result)

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(unique_data_list)
