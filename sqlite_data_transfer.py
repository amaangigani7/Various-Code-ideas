import sqlite3

conn = sqlite3.connect('F:\\udemy.django\\git_repo\\db.sqlite3')
cur = conn.cursor()

cur.execute('SELECT title FROM light_novel_scratchpad')
rows = cur.fetchall()

cur.execute('SELECT content FROM light_novel_scratchpad')
content = cur.fetchall()

# for i in content:
#     print(i[:10])
for i in range(len(rows)):
    with open('F:\\udemy.python\\imp_python_codes\\{}'.format(rows[i][0]), 'w') as f:
        f.write(content[i][0])
#     print(row)
# for i in rows:
#     print(i[0])
