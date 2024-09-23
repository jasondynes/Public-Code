from faker import Faker
from locust import HttpUser, task, constant_pacing, SequentialTaskSet
from faker import Faker
import random
from datetime import datetime
import pytest

VALID_USERNAME = "admin"
VALID_PWD = "password123"

token = None
booking_id_created = None
fake = Faker()


def get_fake_data(data_needed):
    match data_needed:
        case "invalid_username":
            return fake.email()
        case "invalid_pwd":
            return fake.password(length=random.randint(10, 30))
        case "first_name":
            return fake.first_name()
        case "last_name":
            return fake.last_name()
        case "total_price" | "deposit_paid":
            # only returning integers as there is a bug for e.g. 99.99
            return str(random.randint(1, 1000))
        case "checkin_date":
            return str(fake.date_between(datetime(2023, 1, 1), datetime(2024, 8, 30)))
        case "checkout_date":
            return str(fake.date_between(datetime(2024, 9, 1), datetime.today()))
        case "additional_needs":
            return fake.paragraph(random.randint(1, 20))
        case _:
            return None


class Api:
    def __init__(self):
        self.booking_id = None
        self.firstname = get_fake_data("first_name")
        self.lastname = get_fake_data("last_name")
        self.totalprice = get_fake_data("total_price")
        self.depositpaid = get_fake_data("deposit_paid")
        self.checkin_date = get_fake_data("checkin_date")
        self.checkout_date = get_fake_data("checkout_date")
        self.additional_needs = get_fake_data("additional_needs")

    def new_data(self):
        self.booking_id = None
        self.firstname = get_fake_data("first_name")
        self.lastname = get_fake_data("last_name")
        self.totalprice = get_fake_data("total_price")
        self.depositpaid = get_fake_data("deposit_paid")
        self.checkin_date = get_fake_data("checkin_date")
        self.checkout_date = get_fake_data("checkout_date")
        self.additional_needs = get_fake_data("additional_needs")


# create a persistent API object to contain data across tests
api = Api()


class RestfulBookerAPIUser(HttpUser):
    host = "https://restful-booker.herokuapp.com"
# sub class to sequence events on a per user basis

    @task
    class SequenceOfTasks(SequentialTaskSet):
        wait_time = constant_pacing(1)

        @task
        def ping_api(self):
            response = self.client.get("/ping")

        @task
        def post_valid_token_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            data = {'username': VALID_USERNAME, 'password': VALID_PWD}
            response = self.client.post("/auth", headers=header, json=data)
            json_msg = response.json()
            global token
            token = json_msg["token"]

        @task
        def post_invalid_token_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            data = {'username': get_fake_data("invalid_username"), 'password': get_fake_data("invalid_pwd")}
            response = self.client.post("/auth", headers=header, json=data)

        @task
        def create_booking_api(self):
            api.new_data()
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            data = {"firstname": api.firstname,
                    "lastname": api.lastname,
                    "totalprice": api.totalprice,
                    "depositpaid": api.depositpaid,
                    "bookingdates": {"checkin": api.checkin_date, "checkout": api.checkout_date},
                    "additional_needs": api.additional_needs,
                    }
            response = self.client.post("/booking", headers=header, json=data)
            json_msg = response.json()
            api.booking_id = json_msg["bookingid"]

        @task
        def get_all_booking_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            response = self.client.get("/booking", headers=header)

        @task
        def get_booking_by_id_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            response = self.client.get("/booking/" + str(api.booking_id), headers=header)

        @task
        def get_booking_by_fake_first_name_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            response = self.client.get("/booking?firstname=" + get_fake_data("first_name"), headers=header)

        @task
        def get_booking_by_first_name_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            response = self.client.get("/booking?firstname=" + api.firstname, headers=header)

        @task
        def get_booking_by_fake_last_name_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            response = self.client.get("/booking?lastname=" + get_fake_data("last_name"), headers=header)

        @task
        def get_booking_by_last_name_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            response = self.client.get("/booking?lastname=" + api.lastname, headers=header)

        @task
        def get_booking_by_fake_first_last_name_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            response = self.client.get("/booking?firstname=" + get_fake_data("first_name")
                                       + "&" + "lastname=" + get_fake_data("last_name"), headers=header)

        @task
        def get_booking_by_first_last_name_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            response = self.client.get("/booking?firstname=" + api.firstname
                                       + "&" + "lastname=" + api.lastname, headers=header)

        @task
        def get_booking_by_checkin_date_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            response = self.client.get("/booking?checkin=" + get_fake_data("checkin_date"), headers=header)

        @task
        def get_booking_by_checkout_date_api(self):
            header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            response = self.client.get("/booking?checkout=" + get_fake_data("checkout_date"), headers=header)
