db = db.getSiblingDB("corona_travel")

// db.place.createIndex({ place_id: 1 }, { unique: true })
db.places.insert({ name: "Moscow", place_id: "moscow", pos: {lat:55.749792 , lng: 37.632495} })
db.places.insert({ name: "Madrid", place_id: "madrid", pos: {lat:40.416775, lng: -3.703790} })
db.places.insert({ name: "New York", place_id: "ny", pos: {lat:40.730610 , lng: -73.935242} })

db.facts.insert({ name: "Req Square", description: "Red Square was built in 16-th century", fact_id: "moscow_red_sqr", pos: {lat:55.749792 , lng: 37.632495} })
db.facts.insert({ name: "Manhattan", description: "Manhattan is historical center on NY", fact_id: "ny_manh", pos: {lat:40.730610 , lng: -73.935242}})

