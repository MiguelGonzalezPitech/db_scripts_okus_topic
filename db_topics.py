import pymysql
import sys

db = pymysql.connect(
    'okus.cz8dcgq2qxno.us-east-1.rds.amazonaws.com',
    'pitech_master',
    'HiKrKiNMivS5ynHiKr')
cursor = db.cursor()

query = """
select 
	T.id as Topic_id,
	S.id as Sub_id,
	T.name as Topic_Name,
	S.name as Sub_Name
from productionDummy.topics T
inner join productionDummy.subtopics S on T.id = S.topic_id
where T.id = {0}
"""



for topic_id in sys.argv[1:]:
    cursor.execute(query.format(topic_id))

    result = cursor.fetchall()
    topic_id = result[0][0]
    topic_name = result[0][2]
    print('topic id: {0}; topic name: {1}'.format(topic_id,topic_name))
    for row in result:
        print('|-->subtopic name: {0}'.format(row[3]))