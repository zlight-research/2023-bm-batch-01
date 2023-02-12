tour = {"yadhu":{"distance": 24,
				 "places":["thrissur","idukki"]
					},
		"nimisha":{"distance":10,
					"places":["palakkad","wayanad"]
					},
		"athisha":{"distance":12,
					"places":["idukki","kochi"]
					}
}

totel_distance = 0
all_places = list()

for value in tour.values():
    totel_distance += value["distance"]
    all_places.extend(value["places"])

print(totel_distance,set(all_places))



