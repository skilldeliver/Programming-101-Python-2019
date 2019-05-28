# HackBulgaria Airlines

Discover the world with HackBulgaria Airlines!

![HackBulgaria Airlines](airplane.png)

We need to create a website for the HackBulgaria Airlines! The project has to be
written in Django!

On the Airline's website, the users have to be able to find the following things:
- all flights
- per each flight there has to be a detailed information with the plane, the destinations,
the capacity of the plane and the available seats
- the users have to be able to book tickets for specific flight
- each user has to be able to see his flights and the information for them
- if a user has already booed a ticket, he has to be able to cancel his reservation
- the last, but not least requirement for the project is:
Only already logged users can perform actions on the website. You need to create sign in/log in page!

What do we need to create our project?

## Models
 - Flight(start_time=Date(29, 11, 2016, hour='12:20'), end_time=Date(29, 11, 2016, hour='15:30'), passengers=100, max_passengers=120, from_dest="Sofia", to_dest="London",)
 - User(first_name="Rositsa", last_name="Zlateva", age=22)
 - Passenger(user_id=23, flight=Flight(....))
 - FlightReservation(Passenget(), Flight(), seat="44B", price="99EUR")
## Views
## Urls

```python
- home page: http://hackbulgaria-airlines.com
- sign in/ log in : http://hackbulgaria-airlines.com/login
- user profile: http://hackbulgaria-airlines.com/myprofile
- all flights: http://hackbulgaria-airlines.com/flights
- flight information: http://hackbulgaria-airlines.com/flights/<flight_id>
- reservation: http://hackbulgaria-airlines.com/flights/<flight_id>/reservation
- user reservations: http://hackbulgaria-airlines.com/myreservations
```
