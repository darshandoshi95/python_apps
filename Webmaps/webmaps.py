
# coding: utf-8

# In[1]:


import pip
pip.main(['install', 'folium'])


# In[21]:


import folium
import pandas


# In[10]:


map=folium.Map(location=[19.1726,72.9425],zoom_start=20)
map.save("map1.html")


# #adding points to map

# In[20]:


map=folium.Map(location=[19.1726,72.9425],zoom_start=6,tiles="Mapbox Bright")
fg=folium.FeatureGroup(name='marker')
fg.add_child(folium.Marker([19.1726,72.9425],popup="Home",icon=folium.Icon(color="green")))
map.add_child(fg)
map.save("map2.html")


# In[22]:


#load locations from a file


# In[25]:


data=pandas.read_csv("/Users/darshandoshi/Desktop/git-repositiories/python_apps/Webmaps/app2-web-map/Volcanoes_USA.txt")


# In[26]:


data


# In[63]:


fg1=folium.FeatureGroup(name='marker')
for row in data.itertuples(index=True, name='Pandas'):
    fg1.add_child(folium.Marker([getattr(row, "LAT"),getattr(row, "LON")],popup=str(getattr(row,"ELEV")),icon=folium.Icon(color(getattr(row,"ELEV")))))
    map.add_child(fg1)
map.save("map3.html")


# In[68]:


def color_produce(elev):
    if elev<2000:
        return "green"
    elif  2000<elev<4000:
        return "orange"
    else:
        return "red"
    


# In[60]:


dir(folium)


# In[62]:


help(folium.Circle)


# In[78]:


map1=folium.Map(location=[48.776798,-121.810997],zoom_start=6,tiles="Mapbox Bright")
fg2=folium.FeatureGroup(name='marker')
for row in data.itertuples(index=True, name='Pandas'):
    fg2.add_child(folium.CircleMarker([getattr(row, "LAT"),getattr(row, "LON")],radius=6,color="grey",fill_color=color_produce(getattr(row,"ELEV")),popup=str(getattr(row,"ELEV")),fill_opacity=0.7,fill=True))

fg2.add_child(folium.GeoJson(data=open("/Users/darshandoshi/Desktop/git-repositiories/python_apps/Webmaps/app2-web-map/world.json",'r',encoding="utf-8-sig").read(),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<20000000 
                         else 'yellow' if 2000000 < x['properties']['POP2005'] < 40000000
                        else 'red'}))
map1.add_child(fg2)
map1.save("map4.html")


# In[ ]:




