def lonlat2xyz(lat, lon):
    x=[]
    y=[]
    for time in range(0,len(lat)):
        latitude=lat[time]
        longitude=lon[time]
        
        # WGS84 ellipsoid constants:
        a = 6378137
        e = 8.1819190842622e-2
        #Urbana Altitude in meters
        altitude = 222
        #(prime vertical radius of curvature)
        N = a / math.sqrt(1 - e*e * math.sin(math.radians(latitude))* math.sin(math.radians(latitude)))
        x.append((N+altitude) * math.cos(math.radians(latitude)) * math.cos(math.radians(longitude)))
        y.append((N+altitude) * math.cos(math.radians(latitude)) * math.sin(math.radians(longitude)))
        #z = ((1-e*e) * N + altitude) * math.sin(math.radians(latitude))
    
    minx = min(x)
    miny = y[x.index(minx)]
    
    for t in range(0, len(x)):
        x[t] = x[t]-minx
        y[t] = y[t]-miny
    
    return x, y
