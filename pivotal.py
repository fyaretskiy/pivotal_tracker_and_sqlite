#first figure out the connection
#check if table exists
#have commands to create and update utilizing the tutorial 
#from new coder
#need to use kargs to show data


import api_key
import sqlite3
import requests


api_token = api_key.api_token
project_id = api_key.project_id
url = "https://www.pivotaltracker.com/services/v5/projects/{0}/stories".format(project_id)

def create_TABLES(database):
	"""Creates all the tables and fills out table 3."""
	conn = sqlite3.connect(database)
	try:
		conn.execute('''CREATE TABLE TABLE_1
        (story_id INTEGER PRIMARY KEY     NOT NULL,
        story_name     TEXT	     ,
        story_type     TEXT	,
        estimate         INTEGER 	);''')
	except:
		pass
	try:
		conn.execute('''CREATE TABLE TABLE_2
    	(story_id INT PRIMARY KEY     NOT NULL,
    	requested_by_id     TEXT     ,
        owner_id     TEXT);''')
	except:
		pass
	try:
		conn.execute('''CREATE TABLE TABLE_3
    	(user_id INT PRIMARY KEY     NOT NULL,
        user_name     TEXT);''')
	except:
		pass

	try:
		conn.execute("INSERT INTO TABLE_3 (user_id, user_name) \
		VALUES (1462570, 'XY')");
	except:
		pass
	try:
		conn.execute("INSERT INTO TABLE_3 (user_id, user_name) \
		VALUES (1420764, 'PA')");
	except:
		pass
	conn.commit()
	conn.close()




def view_table_generic(database, table):
	"""View Any table"""
	conn = sqlite3.connect(database)
	cursor = conn.execute("SELECT * from {0}".format(table))
	for row in cursor:
		print row
	conn.close()


def view_table_1(database):
	"""View table 1"""
	conn = sqlite3.connect(database)
	cursor = conn.execute("SELECT * from TABLE_1")
	print "__________________Table 1:_________________________"
	for row in cursor:
		print "| Story ID:", row[0], "| Story Name:", row[1], "| Story Type:", row[2], "| Estimate:", row[3]
	conn.close()
	
def view_table_2(database):
	"""View table 2"""
	conn = sqlite3.connect(database)
	cursor = conn.execute("SELECT * from TABLE_2")
	print "__________________Table 2:_________________________"
	for row in cursor:
		print "| Story ID:", row[0], "| Request by ID:", row[1], "| User ID:", row[2]
	conn.close()
	

def retrieve_all_tables(database):
	"""Retrieves all the tables in the database"""
	conn = sqlite3.connect(database)
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
	print(cursor.fetchall())
	conn.close()


def update_table_1(database):
	"""Updates table 1"""
	r = requests.get(url, headers={'X-TrackerToken':api_token})
	json_list = r.json()
	
	conn = sqlite3.connect(database)
	
	for i in json_list:
		story_id = int(i["id"])
		try:
			story_name = str(i["name"])
		except KeyError:
			story_name = NULL
		try:
			story_type = str(i["story_type"]) 
		except KeyError:
			story_type = NULL
		try:
			story_estimate = int(i["estimate"])
		except KeyError:
			story_estimate = int(0)

		the_tuple = (story_id, story_name, story_type, story_estimate)
		try:
			conn.execute("""insert into TABLE_1 values (?,?,?,?)""", (the_tuple))
		except:
			pass
		conn.commit()
		
	conn.close()

def update_table_2(database):
	"Updates table 2"
	r = requests.get(url, headers={'X-TrackerToken':api_token})
	json_list = r.json()
	
	conn = sqlite3.connect(database)
	
	for i in json_list:
		story_id = int(i["id"])
		try:
			requested_by_id = str(i["requested_by_id"])
		except KeyError:
			requested_by_id = NULL
		try:
			owner_ids = str(i["owner_ids"]) 
		except KeyError:
			owner_ids = NULL
		
		the_tuple = (story_id, requested_by_id, owner_ids)
		try:
			conn.execute("""insert into TABLE_2 values (?,?,?)""", (the_tuple))
		except:
			pass
		conn.commit()
		
	conn.close()



if __name__ == "__main__":
	create_TABLES("database.db")
	# retrieve_all_tables("database.db")
	update_table_1("database.db")
	update_table_2("database.db")
	# view_table_generic("database.db", "TABLE_1")
	# view_table_generic("database.db", "TABLE_2")
	view_table_1("database.db")
	view_table_2("database.db")

# r = requests.get(url, headers={'X-TrackerToken':api_token})
# json_list = r.json()
	
# conn = sqlite3.connect("database.db")
	
	
