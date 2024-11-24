from dotenv import load_dotenv
import os
load_dotenv()

user=os.environ['USER']
pwd=os.environ['PASSWORD']
host=os.environ['HOST']
database=os.environ['DATABASE']
server=os.environ['SERVER']
DATABASE_CONNECTION = 'postgresql://sisvita_user:xwjtQgxHA0uws48NJbq1qn2qDHQp6fIq@dpg-ct1aqou8ii6s73fe6q20-a.oregon-postgres.render.com/sisvita_6sgi'