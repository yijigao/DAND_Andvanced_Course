import sqlite3
import pandas as pd

db = sqlite3.connect("C:\\Users\\yijig\\Desktop\\Advanced course\\sqlite_windows\\Chengdu.db")
c = db.cursor()

QUERY = """
SELECT tags.value, COUNT(*) as count
FROM (SELECT * FROM nodes_tags
UNION ALL 
SELECT * FROM ways_tags) tags
WHERE tags.key = "postcode"
GROUP BY tags.value
ORDER BY count DESC
;
"""
QUERY_CITY = """
SELECT tags.value, COUNT(*) as count
FROM (SELECT * FROM nodes_tags UNION ALL
SELECT * FROM ways_tags) tags
WHERE tags.key LIKE '%city'
GROUP BY tags.value
ORDER BY count DESC;
"""
QUERY_Total_nodes ="""
SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags
JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='restaurant') i
ON nodes_tags.id=i.id
WHERE nodes_tags.key='cuisine'
GROUP BY nodes_tags.value
ORDER BY num DESC;
"""
QUERY_Test = """
SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags
JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='restaurant')
i
ON nodes_tags.id=i.id
WHERE nodes_tags.key='cuisine'
GROUP BY nodes_tags.value
ORDER BY num DESC
LIMIT 10;
"""

c.execute(QUERY_Test)
rows = c.fetchall()
df = pd.DataFrame(rows)
print(df)

db.close()