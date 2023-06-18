from utils.flight import flight
from datetime import datetime, date, timedelta
def parse_offer(offer):
    if str(offer) == "" or offer is None:
        return "empty result"
    
    try:
        outbound_flight = flight()
        inbound_flight = flight()
        lines = offer.split('\n')
        mark = [i for i in range(len(lines)) if "night" in lines[i]]
        outbound_flight.start_time = lines[0]
        outbound_flight.start_airport = lines[1]
        outbound_flight.start_airport_code = lines[2]
        outbound_flight.end_time = lines[5]
        outbound_flight.total_time = lines[3]
        outbound_flight.stops = lines[4]

        if len(mark) > 0 and mark[0] == 9:
            outbound_flight.start_date = datetime.strptime(lines[8], '%a %d %b')
            outbound_flight.end_airport = lines[6]
            outbound_flight.end_airport_code = lines[7]
            outbound_flight.end_date = lines[8]
        else:
            outbound_flight.start_date = datetime.strptime(lines[9], '%a %d %b')
            offset = int(lines[6][1:])
            outbound_flight.end_airport = lines[7]
            outbound_flight.end_airport_code = lines[8]
            outbound_flight.end_date = datetime.strptime(lines[9], '%a %d %b')
            outbound_flight.start_date = outbound_flight.end_date - timedelta(days=offset)

        return mark
    except:
        return "error parsing result"

def describe_flight(flight):
    print(f"start date: {flight.start_date}, start time: {flight.start_time}\n")
    print(f"start airport: {flight.start_airport}, end airport: {flight.end_airport}\n")
    print(f"total time: {flight.total_time}, stops: {flight.stops}\n")
    print(f"price: {flight.price}\n\n")

def parse_offer_azair(offer):
    if str(offer) == "" or offer is None:
        return "empty result"
    
    try:
        counter = 0
        outbound_flight = flight()
        inbound_flight = flight()
        lines = offer.split(' ')
        outbound_flight.start_date = datetime.strptime(lines[2], "%d/%m/%y")
        outbound_flight.start_time = lines[3]
        outbound_flight.start_airport = lines[4]
        if (not lines[5].isupper()):
            outbound_flight.start_airport = outbound_flight.start_airport + " " + lines[5]
            counter += 1
            
        outbound_flight.start_airport_code = lines[5 + counter]
        outbound_flight.end_date = outbound_flight.start_date
        outbound_flight.end_time = lines[6 + counter]
        outbound_flight.end_airport = lines[7 + counter]
        if (not lines[8 + counter].isupper()):
            outbound_flight.end_airport = outbound_flight.end_airport + " " + lines[8 + counter]
            counter += 1
            
        outbound_flight.end_airport_code = lines[8 + counter]
        outbound_flight.total_time = lines[9 + counter]
        outbound_flight.stops = lines[12 + counter]
        price_details = lines[13 + counter].split("\n")
        outbound_flight.price = price_details[2]

        return outbound_flight
    except:
        return "error parsing result"