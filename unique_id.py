# encryption

import zlib
import pandas

measure_comp = pandas.read_csv('bbdb_consented.csv')


print(measure_comp)


fn = measure_comp['firstname'].tolist()
ln = measure_comp['lastname'].tolist()
dob = measure_comp['dob'].tolist()

unique_ids = []

test = []

for i in range(len(measure_comp)):
	s = '{}{}{}'.format(fn[i], ln[i], dob[i])
	x = hex(zlib.crc32(s))
	x = x.strip('-')[2:]
	if(len(x) != 8):
		adjusted = x.ljust(8, '0')
		unique_ids.append(adjusted)
	else:
		unique_ids.append(x)

print(unique_ids)

print(len(unique_ids))

# print(len(unique_id), unique_id, x)
