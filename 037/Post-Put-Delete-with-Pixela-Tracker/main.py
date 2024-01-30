

from dotenv import load_dotenv
import os
import requests
from datetime import datetime


load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_ACCOUNT = os.getenv("PIXELA_ACCOUNT")
# https://pixe.la


#########################
# Create pixela account #
#########################
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": PIXELA_TOKEN,  # I created this randomly
    "username": PIXELA_ACCOUNT,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(
#     url=user_parameters,
#     json=parameters,
# )
# response.raise_for_status()
# print(response.text)
# # {"message":"Success. Let's visit https://pixe.la/@komnick , it is your profile page!","isSuccess":true}


####################
# Create new graph #
####################
new_graph_endpoint = f"{pixela_endpoint}/{PIXELA_ACCOUNT}/graphs"
new_graph_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}
new_graph_parameters = {
    "username": PIXELA_ACCOUNT,
    "id": "graph001",
    "name": "Weight Tracker",
    "unit": "lbs",
    "type": "float",
    "color": 'shibafu',
}
# japanese colors = shibafu(green), momiji(red), sora(blue), ichou(yellow), ajisai(purple), kuro(black)

# response = requests.post(
#     url=new_graph_endpoint,
#     headers=new_graph_headers,
#     json=new_graph_parameters
# )
# # response.raise_for_status()
# print(response.text)
# # {"message":"Success.","isSuccess":true}

# https://pixe.la/v1/users/komnick/graphs/graph001.html

# Update Graph
update_graph_endpoint = f"{pixela_endpoint}/{PIXELA_ACCOUNT}/graphs/graph001"
update_graph_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}
# update_graph_parameters = {
#     "date": datetime.now().strftime("%Y%m%d"),
#     "quantity": "206.2",
# }
update_graph_parameters = {
    "date": "20231230",
    "quantity": "207.4",
}

while True:
    try:
        response = requests.post(
            url=update_graph_endpoint,
            headers=update_graph_headers,
            json=update_graph_parameters,
        )
        response.raise_for_status()
        break
    except requests.exceptions.HTTPError as e:
        print(e)
        print('Trying again...')
print(response.text)


# note:
# requests.put() will change existing data
# requests.delete() will delete data
# duh
