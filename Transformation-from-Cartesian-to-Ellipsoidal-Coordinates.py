# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 14:29:18 2022

@author: Asus
# """
# Adilhan KOÇAK 2200674035 
# 21.12.2022
#This function be able to Transformation from Cartesian to Ellipsoidal Coordinates.Fırst ı solve a radıan format this question finally ı convert a degree format.
#INPUT = [X,Y,Z] COORDINATES OF CARTESIAN COORDINATE SYSTEM
#OUTPUT = [LATITUDE,LONGITUDE,HEİGHT] COORDINATES OF ELLIPSOIDAL COORDINATE SYSTEM
#X,Y,Z and HEIGHT ======> meters format
#LATITUDE,LONGITUDE ======> degree format
import math
#I defined parameters of GRS80 ellipsoid.
ax = 6378137.0
bx = 6356752.3141
#create a function be able to ,Transformation from Cartesian to Ellipsoidal Coordinates.
def xyz2blh(x,y,z):
    #ı defined eccentricity.
    e = math.sqrt(1 - (bx**2)/(ax**2))
    #ı defined a formula of latitude(RADIAN FORMAT)
    lon = math.atan2(y, x)
    #ı defined a formula of longitude(RADIAN FORMAT)
    lat = math.atan(z / math.hypot(x, y))
    #I defined start point with respect to latitude for iterative solution 
    lat0 = 0
    #For iterative solution with while loop "abs(lat-lat0) ====> for good values of latitude values" 
    while (abs(lat - lat0) >  10**-12):
        
        lat0 = lat
        N = ax / math.sqrt(1 - e**2 * math.sin(lat0)**2)
        lat = math.atan((z + e**2 * N * math.sin(lat0)) / math.hypot(x, y))
        
    #get new N values
    N = ax / (math.sqrt(1 - e**2 * math.sin(lat)**2))
    #ı found a height values with new lat and N values
    height = math.sqrt(x**2+y**2)/math.cos(lat) - N
    #convert lon and lat degree format.
    # lon = math.degrees(lon)
    # lat = math.degrees(lat)
    #return values
    return [lat,lon,height]

a = xyz2blh(4208830.726  ,2334850.0235  ,4171267.089)
print(a)
#round a apporximate values 
# print([math.ceil(a[0]),math.ceil(a[1]),math.ceil(a[2])])
