from main_package.utils.flight import flight
from datetime import datetime, date, timedelta
def parse_offer(offer):
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

    if mark[0] == 9:
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
