import re
from pprint import pprint
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




with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(result)
