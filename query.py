#Total estimates (requested) and total owned estimates by user(s) who have requested more than two stories of bug type.

import sqlite3
from collections import Counter

#Making headers for display
conn = sqlite3.connect("database.db") #getting column info for table 1
a = conn.execute("PRAGMA table_info(TABLE_1)")
a = list(a)
b = conn.execute("PRAGMA table_info(TABLE_2)") #geting column info for table 2
b = list(b)

#querying both tables
query = conn.execute("SELECT * \
			  FROM TABLE_1 \
			  INNER JOIN TABLE_2 \
			  ON TABLE_1.story_id = TABLE_2.story_id ")
query = list(query) 

#Optional Displaying Query With Headers
# print a[0][1], " ", a[1][1], "", a[2][1], a[3][1], b[1][1], b[2][1]
# for i in query:
# 	print i[0], "  ", i[1], "   ", i[2], "     ", i[3], i[5], i[6]


#Looking for "bug" types
user_list = []
for i in query: 
	if i[2] == "bug":
		user_list.append(i[5])
a = Counter(user_list)

list_of_ids = []
for i in a: #iterating through counted Collections object
	if a[i] > 2:
		list_of_ids.append(i) #adding user id to list of id's

for j in list_of_ids:
	count_requested = 0
	count_owned = 0
	for i in query:
		if j == i[5]:
			count_requested += 1
		
		if j == i[6]:
			count_owned += 1
		
	print j, "Total requested:", count_requested
	print j, "Total owned:", count_owned
