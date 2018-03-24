origin = input("Where are you?:").replace(" ", "+")
destination = input("Where do you want to go?:").replace(" ", "+")
departure = input("What time are you starting?:")
arrival = input("What time do you want to be there by?:")


def return_traffic_analysis(origin,destination,departure,arrival):
    import urllib.request, json, time

    endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    api_key = "AIzaSyBTr-wJwTkr6VUt3xboaCyZBtQk_ST_GHY"
    departure_hour = departure.split(":")[0]
    departure_minute = departure.split(":")[1]
    departure_time = float(departure_hour+"."+departure_minute)

    arrival_hour = arrival.split(":")[0]
    arrival_minute = arrival.split(":")[1]
    arrival_time = float(arrival_hour+"."+arrival_minute)
    dict_time = {}
    best_time = 0;
    a = 0;
    while departure_time < arrival_time:
        nav_request = 'origins={}&destinations={}&departure_time={}&mode={}&traffic_model={}&key={}'.format(origin,destination,int(time.mktime(time.strptime('2018-03-24 ' + departure + ":00",'%Y-%m-%d %H:%M:%S'))), "driving","best_guess", api_key)
        request = endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        data = json.loads(response)
        output = (data['rows'][0]['elements'][0]['duration_in_traffic']["text"])
        time_hour = output.replace(" mins", "")
        time_hour = time_hour.replace(" hour ", ".")
        time_hour = time_hour.replace(" hours ", ".")
        time_hour = time_hour.replace(" min", "")
        # time_hour = time_hour.replace(":", ".")
        time_hour = float(time_hour)
        num = departure_time+time_hour
        if (num-int(num)) >= 0.6:
            num += 1.0
            num = num - 0.6
            num = round(num, 2)
        if (num)<arrival_time:
            dict_time[departure_time] = time_hour
        departure_time += 0.25
        departure_time = round(departure_time, 2)
        if (departure_time-int(departure_time)) >= 0.6:
            departure_time += 1.0
            departure_time = departure_time - 0.6
            departure_time = round(departure_time, 2)

        departure = str(departure_time).replace(".", ":")

    departure_time = float(departure_hour+"."+departure_minute)
    best_time = departure_time
    if dict_time.values() == 0.0:
         print ("You cannot reach to your destination within the time limit you have sent")
    else:
        lowest = dict_time[departure_time]
        for v in dict_time.values():
            if dict_time[departure_time] <= lowest:
                lowest = dict_time[departure_time]
                best_time = departure_time
            departure_time += 0.25
            departure_time = round(departure_time, 2)
            if (departure_time - int(departure_time)) >= 0.6:
                departure_time += 1.0
                departure_time = departure_time - 0.6
                departure_time = round(departure_time, 2)

        print(best_time)





return_traffic_analysis(origin,destination,departure,arrival)
# print(destination_address)
# print(origin_address)

# # def return_weather_analysis(origin,destination):
#     import urllib.request, json, time
#
#     endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?"
#     api_key = "AIzaSyBTr-wJwTkr6VUt3xboaCyZBtQk_ST_GHY"
#     nav_request = 'origins={}&destinations={}&key={}'.format(origin,destination,api_key)
#     request = endpoint + nav_request
#     response = urllib.request.urlopen(request).read()
#     data = json.loads(response)
#
#     print(data)

    # endpoint = "http://api.openweathermap.org/data/2.5/weather?id=524901&APPID={APIKEY}"
    # api_key = "2fe8527826c3ba5ef45eee23d075f47b"

#18205 Warbler Way, West Windsor, NJ 08550
#6 MetroTech Center, Brooklyn, NY 11201
#0318


