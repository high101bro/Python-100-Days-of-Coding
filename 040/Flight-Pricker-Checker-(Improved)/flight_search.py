import requests
from flight_data import FlightData
from dotenv import load_dotenv
# import pprint
import os

load_dotenv()
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")


class FlightSearch:
    def __init__(self):
        self.city_codes = []

    def get_destination_codes(self, city_names):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_names, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
        # print("get destination codes triggered")
        # location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        # headers = {"apikey": os.environ["TEQUILA_API_KEY"]}
        # for city in city_names:
        #     query = {"term": city, "location_types": "city"}
        #     response = requests.get(url=location_endpoint, headers=headers, params=query)
        #     results = response.json()["locations"]
        #     code = results[0]["code"]
        #     self.city_codes.append(code)
        #
        # return self.city_codes

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, max_stopovers=0):
        if max_stopovers > 10:
            print(f"No flights found with up to {max_stopovers} stopovers.")
            return None

        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": max_stopovers,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )
        data = response.json().get("data")

        if not data:
            print(f"No flights found with {max_stopovers} stopovers. Trying with {max_stopovers + 1} stopovers.")
            return self.check_flights(origin_city_code, destination_city_code, from_time, to_time, max_stopovers + 1)

        try:
            flight_info = data[0]
        except IndexError:
            print("Error accessing flight data.")
            return None

        flight_data = FlightData(
            price=flight_info["price"],
            origin_city=flight_info["route"][0]["cityFrom"],
            origin_airport=flight_info["route"][0]["flyFrom"],
            destination_city=flight_info["route"][0]["cityTo"],
            destination_airport=flight_info["route"][0]["flyTo"],
            out_date=flight_info["route"][0]["local_departure"].split("T")[0],
            return_date=flight_info["route"][1]["local_departure"].split("T")[0]
        )

        return flight_data