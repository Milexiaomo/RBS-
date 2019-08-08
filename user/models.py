import sys
sys.path.append(r"F:\RBS")

from Tool.tool_db import DB
class Personal():

    def personal_data(self):
        sql="select * from personal"
        data=DB.query_sql(sql,())
        return data
