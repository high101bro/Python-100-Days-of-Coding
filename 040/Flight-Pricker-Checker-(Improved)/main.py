from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "PIT"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
print(sheet_data)
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_codes(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"],
        "willingToPay": data["willingToPay"],
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination_code in destinations:
    # try:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    # print(f"Flight to {flight.destination_city} for ${flight.price}")
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["willingToPay"]:
        print(destinations[destination_code]['id'])
        input()
        data_manager.update_destination_price(lowest_price=flight.price)

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        subject = f"Low price alert to {flight.destination_city}!"
        message = f"Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_emails(emails, subject, message)
    # except IndexError as e:
    #     print(f"There was an index error: {e}")

