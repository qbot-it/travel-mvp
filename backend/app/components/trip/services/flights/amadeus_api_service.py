import requests
from ...dto.flight.flight import Flight
from ...dto.flight.itinerary import Itinerary
from ...dto.flight.segment import Segment
from ...exceptions.api_authentication_failed import ApiAuthenticationFailedException
from ...exceptions.api_request_failed import ApiRequestFailedException
from ....config import settings


class AmadeusApiService:
    __url: str
    __auth_url: str
    __key: str
    __secret: str

    def __init__(self):
        self.__url = settings.amadeus_api_url
        self.__auth_url = settings.amadeus_api_auth_url
        self.__key = settings.amadeus_api_key
        self.__secret = settings.amadeus_api_secret

    def get_flight_offers(self,
                          name: str,
                          origin: str,
                          destination: str,
                          departure_date: str,
                          adults: int,
                          return_date: str | None = None,
                          children: int | None = None,
                          currency_code: str = 'EUR'
                          ) -> list[Flight]:
        """
        :raises ApiAuthenticationFailedException
        :raises ApiRequestFailedException
        """
        access_token = self.__authenticate()
        headers = {'Authorization': f'Bearer {access_token}'}

        params = {
            'originLocationCode': origin,
            'destinationLocationCode': destination,
            'departureDate': departure_date,
            'returnDate': return_date,
            'adults': adults,
            'children': children,
            'currencyCode': currency_code,
        }

        response = requests.get(self.__url, headers=headers, params=params)

        flights = []
        if response.status_code == 200:
            response_data = response.json()
            for item in response_data['data']:
                itineraries = []
                for itinerary_data in item['itineraries']:
                    segments = []
                    for segment_data in itinerary_data['segments']:
                        segment = Segment(
                            departure_airport_code=segment_data['departure']['iataCode'],
                            departure_date_time=segment_data['departure']['at'],
                            arrival_airport_code=segment_data['arrival']['iataCode'],
                            arrival_date_time=segment_data['arrival']['at'],
                            aircraft_code=segment_data['aircraft']['code'],
                            carrier_code=segment_data['carrierCode'],
                            number=segment_data['number'],
                        )
                        segments.append(segment)
                    itineraries.append(Itinerary(segments=segments))
                flights.append(Flight(
                    title=name,
                    price=float(item['price']['grandTotal']),
                    itineraries=itineraries
                ))
            return flights
        else:
            raise ApiRequestFailedException(response.text)

    def __authenticate(self) -> str:
        response = requests.post(self.__auth_url, data={
            'grant_type': 'client_credentials',
            'client_id': self.__key,
            'client_secret': self.__secret
        })

        if response.status_code == 200:
            return response.json()['access_token']
        else:
            raise ApiAuthenticationFailedException(response.text)
