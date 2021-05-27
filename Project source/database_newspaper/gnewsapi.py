#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[182]:


import requests
import pandas as pd
import sidetable
import json
from pandas import json_normalize
from datetime import date
import time
from newsapi import NewsApiClient
import logging
import re


# In[4]:


today = date.today()
day = today.strftime("%d_%m_%Y")


# In[5]:


day


# In[6]:


print(today)


# # API's

# ## Gnews API

# In[7]:


url = "https://gnews.io/api/v4/top-headlines"

#different topic: breaking-news, world, nation, business, technology, entertainment, sports, science and health.
breaking = {"topic":"breaking-news","country":"ch","lang":"de","token":"put your token here"}
world = {"topic":"world","country":"ch","lang":"de","token":"put your token here"}
nation = {"topic":"nation","country":"ch","lang":"de","token":"put your token here"}
business = {"topic":"business","country":"ch","lang":"de","token":"put your token here"}
technology = {"topic":"technology","country":"ch","lang":"de","token":"put your token here"}
entertainment = {"topic":"entertainment","country":"ch","lang":"de","token":"put your token here"}
sports = {"topic":"sports","country":"ch","lang":"de","token":"put your token here"}
science = {"topic":"science","country":"ch","lang":"de","token":"put your token here"}
health = {"topic":"health","country":"ch","lang":"de","token":"put your token here"}

payload = ""
headers = {'cookie': 'PHPSESSID=put your PHPSESSID here'}

response_breaking = requests.request("GET", url, data=payload, headers=headers, params=breaking)
time.sleep(2)
response_world = requests.request("GET", url, data=payload, headers=headers, params=world)
time.sleep(2)
response_nation = requests.request("GET", url, data=payload, headers=headers, params=nation)
time.sleep(2)
response_business = requests.request("GET", url, data=payload, headers=headers, params=business)
time.sleep(2)
response_technology = requests.request("GET", url, data=payload, headers=headers, params=technology)
time.sleep(2)
response_sports = requests.request("GET", url, data=payload, headers=headers, params=sports)
time.sleep(2)
response_science = requests.request("GET", url, data=payload, headers=headers, params=science)
time.sleep(2)
response_health = requests.request("GET", url, data=payload, headers=headers, params=health)
time.sleep(2)
response_entertainment = requests.request("GET", url, data=payload, headers=headers, params=entertainment)
time.sleep(2)


# In[8]:


gnews_breaking = json.loads(response_breaking.text)
gnews_world= json.loads(response_world.text) 
gnews_nation= json.loads(response_nation.text)
gnews_business= json.loads(response_business.text) 
gnews_technology= json.loads(response_technology.text) 
gnews_sports= json.loads(response_sports.text) 
gnews_science= json.loads(response_science.text) 
gnews_health= json.loads(response_health.text)
gnews_entertainment= json.loads(response_entertainment.text)


# ## NewsApi

# In[9]:


# Init
newsapi = NewsApiClient(api_key='put your token here')


# ### Category

# In[10]:


# /category business entertainment general health science sports technology
business = newsapi.get_top_headlines(category='business', language='de', country='ch')
time.sleep(2)
entertainment = newsapi.get_top_headlines(category='entertainment', language='de', country='ch')
time.sleep(2)
general = newsapi.get_top_headlines(category='general', language='de', country='ch')
time.sleep(2)
health = newsapi.get_top_headlines(category='health', language='de', country='ch')
time.sleep(2)
science = newsapi.get_top_headlines(category='science', language='de', country='ch')
time.sleep(2)
sports = newsapi.get_top_headlines(category='sports', language='de', country='ch')
time.sleep(2)
technology = newsapi.get_top_headlines(category='technology', language='de', country='ch')
time.sleep(2)


# # Create dataframe

# ## Categories GNewsAPI

# In[11]:


'''gnews_breaking 
gnews_world
gnews_nation
gnews_business
gnews_technology
gnews_science
gnews_health
gnews_entertainment'''


# In[480]:


df_gworld = json_normalize(gnews_world,record_path = ['articles'])
df_gnation = json_normalize(gnews_nation,record_path = ['articles'])
df_gbusiness = json_normalize(gnews_business,record_path = ['articles'])
df_gentertainment = json_normalize(gnews_entertainment,record_path = ['articles'])
df_gbreaking  = json_normalize(gnews_breaking,record_path = ['articles'])
df_ghealth = json_normalize(gnews_health,record_path = ['articles'])
df_gscience = json_normalize(gnews_science,record_path = ['articles'])
df_gsports = json_normalize(gnews_sports,record_path = ['articles'])
df_gtechnology = json_normalize(gnews_technology,record_path = ['articles'])


# ## Categories NewsAPI

# In[481]:


df_business = json_normalize(business,record_path = ['articles'])
df_entertainment = json_normalize(entertainment,record_path = ['articles'])
df_general = json_normalize(general,record_path = ['articles'])
df_health = json_normalize(health,record_path = ['articles'])
df_science = json_normalize(science,record_path = ['articles'])
df_sports = json_normalize(sports,record_path = ['articles'])
df_technology = json_normalize(technology,record_path = ['articles'])


# # Clean NewsAPI DF

# In[483]:


def postfix_title(title):
    return title.rsplit(' - ',1)[0]
   
def double_title(title):
    return postfix_title(postfix_title(title))

def noop(title):
    return title


# In[484]:


SOURCES = {
    '20 Minuten': postfix_title,
    'Www.nau.ch': postfix_title,
    'Blick.ch': postfix_title,
    'Tagesanzeiger.ch': postfix_title,
    'Telebasel.ch': postfix_title,
    'Bluewin.ch': postfix_title,
    'Www.gmx.ch': postfix_title,
    'Www.vox.de': postfix_title,
    'Finews.ch': postfix_title,
    'Watson.ch': postfix_title,
    'Www.srf.ch': postfix_title,
    'Goldreporter.de': postfix_title,
    'Aerotelegraph.com': postfix_title,
    'Cointelegraph': postfix_title,
    'Heilpraxisnet.de': postfix_title,
    'Tagblatt.ch': postfix_title,
    'Herisau24.ch': postfix_title,
    'CHIP Online Deutschland': postfix_title,
    'heise online': postfix_title,
    'Aponet.de': postfix_title,
    'DIE WELT': postfix_title,
    'Frankfurt-live.com': postfix_title,
    'Presseportal.de': postfix_title,
    'Augsburger Allgemeine': postfix_title,
    'Puls24.at': postfix_title,
    'Achgut.com': postfix_title,
    'Seniorweb.ch': postfix_title,
    'B.Z. Berlin': postfix_title,
    't-online.de': postfix_title,
    'Faz.net': double_title,
    'futurezone.at': postfix_title,
    'Businessinsider.de': postfix_title,
    'Krone.at': postfix_title,
    'Bernerzeitung.ch': postfix_title,
    'Herzeblog.de': postfix_title,
    'Aargauerzeitung.ch': postfix_title,
    'Spiegel Online': postfix_title,
    'Focus': postfix_title,
    'Spiegel Online': postfix_title,
    'Wirtschafts Woche': postfix_title,
    'Google News': postfix_title,
    'T3n': postfix_title,
    'Bild': postfix_title,
    'Motorsport-total.com': postfix_title,
    'Speedweek.com': postfix_title,
    'Btc-echo.de': postfix_title,
    'ComputerBase': postfix_title,
    'derStandard.at': postfix_title,    
    'Itmagazine.ch': double_title,
    'Cryptoticker.io': double_title,
    'n-tv NACHRICHTEN': double_title,
    'DER AKTIONÄR': double_title,
    'scinexx | Das Wissensmagazin': double_title,
    'FAZ - Frankfurter Allgemeine Zeitung': double_title,
}



# In[486]:


def cleanup_title(source, title):
    if source not in SOURCES:
        logging.warn("Unknown source %s, leaving as-is", source)
        print("'"+source+"': postfix_title,")
		#SOURCES.update({source: postfix_title})
    return SOURCES.get(source, noop)(title)


# In[487]:


def clean_dataframe(df):
    # clean title from '- newspaper Name'
    title_apply = df.apply(
        lambda row : cleanup_title(row['source.name'], row['title']),
        axis = 1
    )
    # reassign column title
    df['title'] = title_apply
    return df


# In[488]:


df_business = clean_dataframe(df_business)
df_entertainment = clean_dataframe(df_entertainment)
df_general= clean_dataframe(df_general)
df_health = clean_dataframe(df_health)
df_science = clean_dataframe(df_science)
df_sports = clean_dataframe(df_sports)
df_technology = clean_dataframe(df_technology)


# # Clean Frame

# In[489]:


frames_world = [] 
frames_nation = [] 
frames_business = [] 
frames_technology = [] 
frames_entertainment = [] 
frames_sports = [] 
frames_science = []
frames_health = []


# In[490]:


def clean_df(df, frames, category: str):
    if len(df)>0:
        df = df[['source.name', 'title','description','publishedAt']]
        header_list = ['source.name', 'title','description','category','publishedAt']
        df = df.reindex(columns = header_list)   
        df['category'] = category
        df = df.rename(columns={'source.name':'source'})
        df = df[df['source'].notnull()]
        df = df[df['title'].notnull()]
        df = df[df['description'].notnull()]
        
        frames.append(df)
        return df
    else:
        print(df,"Empty")


# # Categories

# ## World

# In[491]:


world1 = clean_df(df_gworld,frames_world, "world") 
world2 = clean_df(df_gbreaking,frames_world, "world") 
world3  = clean_df(df_general,frames_world, "world") 
df_world= pd.concat(frames_world,ignore_index=True)
len(df_world)


# In[492]:


df_world= df_world.drop_duplicates(subset=['description'],ignore_index=True)
len(df_world)


# ## Nation

# In[495]:


df_nat = clean_df(df_gnation,frames_nation, "nation")


# In[496]:


len(df_nat)


# ## Business

# In[498]:


bus1= clean_df(df_business,frames_business,"business")
bus2= clean_df(df_gbusiness,frames_business, "business")
df_bus= pd.concat(frames_business,ignore_index=True)
len(df_bus)


# In[499]:


df_bus= df_bus.drop_duplicates(subset=['description'],ignore_index=True)
len(df_bus)


# ## Technology

# In[501]:


technology1 = clean_df(df_gbreaking ,frames_technology,"technology") 
technology2 = clean_df(df_gtechnology,frames_technology, "technology") 
df_tech= pd.concat(frames_technology,ignore_index=True)
len(df_tech)


# In[502]:


df_tech= df_tech.drop_duplicates(subset=['description'],ignore_index=True)
len(df_tech)


# ## Entertainment

# In[504]:


ent1 = clean_df(df_entertainment,frames_entertainment, "entertainment") 
ent2 = clean_df(df_gentertainment,frames_entertainment, "entertainment") 
df_ent= pd.concat(frames_entertainment,ignore_index=True)
len(df_ent)


# In[505]:


df_ent= df_ent.drop_duplicates(subset=['description'],ignore_index=True)
len(df_ent)


# ## Sports

# In[507]:


sport1 = clean_df(df_sports,frames_sports,"sport") 
sport2 = clean_df(df_gsports,frames_sports,"sport") 
df_sport= pd.concat(frames_sports,ignore_index=True)
len(df_sport)


# In[508]:


df_sport= df_sport.drop_duplicates(subset=['description'],ignore_index=True)
len(df_sport)


# ## Science

# In[42]:


science1 = clean_df(df_science,frames_science,"science") 
science2 = clean_df(df_gscience,frames_science, "science") 
df_scnc= pd.concat(frames_science,ignore_index=True)
len(df_scnc)


# In[43]:


df_scnc= df_scnc.drop_duplicates(subset=['description'],ignore_index=True)
len(df_scnc)


# ## Health

# In[45]:


health1 = clean_df(df_health,frames_health, "health") 
health2 = clean_df(df_ghealth,frames_health, "health") 
df_hlth= pd.concat(frames_health,ignore_index=True)
len(df_hlth)


# In[46]:


df_hlth= df_hlth.drop_duplicates(subset=['description'],ignore_index=True)
len(df_hlth)


# # Total

# In[59]:


frames = [df_world,df_nat,df_bus,df_tech,df_ent,df_sport,df_scnc,df_hlth]


# In[60]:


df_total = pd.concat(frames,ignore_index=True)
len(df_total)


# In[62]:


df_total = df_total.drop_duplicates(subset=['description'])
len(df_total)


# # Export

# In[ ]:


df_total.to_csv(r'.\Project source\database_newspaper\total\total' + day + '.csv', index=False)
df_world.to_csv(r'.\Project source\database_newspaper\world\world' + day + '.csv', index=False)
df_nat.to_csv(r'.\Project source\database_newspaper\nation\nation' + day + '.csv', index=False)
df_bus.to_csv(r'.\Project source\database_newspaper\business\business' + day + '.csv', index=False)
df_tech.to_csv(r'.\Project source\database_newspaper\technology\technology' + day + '.csv', index=False)
df_ent.to_csv(r'.\Project source\database_newspaper\entertainment\entertainment' + day + '.csv', index=False)
df_sport.to_csv(r'.\Project source\database_newspaper\sport\sport' + day + '.csv', index=False)
df_scnc.to_csv(r'.\Project source\database_newspaper\science\science' + day + '.csv', index=False)
df_hlth.to_csv(r'.\Project source\database_newspaper\health\health' + day + '.csv', index=False)

print("Exported! In date " + day)

