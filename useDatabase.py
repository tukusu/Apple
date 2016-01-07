 #!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('dataset/station.db')
cur = conn.cursor()

cur.execute("""SELECT name,address FROM station;""")

for name,address in cur.fetchall():
	print u"駅名:%s    住所:%s" % (name,address)