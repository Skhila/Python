import requests
import json
import sqlite3

# I
characters_url = 'https://rickandmortyapi.com/api/character'

payload = {'name': 'morty', 'status': 'dead'}
r = requests.get(characters_url, params=payload)
dead_morty_res = r.json()
print(f"Response Date: {r.headers['Date']}")
print(f"Source Server: {r.headers['server']}")
status = r.status_code
if str(status)[0] == '2':
    print(f'success!!, status code: {status} \n')
elif str(status)[0] == '3':
    print(f'Redirection !!, status code: {status} \n')
elif str(status)[0] == '4':
    print(f'Client Error !!, status code: {status} \n')
elif str(status)[0] == '5':
    print(f'Server Error!!, status code: {status} \n')

# print(r.headers)
print(f'There are {len(dead_morty_res["results"])} dead Morties!! \n')

# II - III

res = r.json()
# print(r.text)
# print(json.dumps(res, indent=4))

with open('dead_morties.json', 'w') as dead_morties_data:
    json.dump(res, dead_morties_data, indent=4)

print('Don\'t Forget Them 😢: ')
for each_dead_morty in res['results']:
    print(f"{each_dead_morty['name']}, From \"{each_dead_morty['location']['name']}\","
          f" \"Acted\" in {len(each_dead_morty['episode'])} episodes")

# IV

conn = sqlite3.connect('rm_characters.sqlite')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS rm
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name VARCHAR(50),
                Gender VARCHAR(50),
                Location VARCHAR(100))
                ''')

characters_list = []
char_index = 1
chars_count = r_all_chars = requests.get(characters_url).json()['info']['count']

while char_index <= chars_count:
    characters_url = f'https://rickandmortyapi.com/api/character/{char_index}'
    char_r = requests.get(characters_url).json()
    # characters_res =

    characters_list.append((char_r['name'], char_r['gender'], char_r['location']['name'],))
    char_index += 1


cursor.executemany("INSERT INTO rm (Name, Gender, Location) values (?, ?, ?)", characters_list)
conn.commit()

conn1 = sqlite3.connect('rm_locations.sqlite')
cursor1 = conn1.cursor()

cursor1.execute('''CREATE TABLE IF NOT EXISTS rm_locations
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name VARCHAR(50),
                Dimension VARCHAR(100),
                Population INTEGER)
                ''')


locations_list = []
loc_index = 1
locs_count = requests.get('https://rickandmortyapi.com/api/location').json()['info']['count']


while loc_index <= locs_count:
    locations_url = f'https://rickandmortyapi.com/api/location/{loc_index}'

    loc_r = requests.get(locations_url).json()
    # locations_res = loc_r.json()

    locations_list.append((loc_r['name'], loc_r['dimension'], len(loc_r['residents'])))
    loc_index += 1


cursor1.executemany("INSERT INTO rm_locations (Name, Dimension, Population) values (?, ?, ?)", locations_list)
conn1.commit()

conn2 = sqlite3.connect('rm_dimensions.sqlite')
cursor2 = conn2.cursor()

cursor2.execute('''CREATE TABLE IF NOT EXISTS rm_locations
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name VARCHAR(50),
                Number_of_locations INTEGER)
                ''')

cursor1.execute("SELECT Dimension, COUNT(Dimension) FROM rm_locations GROUP BY Dimension")
dims_list = []

for record in cursor1.fetchall():
    # print(f'Dimension Name: {record[0]}; Number Of Locations: {record[1]} ')
    dims_list.append((record[0], record[1]))

cursor2.executemany("INSERT INTO rm_locations (Name, Number_of_locations) values (?,?)", dims_list)
conn2.commit()
