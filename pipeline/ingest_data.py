#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm


# In[12]:


prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
data = f'{prefix}yellow_tripdata_2021-01.csv.gz'
data


# In[14]:


df = pd.read_csv(data)


# In[15]:


df.head()


# In[16]:


df.describe()


# In[18]:


len(df)


# In[19]:


df['VendorID']


# In[20]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    data,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[21]:


df.head()


# In[22]:


df['tpep_pickup_datetime']


# In[25]:


get_ipython().system('uv add sqlalchemy')


# In[27]:


get_ipython().system('uv add psycopg2-binary')


# In[31]:



engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[34]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[35]:


df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[39]:


df_iter = pd.read_csv(
    data,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000,
)


# In[44]:





# In[50]:


for df_chunk in df_iter:
    print(len(df_chunk))


# In[52]:


df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')


# In[53]:


first = True

for df_chunk in df_iter:

    if first:
        # Create table schema (no data)
        df_chunk.head(0).to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="replace"
        )
        first = False
        print("Table created")

    # Insert chunk
    df_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append"
    )

    print("Inserted:", len(df_chunk))


# In[54]:




for df_chunk in tqdm(df_iter):
    ...


# In[55]:


uv run pgcli -h localhost -p 5432 -u root -d ny_taxi


# In[ ]:




