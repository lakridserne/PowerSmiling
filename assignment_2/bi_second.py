# ### 1. Read the entire dataset of Danish housing sales data, from Boliga, into a Pandas DataFrame. Use the read_csv function from the pandas module.
#


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json, csv
import math



housing = pd.read_csv("./git/boliga_all.csv")

#housing.head()


len(housing)

housing.shape


# ### 2. Geocode the the entire dataset of Danish housing sales data. Add two new columns to the DataFrame, one for latitude (lat) and one for longitude (lon) coordinates per address. Do the geocoding with help of the OSM dataset stored in a file as discussed in class. Save that DataFrame to a CSV file with the help of pandas'


"""from osmread import parse_file, Node


def decode_node_to_csv():
    for entry in parse_file('./dkosmdata/denmark-latest.osm'):
        if (isinstance(entry, Node) and
            'addr:street' in entry.tags and
            'addr:postcode' in entry.tags and
            'addr:housenumber' in entry.tags):

            yield entry

dicts ={}
arrcity = []
arrzip = []
arrstreet = []
lat = []
lon =[]

for idx, decoded_node in enumerate(decode_node_to_csv()):
    #if idx > 1000000:
    #    break

    for a, b in decoded_node[5].items():

        if a == 'addr:city':
            city = b
        if a == 'addr:housenumber':
            number = b
        if a == 'addr:postcode':
            zipcode = b
        if a == 'addr:street':
            street = b, number

    arrcity.append(city)
    arrzip.append(zipcode)
    arrstreet.append(street)
    lon.append(decoded_node[6])
    lat.append(decoded_node[7])
    #print(city, zipcode, street, decoded_node[6], decoded_node[7])

dicts = {"city":arrcity, "zipcode": arrzip, "street": arrstreet, "longitude":lon ,"latitude":lat}


  """


# saving the dicts containing the 4 lists into pandas dataframe, and save it as csv file
#df = pd.DataFrame(dicts)
#df.to_csv('newpostcodedenmark2.csv', mode='a')


# #### Reading the newly created csv file and Geocoding the original dataset (housing).
# #### The following steps explains the data cleaning and preparing process



newDataframe = pd.read_csv("newpostcodedenmark2.csv", index_col=False)


arrData = np.array(newDataframe.street)



def cleanstreet(street):
    #result = street.find('(')
    street = street.replace('\'','')
    street = street.replace('(','')
    street = street.replace(')','')
    street = street.split(",")

    #int(street)
    street = street[0] + "" + str(street[1])
    return street

#cleanstreet(arrData[0])

cleanstreets = []
for data in arrData:
    cleanstreets.append(cleanstreet(data))

newDataframe['street'] = cleanstreets
print("done")



newDataframe.head()

housing.head()

housing['longitude'] = ''
housing['latitude'] =''

housing.columns

addresslist = []
print("data loaded")
for index, house in housing.iterrows():

    address = house['address'].split(",")[0] + " " + house['zip_code'].split(" ")[0]
    addresslist.append(address)

print("first part done")
print(addresslist[0])


newDatalist =[]
c = 0
for index, house in newDataframe.iterrows():
        addr = house['street'] + " " + str(house['zipcode'])
        newDatalist.append(addr)

newDataframe['street'] = newDatalist

housing['address'] = addresslist

print(housing.head())

#housing[housing[housing.address].isin(newDatalist)]
housing[housing.address.isin(newDatalist)] #it seems to find data

# inserting the latitude to housing dataframe
#housing.loc[housing.address.isin(newDatalist), 'latitude'] = newDataframe['latitude']

# inserting the longitude to housing dataframe
#housing.loc[housing.address.isin(newDatalist), 'longitude'] = newDataframe['longitude']


housing


#housing.to_csv('finaldenmarkdata.csv', mode='a')


# ### 3. Convert all sales dates in the dataset into proper datetime objects, see http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html.

dataframe = pd.read_csv("finaldenmarkdata.csv", index_col=False)



dataframe.head()


newdate = pd.to_datetime(housing.sell_date)


housing['sell_date'] = newdate


housing.head()


# ### 4. Compute the average price per square meter for the years 1992 and 2016 respectively for the city centers of Copenhagen (zip code 1050-1049), Odense (zip code 5000), Aarhus (zip code 8000), and Aalborg (zip code 9000). Create two new DataFrames, one for the year 1992 and one for the year 2016, which contain the respective zip codes and the average price per square meter corresponding to the aforementioned cities. Let the DataFrames be sorted by ascending prices.


housing['sell_date'].values


dates = pd.DatetimeIndex(housing.sell_date)


years = dates.year
housing['sell_year'] = years
#housing['sell_year']



year92 = housing[(housing['sell_year']==1992) & (housing['zip_code'].isin(['1050 København K','1049 København K',
                                                                          '5000 Odense C','8000 Aarhus C','9000 Aalborg']))]


year16 = housing[(housing['sell_year']==2016) & (housing['zip_code'].isin(['1050 København K','1049 København K',
                                                                          '5000 Odense C','8000 Aarhus C','9000 Aalborg']))]


#average price for 1992 (København, Odense, Aarhus, Aalborg)
year92.price_per_sqm.mean()


#average price for 2016 (København, Odense, Aarhus, Aalborg)
year16.price_per_sqm.mean()


# creating 2 new dataframe for 1992 and 2016
dframe92 = {"zipcode":year92.zip_code,"sq_prices": year92.price_per_sqm}
dframe16 = {"zipcode":year16.zip_code,"sq_prices": year16.price_per_sqm}

df92 = pd.DataFrame(dframe92)
df16 = pd.DataFrame(dframe16)

#df92.to_csv('data1992.csv', mode='a')
#df16.to_csv('data2016.csv', mode='a')


# ### 5. Create, with the help of the pandas module, four new CSV files containing the sales data for the year 1992 for the city centers of Copenhagen (zip code 1050-1499), Odense (zip code 5000), Aarhus (zip code 8000), and Aalborg (zip code 9000).


citycenter = []
for index, house in housing.iterrows():

    zipcode = house['zip_code'].split(" ")[0]
    if zipcode>='1050' and zipcode<'1499':
        citycenter.append(zipcode)

cph92 = housing[(housing['sell_year']==1992) & (housing['zip_code'].isin(citycenter))]

odense92 = housing[(housing['sell_year']==1992) & (housing['zip_code'].isin(['5000 Odense C']))]

aarhus92 = housing[(housing['sell_year']==1992) & (housing['zip_code'].isin(['8000 Aarhus C']))]

aalborg92 = housing[(housing['sell_year']==1992) & (housing['zip_code'].isin(['9000 Aalborg']))]


"""
cph92.to_csv('cph1992.csv', mode='a')
odense92.to_csv('odense1992.csv', mode='a')
aarhus92.to_csv('aarhus1992.csv', mode='a')
aalborg92.to_csv('aalborg1992.csv', mode='a')
"""
df = dataframe

# ### 6. Create a 2-dimensional scatter plot, which contains a dot for each location in the dataset of Danish housing sales data. Plot the longitude values on the x- axis and plot the latitude values on the y-axis.

cols = ['year_of_construction','price_per_sq_m']
df[cols].plot(kind='scatter', x='year_of_construction',y='price_per_sq_m')


# ### 7. Use the following function, which computes the Haversine Distance (https://en.wikipedia.org/wiki/Haversine_formula) to compute an array of distances (distances) for each for each location in the dataset of Danish housing sales data to the city center of Roskilde (lat=55.65, lon=12.083333).
distances = []
destination = 55.65, 12.083333
def haversine_distance(origin, destination):

    lat_orig, lon_orig = origin
    lat_dest, lon_dest = destination
    radius = 6371

    dlat = math.radians(lat_dest-lat_orig)
    dlon = math.radians(lon_dest-lon_orig)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat_orig))
        * math.cos(math.radians(lat_dest)) * math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d



for index, data in df.iterrows():
    origin = data['latitude'],data['longitude']
    distances.append(haversine_distance(origin,destination))
print(distances)
