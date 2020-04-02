import sys
from geopy.geocoders import Nominatim

import argparse

MEDIAN = '$10'

parser = argparse.ArgumentParser(description='Predict cab fares/tips.')
parser.add_argument('-a', '--address', nargs='*')
parser.add_argument('-dm', '--day_of_month', type=int)
parser.add_argument('-dw', '--day_of_week', type=int)
parser.add_argument('-hr', '--hour', type=int)
parser.add_argument('-m', '--minute', type=int)
parser.add_argument('-s', '--second', type=int)

# swap this function for new predictor, and propagate changes required by its input
def predict_fare_split(pickup_longitude=None,
                       pickup_latitude=None,
                       tpep_pickup_datetime_day_of_month=None,
                       tpep_pickup_datetime_day_of_week=None,
                       tpep_pickup_datetime_hour=None):
    """ Predictor for fare_split from model/5dc58e76fb7bdd2dd800480b

        Predictive model by BigML - Machine Learning Made Easy
    """
    if (pickup_longitude is None):
        return u'2nd'
    if (pickup_longitude > -73.87553):
        return u'2nd'
    if (pickup_longitude <= -73.87553):
        if (pickup_latitude is None):
            return u'1st'
        if (pickup_latitude > 40.71928):
            if (tpep_pickup_datetime_hour is None):
                return u'1st'
            if (tpep_pickup_datetime_hour > 4):
                if (pickup_latitude > 40.72771):
                    if (pickup_longitude > -73.95264):
                        if (pickup_longitude > -73.88701):
                            return u'2nd'
                        if (pickup_longitude <= -73.88701):
                            if (tpep_pickup_datetime_hour > 8):
                                if (pickup_latitude > 40.75536):
                                    if (pickup_latitude > 40.83197):
                                        return u'2nd'
                                    if (pickup_latitude <= 40.83197):
                                        if (tpep_pickup_datetime_day_of_week is None):
                                            return u'1st'
                                        if (tpep_pickup_datetime_day_of_week > 3):
                                            if (pickup_latitude > 40.78159):
                                                if (tpep_pickup_datetime_day_of_month is None):
                                                    return u'1st'
                                                if (tpep_pickup_datetime_day_of_month > 9):
                                                    return u'2nd'
                                                if (tpep_pickup_datetime_day_of_month <= 9):
                                                    return u'1st'
                                            if (pickup_latitude <= 40.78159):
                                                if (pickup_latitude > 40.77946):
                                                    return u'2nd'
                                                if (pickup_latitude <= 40.77946):
                                                    if (tpep_pickup_datetime_hour > 22):
                                                        return u'2nd'
                                                    if (tpep_pickup_datetime_hour <= 22):
                                                        if (pickup_latitude > 40.77551):
                                                            return u'1st'
                                                        if (pickup_latitude <= 40.77551):
                                                            return u'2nd'
                                        if (tpep_pickup_datetime_day_of_week <= 3):
                                            if (tpep_pickup_datetime_hour > 11):
                                                return u'1st'
                                            if (tpep_pickup_datetime_hour <= 11):
                                                return u'2nd'
                                if (pickup_latitude <= 40.75536):
                                    return u'2nd'
                            if (tpep_pickup_datetime_hour <= 8):
                                if (pickup_latitude > 40.78319):
                                    return u'2nd'
                                if (pickup_latitude <= 40.78319):
                                    return u'2nd'
                    if (pickup_longitude <= -73.95264):
                        if (tpep_pickup_datetime_day_of_week is None):
                            return u'1st'
                        if (tpep_pickup_datetime_day_of_week > 5):
                            if (tpep_pickup_datetime_hour > 12):
                                if (pickup_longitude > -74.00207):
                                    if (pickup_latitude > 40.79701):
                                        return u'2nd'
                                    if (pickup_latitude <= 40.79701):
                                        if (tpep_pickup_datetime_hour > 20):
                                            if (pickup_latitude > 40.73336):
                                                if (tpep_pickup_datetime_day_of_week > 6):
                                                    if (pickup_longitude > -73.95708):
                                                        return u'2nd'
                                                    if (pickup_longitude <= -73.95708):
                                                        return u'1st'
                                                if (tpep_pickup_datetime_day_of_week <= 6):
                                                    if (tpep_pickup_datetime_day_of_month is None):
                                                        return u'1st'
                                                    if (tpep_pickup_datetime_day_of_month > 6):
                                                        if (pickup_latitude > 40.79035):
                                                            return u'2nd'
                                                        if (pickup_latitude <= 40.79035):
                                                            if (pickup_latitude > 40.77772):
                                                                return u'1st'
                                                            if (pickup_latitude <= 40.77772):
                                                                if (pickup_latitude > 40.76643):
                                                                    return u'2nd'
                                                                if (pickup_latitude <= 40.76643):
                                                                    if (pickup_latitude > 40.75242):
                                                                        return u'1st'
                                                                    if (pickup_latitude <= 40.75242):
                                                                        return u'1st'
                                                    if (tpep_pickup_datetime_day_of_month <= 6):
                                                        return u'1st'
                                            if (pickup_latitude <= 40.73336):
                                                return u'2nd'
                                        if (tpep_pickup_datetime_hour <= 20):
                                            if (pickup_longitude > -73.97122):
                                                if (tpep_pickup_datetime_hour > 16):
                                                    if (pickup_longitude > -73.96263):
                                                        return u'1st'
                                                    if (pickup_longitude <= -73.96263):
                                                        return u'1st'
                                                if (tpep_pickup_datetime_hour <= 16):
                                                    if (pickup_latitude > 40.75082):
                                                        if (pickup_longitude > -73.96439):
                                                            return u'1st'
                                                        if (pickup_longitude <= -73.96439):
                                                            return u'1st'
                                                    if (pickup_latitude <= 40.75082):
                                                        return u'2nd'
                                            if (pickup_longitude <= -73.97122):
                                                if (pickup_latitude > 40.74907):
                                                    if (pickup_longitude > -73.98899):
                                                        if (pickup_latitude > 40.79242):
                                                            return u'2nd'
                                                        if (pickup_latitude <= 40.79242):
                                                            if (pickup_latitude > 40.77012):
                                                                if (pickup_latitude > 40.79107):
                                                                    return u'1st'
                                                                if (pickup_latitude <= 40.79107):
                                                                    return u'1st'
                                                            if (pickup_latitude <= 40.77012):
                                                                if (tpep_pickup_datetime_day_of_month is None):
                                                                    return u'1st'
                                                                if (tpep_pickup_datetime_day_of_month > 7):
                                                                    if (tpep_pickup_datetime_day_of_month > 24):
                                                                        return u'1st'
                                                                    if (tpep_pickup_datetime_day_of_month <= 24):
                                                                        if (pickup_latitude > 40.76026):
                                                                            return u'1st'
                                                                        if (pickup_latitude <= 40.76026):
                                                                            return u'1st'
                                                                if (tpep_pickup_datetime_day_of_month <= 7):
                                                                    return u'1st'
                                                    if (pickup_longitude <= -73.98899):
                                                        if (pickup_latitude > 40.75168):
                                                            return u'1st'
                                                        if (pickup_latitude <= 40.75168):
                                                            return u'2nd'
                                                if (pickup_latitude <= 40.74907):
                                                    if (pickup_latitude > 40.73033):
                                                        if (tpep_pickup_datetime_day_of_month is None):
                                                            return u'1st'
                                                        if (tpep_pickup_datetime_day_of_month > 24):
                                                            return u'1st'
                                                        if (tpep_pickup_datetime_day_of_month <= 24):
                                                            if (tpep_pickup_datetime_day_of_month > 17):
                                                                return u'1st'
                                                            if (tpep_pickup_datetime_day_of_month <= 17):
                                                                if (tpep_pickup_datetime_day_of_month > 7):
                                                                    return u'1st'
                                                                if (tpep_pickup_datetime_day_of_month <= 7):
                                                                    return u'1st'
                                                    if (pickup_latitude <= 40.73033):
                                                        return u'1st'
                                if (pickup_longitude <= -74.00207):
                                    if (tpep_pickup_datetime_hour > 17):
                                        return u'2nd'
                                    if (tpep_pickup_datetime_hour <= 17):
                                        return u'1st'
                            if (tpep_pickup_datetime_hour <= 12):
                                if (tpep_pickup_datetime_hour > 6):
                                    if (pickup_latitude > 40.78892):
                                        return u'1st'
                                    if (pickup_latitude <= 40.78892):
                                        if (tpep_pickup_datetime_hour > 10):
                                            if (pickup_latitude > 40.73933):
                                                if (pickup_longitude > -74.00441):
                                                    if (pickup_latitude > 40.78195):
                                                        return u'1st'
                                                    if (pickup_latitude <= 40.78195):
                                                        if (pickup_longitude > -73.96902):
                                                            return u'1st'
                                                        if (pickup_longitude <= -73.96902):
                                                            if (pickup_latitude > 40.76806):
                                                                return u'1st'
                                                            if (pickup_latitude <= 40.76806):
                                                                if (pickup_latitude > 40.74373):
                                                                    return u'1st'
                                                                if (pickup_latitude <= 40.74373):
                                                                    return u'1st'
                                                if (pickup_longitude <= -74.00441):
                                                    return u'2nd'
                                            if (pickup_latitude <= 40.73933):
                                                return u'1st'
                                        if (tpep_pickup_datetime_hour <= 10):
                                            if (pickup_longitude > -73.98718):
                                                if (pickup_latitude > 40.73344):
                                                    if (pickup_longitude > -73.9584):
                                                        return u'1st'
                                                    if (pickup_longitude <= -73.9584):
                                                        if (pickup_longitude > -73.96849):
                                                            return u'1st'
                                                        if (pickup_longitude <= -73.96849):
                                                            if (pickup_latitude > 40.7736):
                                                                return u'1st'
                                                            if (pickup_latitude <= 40.7736):
                                                                return u'1st'
                                                if (pickup_latitude <= 40.73344):
                                                    return u'2nd'
                                            if (pickup_longitude <= -73.98718):
                                                return u'1st'
                                if (tpep_pickup_datetime_hour <= 6):
                                    return u'2nd'
                        if (tpep_pickup_datetime_day_of_week <= 5):
                            if (tpep_pickup_datetime_day_of_week > 2):
                                if (tpep_pickup_datetime_hour > 7):
                                    if (tpep_pickup_datetime_day_of_month is None):
                                        return u'1st'
                                    if (tpep_pickup_datetime_day_of_month > 11):
                                        if (pickup_latitude > 40.76236):
                                            if (tpep_pickup_datetime_hour > 10):
                                                if (pickup_longitude > -73.97267):
                                                    if (pickup_latitude > 40.79992):
                                                        return u'2nd'
                                                    if (pickup_latitude <= 40.79992):
                                                        if (pickup_longitude > -73.9574):
                                                            if (pickup_latitude > 40.767):
                                                                return u'1st'
                                                            if (pickup_latitude <= 40.767):
                                                                return u'2nd'
                                                        if (pickup_longitude <= -73.9574):
                                                            if (tpep_pickup_datetime_day_of_month > 28):
                                                                return u'1st'
                                                            if (tpep_pickup_datetime_day_of_month <= 28):
                                                                if (tpep_pickup_datetime_hour > 20):
                                                                    return u'1st'
                                                                if (tpep_pickup_datetime_hour <= 20):
                                                                    if (pickup_latitude > 40.79639):
                                                                        return u'1st'
                                                                    if (pickup_latitude <= 40.79639):
                                                                        if (pickup_latitude > 40.76718):
                                                                            return u'1st'
                                                                        if (pickup_latitude <= 40.76718):
                                                                            return u'1st'
                                                if (pickup_longitude <= -73.97267):
                                                    if (pickup_latitude > 40.7725):
                                                        if (tpep_pickup_datetime_hour > 21):
                                                            return u'2nd'
                                                        if (tpep_pickup_datetime_hour <= 21):
                                                            if (tpep_pickup_datetime_hour > 13):
                                                                return u'1st'
                                                            if (tpep_pickup_datetime_hour <= 13):
                                                                return u'1st'
                                                    if (pickup_latitude <= 40.7725):
                                                        if (tpep_pickup_datetime_day_of_month > 21):
                                                            return u'2nd'
                                                        if (tpep_pickup_datetime_day_of_month <= 21):
                                                            return u'2nd'
                                            if (tpep_pickup_datetime_hour <= 10):
                                                if (pickup_longitude > -73.95866):
                                                    return u'2nd'
                                                if (pickup_longitude <= -73.95866):
                                                    if (pickup_latitude > 40.77484):
                                                        return u'2nd'
                                                    if (pickup_latitude <= 40.77484):
                                                        return u'1st'
                                        if (pickup_latitude <= 40.76236):
                                            if (pickup_longitude > -73.97528):
                                                if (pickup_latitude > 40.75269):
                                                    if (tpep_pickup_datetime_hour > 8):
                                                        if (pickup_latitude > 40.76039):
                                                            return u'1st'
                                                        if (pickup_latitude <= 40.76039):
                                                            if (pickup_longitude > -73.97038):
                                                                return u'2nd'
                                                            if (pickup_longitude <= -73.97038):
                                                                return u'2nd'
                                                    if (tpep_pickup_datetime_hour <= 8):
                                                        return u'1st'
                                                if (pickup_latitude <= 40.75269):
                                                    return u'2nd'
                                            if (pickup_longitude <= -73.97528):
                                                if (pickup_longitude > -74.00269):
                                                    if (tpep_pickup_datetime_hour > 9):
                                                        if (pickup_latitude > 40.74616):
                                                            if (tpep_pickup_datetime_day_of_month > 28):
                                                                return u'2nd'
                                                            if (tpep_pickup_datetime_day_of_month <= 28):
                                                                if (pickup_longitude > -73.99053):
                                                                    if (tpep_pickup_datetime_hour > 16):
                                                                        if (tpep_pickup_datetime_day_of_month > 14):
                                                                            if (pickup_longitude > -73.98451):
                                                                                return u'2nd'
                                                                            if (pickup_longitude <= -73.98451):
                                                                                return u'2nd'
                                                                        if (tpep_pickup_datetime_day_of_month <= 14):
                                                                            return u'1st'
                                                                    if (tpep_pickup_datetime_hour <= 16):
                                                                        if (pickup_latitude > 40.75583):
                                                                            return u'2nd'
                                                                        if (pickup_latitude <= 40.75583):
                                                                            return u'1st'
                                                                if (pickup_longitude <= -73.99053):
                                                                    if (tpep_pickup_datetime_hour > 15):
                                                                        return u'2nd'
                                                                    if (tpep_pickup_datetime_hour <= 15):
                                                                        return u'2nd'
                                                        if (pickup_latitude <= 40.74616):
                                                            if (pickup_longitude > -73.99421):
                                                                if (tpep_pickup_datetime_day_of_month > 28):
                                                                    return u'2nd'
                                                                if (tpep_pickup_datetime_day_of_month <= 28):
                                                                    if (pickup_latitude > 40.72833):
                                                                        if (tpep_pickup_datetime_hour > 15):
                                                                            if (tpep_pickup_datetime_hour > 20):
                                                                                return u'1st'
                                                                            if (tpep_pickup_datetime_hour <= 20):
                                                                                return u'1st'
                                                                        if (tpep_pickup_datetime_hour <= 15):
                                                                            return u'2nd'
                                                                    if (pickup_latitude <= 40.72833):
                                                                        return u'2nd'
                                                            if (pickup_longitude <= -73.99421):
                                                                if (tpep_pickup_datetime_hour > 21):
                                                                    return u'2nd'
                                                                if (tpep_pickup_datetime_hour <= 21):
                                                                    return u'1st'
                                                    if (tpep_pickup_datetime_hour <= 9):
                                                        if (pickup_latitude > 40.74305):
                                                            return u'1st'
                                                        if (pickup_latitude <= 40.74305):
                                                            return u'2nd'
                                                if (pickup_longitude <= -74.00269):
                                                    if (pickup_latitude > 40.7395):
                                                        return u'2nd'
                                                    if (pickup_latitude <= 40.7395):
                                                        return u'2nd'
                                    if (tpep_pickup_datetime_day_of_month <= 11):
                                        if (tpep_pickup_datetime_day_of_month > 1):
                                            if (pickup_longitude > -73.97087):
                                                if (tpep_pickup_datetime_hour > 10):
                                                    if (pickup_latitude > 40.76117):
                                                        if (pickup_latitude > 40.79943):
                                                            return u'2nd'
                                                        if (pickup_latitude <= 40.79943):
                                                            if (pickup_longitude > -73.95504):
                                                                return u'1st'
                                                            if (pickup_longitude <= -73.95504):
                                                                if (pickup_latitude > 40.77657):
                                                                    return u'1st'
                                                                if (pickup_latitude <= 40.77657):
                                                                    return u'1st'
                                                    if (pickup_latitude <= 40.76117):
                                                        return u'1st'
                                                if (tpep_pickup_datetime_hour <= 10):
                                                    return u'1st'
                                            if (pickup_longitude <= -73.97087):
                                                if (pickup_latitude > 40.7469):
                                                    if (pickup_longitude > -73.98913):
                                                        if (tpep_pickup_datetime_hour > 8):
                                                            if (tpep_pickup_datetime_day_of_week > 3):
                                                                if (pickup_latitude > 40.76255):
                                                                    if (pickup_longitude > -73.97161):
                                                                        return u'1st'
                                                                    if (pickup_longitude <= -73.97161):
                                                                        if (tpep_pickup_datetime_hour > 22):
                                                                            return u'2nd'
                                                                        if (tpep_pickup_datetime_hour <= 22):
                                                                            return u'1st'
                                                                if (pickup_latitude <= 40.76255):
                                                                    if (pickup_longitude > -73.97369):
                                                                        return u'2nd'
                                                                    if (pickup_longitude <= -73.97369):
                                                                        if (tpep_pickup_datetime_hour > 9):
                                                                            if (tpep_pickup_datetime_hour > 12):
                                                                                return u'1st'
                                                                            if (tpep_pickup_datetime_hour <= 12):
                                                                                return u'1st'
                                                                        if (tpep_pickup_datetime_hour <= 9):
                                                                            return u'1st'
                                                            if (tpep_pickup_datetime_day_of_week <= 3):
                                                                return u'1st'
                                                        if (tpep_pickup_datetime_hour <= 8):
                                                            return u'1st'
                                                    if (pickup_longitude <= -73.98913):
                                                        if (tpep_pickup_datetime_hour > 9):
                                                            if (pickup_latitude > 40.75141):
                                                                return u'1st'
                                                            if (pickup_latitude <= 40.75141):
                                                                return u'2nd'
                                                        if (tpep_pickup_datetime_hour <= 9):
                                                            return u'1st'
                                                if (pickup_latitude <= 40.7469):
                                                    if (pickup_longitude > -73.97703):
                                                        return u'2nd'
                                                    if (pickup_longitude <= -73.97703):
                                                        if (pickup_longitude > -74.00414):
                                                            if (pickup_latitude > 40.73921):
                                                                return u'1st'
                                                            if (pickup_latitude <= 40.73921):
                                                                if (pickup_longitude > -73.98677):
                                                                    return u'1st'
                                                                if (pickup_longitude <= -73.98677):
                                                                    return u'1st'
                                                        if (pickup_longitude <= -74.00414):
                                                            return u'1st'
                                        if (tpep_pickup_datetime_day_of_month <= 1):
                                            if (pickup_latitude > 40.75381):
                                                return u'1st'
                                            if (pickup_latitude <= 40.75381):
                                                return u'1st'
                                if (tpep_pickup_datetime_hour <= 7):
                                    if (pickup_latitude > 40.78102):
                                        return u'2nd'
                                    if (pickup_latitude <= 40.78102):
                                        if (pickup_latitude > 40.73758):
                                            if (pickup_longitude > -74.00056):
                                                if (pickup_latitude > 40.76506):
                                                    return u'1st'
                                                if (pickup_latitude <= 40.76506):
                                                    if (pickup_longitude > -73.96099):
                                                        return u'2nd'
                                                    if (pickup_longitude <= -73.96099):
                                                        if (tpep_pickup_datetime_day_of_month is None):
                                                            return u'1st'
                                                        if (tpep_pickup_datetime_day_of_month > 1):
                                                            if (tpep_pickup_datetime_hour > 6):
                                                                return u'1st'
                                                            if (tpep_pickup_datetime_hour <= 6):
                                                                return u'1st'
                                                        if (tpep_pickup_datetime_day_of_month <= 1):
                                                            return u'1st'
                                            if (pickup_longitude <= -74.00056):
                                                return u'2nd'
                                        if (pickup_latitude <= 40.73758):
                                            return u'2nd'
                            if (tpep_pickup_datetime_day_of_week <= 2):
                                if (tpep_pickup_datetime_day_of_month is None):
                                    return u'1st'
                                if (tpep_pickup_datetime_day_of_month > 26):
                                    return u'1st'
                                if (tpep_pickup_datetime_day_of_month <= 26):
                                    if (tpep_pickup_datetime_day_of_week > 1):
                                        if (tpep_pickup_datetime_day_of_month > 9):
                                            if (tpep_pickup_datetime_hour > 6):
                                                if (pickup_latitude > 40.76199):
                                                    if (tpep_pickup_datetime_hour > 9):
                                                        if (pickup_latitude > 40.76513):
                                                            if (pickup_longitude > -73.98251):
                                                                if (pickup_latitude > 40.79842):
                                                                    return u'2nd'
                                                                if (pickup_latitude <= 40.79842):
                                                                    if (tpep_pickup_datetime_hour > 21):
                                                                        return u'1st'
                                                                    if (tpep_pickup_datetime_hour <= 21):
                                                                        return u'1st'
                                                            if (pickup_longitude <= -73.98251):
                                                                return u'2nd'
                                                        if (pickup_latitude <= 40.76513):
                                                            return u'1st'
                                                    if (tpep_pickup_datetime_hour <= 9):
                                                        return u'2nd'
                                                if (pickup_latitude <= 40.76199):
                                                    if (tpep_pickup_datetime_hour > 8):
                                                        if (pickup_latitude > 40.74473):
                                                            if (pickup_longitude > -73.98981):
                                                                if (pickup_latitude > 40.76051):
                                                                    return u'1st'
                                                                if (pickup_latitude <= 40.76051):
                                                                    if (pickup_longitude > -73.97755):
                                                                        return u'2nd'
                                                                    if (pickup_longitude <= -73.97755):
                                                                        return u'1st'
                                                            if (pickup_longitude <= -73.98981):
                                                                return u'2nd'
                                                        if (pickup_latitude <= 40.74473):
                                                            if (tpep_pickup_datetime_hour > 20):
                                                                return u'2nd'
                                                            if (tpep_pickup_datetime_hour <= 20):
                                                                return u'1st'
                                                    if (tpep_pickup_datetime_hour <= 8):
                                                        return u'1st'
                                            if (tpep_pickup_datetime_hour <= 6):
                                                return u'1st'
                                        if (tpep_pickup_datetime_day_of_month <= 9):
                                            if (pickup_longitude > -73.95836):
                                                return u'2nd'
                                            if (pickup_longitude <= -73.95836):
                                                if (tpep_pickup_datetime_hour > 7):
                                                    if (tpep_pickup_datetime_hour > 12):
                                                        if (tpep_pickup_datetime_hour > 19):
                                                            return u'1st'
                                                        if (tpep_pickup_datetime_hour <= 19):
                                                            if (pickup_longitude > -74.00601):
                                                                return u'1st'
                                                            if (pickup_longitude <= -74.00601):
                                                                return u'2nd'
                                                    if (tpep_pickup_datetime_hour <= 12):
                                                        return u'1st'
                                                if (tpep_pickup_datetime_hour <= 7):
                                                    return u'1st'
                                    if (tpep_pickup_datetime_day_of_week <= 1):
                                        if (pickup_longitude > -74.00376):
                                            if (pickup_latitude > 40.7982):
                                                return u'2nd'
                                            if (pickup_latitude <= 40.7982):
                                                if (pickup_longitude > -73.97089):
                                                    if (pickup_longitude > -73.96333):
                                                        if (tpep_pickup_datetime_hour > 9):
                                                            return u'1st'
                                                        if (tpep_pickup_datetime_hour <= 9):
                                                            return u'2nd'
                                                    if (pickup_longitude <= -73.96333):
                                                        return u'1st'
                                                if (pickup_longitude <= -73.97089):
                                                    if (tpep_pickup_datetime_hour > 7):
                                                        if (pickup_longitude > -73.97404):
                                                            return u'1st'
                                                        if (pickup_longitude <= -73.97404):
                                                            if (tpep_pickup_datetime_day_of_month > 8):
                                                                if (tpep_pickup_datetime_day_of_month > 15):
                                                                    if (tpep_pickup_datetime_day_of_month > 22):
                                                                        return u'1st'
                                                                    if (tpep_pickup_datetime_day_of_month <= 22):
                                                                        if (tpep_pickup_datetime_hour > 19):
                                                                            return u'1st'
                                                                        if (tpep_pickup_datetime_hour <= 19):
                                                                            return u'1st'
                                                                if (tpep_pickup_datetime_day_of_month <= 15):
                                                                    if (pickup_longitude > -73.99252):
                                                                        if (tpep_pickup_datetime_hour > 16):
                                                                            return u'1st'
                                                                        if (tpep_pickup_datetime_hour <= 16):
                                                                            return u'1st'
                                                                    if (pickup_longitude <= -73.99252):
                                                                        return u'1st'
                                                            if (tpep_pickup_datetime_day_of_month <= 8):
                                                                if (tpep_pickup_datetime_hour > 20):
                                                                    return u'1st'
                                                                if (tpep_pickup_datetime_hour <= 20):
                                                                    return u'1st'
                                                    if (tpep_pickup_datetime_hour <= 7):
                                                        return u'1st'
                                        if (pickup_longitude <= -74.00376):
                                            return u'1st'
                if (pickup_latitude <= 40.72771):
                    if (pickup_latitude > 40.72312):
                        if (tpep_pickup_datetime_hour > 20):
                            return u'2nd'
                        if (tpep_pickup_datetime_hour <= 20):
                            if (tpep_pickup_datetime_hour > 7):
                                if (tpep_pickup_datetime_day_of_month is None):
                                    return u'1st'
                                if (tpep_pickup_datetime_day_of_month > 27):
                                    return u'2nd'
                                if (tpep_pickup_datetime_day_of_month <= 27):
                                    if (tpep_pickup_datetime_day_of_month > 26):
                                        return u'1st'
                                    if (tpep_pickup_datetime_day_of_month <= 26):
                                        if (tpep_pickup_datetime_day_of_week is None):
                                            return u'1st'
                                        if (tpep_pickup_datetime_day_of_week > 6):
                                            return u'1st'
                                        if (tpep_pickup_datetime_day_of_week <= 6):
                                            if (pickup_longitude > -73.90834):
                                                return u'2nd'
                                            if (pickup_longitude <= -73.90834):
                                                if (pickup_longitude > -73.94433):
                                                    return u'1st'
                                                if (pickup_longitude <= -73.94433):
                                                    if (tpep_pickup_datetime_day_of_month > 1):
                                                        if (tpep_pickup_datetime_day_of_week > 1):
                                                            if (pickup_latitude > 40.72367):
                                                                if (pickup_latitude > 40.72397):
                                                                    if (tpep_pickup_datetime_day_of_month > 8):
                                                                        return u'2nd'
                                                                    if (tpep_pickup_datetime_day_of_month <= 8):
                                                                        return u'1st'
                                                                if (pickup_latitude <= 40.72397):
                                                                    return u'1st'
                                                            if (pickup_latitude <= 40.72367):
                                                                return u'2nd'
                                                        if (tpep_pickup_datetime_day_of_week <= 1):
                                                            return u'1st'
                                                    if (tpep_pickup_datetime_day_of_month <= 1):
                                                        return u'1st'
                            if (tpep_pickup_datetime_hour <= 7):
                                return u'2nd'
                    if (pickup_latitude <= 40.72312):
                        if (tpep_pickup_datetime_hour > 21):
                            return u'2nd'
                        if (tpep_pickup_datetime_hour <= 21):
                            if (pickup_longitude > -73.98799):
                                return u'2nd'
                            if (pickup_longitude <= -73.98799):
                                if (pickup_longitude > -74.00883):
                                    if (tpep_pickup_datetime_day_of_month is None):
                                        return u'2nd'
                                    if (tpep_pickup_datetime_day_of_month > 5):
                                        if (tpep_pickup_datetime_hour > 6):
                                            if (tpep_pickup_datetime_hour > 19):
                                                return u'2nd'
                                            if (tpep_pickup_datetime_hour <= 19):
                                                if (tpep_pickup_datetime_hour > 17):
                                                    return u'1st'
                                                if (tpep_pickup_datetime_hour <= 17):
                                                    return u'2nd'
                                        if (tpep_pickup_datetime_hour <= 6):
                                            return u'2nd'
                                    if (tpep_pickup_datetime_day_of_month <= 5):
                                        return u'1st'
                                if (pickup_longitude <= -74.00883):
                                    return u'2nd'
            if (tpep_pickup_datetime_hour <= 4):
                if (pickup_latitude > 40.72368):
                    if (tpep_pickup_datetime_hour > 1):
                        if (pickup_longitude > -73.9976):
                            if (pickup_latitude > 40.73361):
                                if (pickup_latitude > 40.75826):
                                    if (pickup_longitude > -73.98078):
                                        return u'2nd'
                                    if (pickup_longitude <= -73.98078):
                                        return u'2nd'
                                if (pickup_latitude <= 40.75826):
                                    return u'2nd'
                            if (pickup_latitude <= 40.73361):
                                return u'2nd'
                        if (pickup_longitude <= -73.9976):
                            return u'2nd'
                    if (tpep_pickup_datetime_hour <= 1):
                        if (pickup_longitude > -74.00317):
                            if (tpep_pickup_datetime_day_of_month is None):
                                return u'2nd'
                            if (tpep_pickup_datetime_day_of_month > 1):
                                if (pickup_latitude > 40.72824):
                                    if (pickup_latitude > 40.75822):
                                        if (pickup_longitude > -73.93926):
                                            return u'1st'
                                        if (pickup_longitude <= -73.93926):
                                            if (tpep_pickup_datetime_day_of_week is None):
                                                return u'2nd'
                                            if (tpep_pickup_datetime_day_of_week > 4):
                                                if (tpep_pickup_datetime_day_of_month > 9):
                                                    return u'2nd'
                                                if (tpep_pickup_datetime_day_of_month <= 9):
                                                    return u'2nd'
                                            if (tpep_pickup_datetime_day_of_week <= 4):
                                                return u'2nd'
                                    if (pickup_latitude <= 40.75822):
                                        if (pickup_latitude > 40.731):
                                            if (pickup_latitude > 40.75635):
                                                return u'1st'
                                            if (pickup_latitude <= 40.75635):
                                                if (pickup_longitude > -73.95907):
                                                    return u'2nd'
                                                if (pickup_longitude <= -73.95907):
                                                    if (tpep_pickup_datetime_day_of_month > 2):
                                                        if (pickup_latitude > 40.74472):
                                                            if (pickup_longitude > -73.96521):
                                                                return u'1st'
                                                            if (pickup_longitude <= -73.96521):
                                                                if (tpep_pickup_datetime_day_of_week is None):
                                                                    return u'2nd'
                                                                if (tpep_pickup_datetime_day_of_week > 4):
                                                                    return u'2nd'
                                                                if (tpep_pickup_datetime_day_of_week <= 4):
                                                                    return u'1st'
                                                        if (pickup_latitude <= 40.74472):
                                                            if (pickup_longitude > -74.00101):
                                                                return u'1st'
                                                            if (pickup_longitude <= -74.00101):
                                                                return u'2nd'
                                                    if (tpep_pickup_datetime_day_of_month <= 2):
                                                        return u'1st'
                                        if (pickup_latitude <= 40.731):
                                            return u'2nd'
                                if (pickup_latitude <= 40.72824):
                                    return u'2nd'
                            if (tpep_pickup_datetime_day_of_month <= 1):
                                return u'2nd'
                        if (pickup_longitude <= -74.00317):
                            return u'2nd'
                if (pickup_latitude <= 40.72368):
                    return u'2nd'
        if (pickup_latitude <= 40.71928):
            if (pickup_latitude > 40.71299):
                if (pickup_longitude > -74.0127):
                    if (tpep_pickup_datetime_hour is None):
                        return u'2nd'
                    if (tpep_pickup_datetime_hour > 6):
                        if (pickup_longitude > -73.99868):
                            return u'2nd'
                        if (pickup_longitude <= -73.99868):
                            if (tpep_pickup_datetime_day_of_week is None):
                                return u'2nd'
                            if (tpep_pickup_datetime_day_of_week > 5):
                                return u'1st'
                            if (tpep_pickup_datetime_day_of_week <= 5):
                                return u'2nd'
                    if (tpep_pickup_datetime_hour <= 6):
                        return u'2nd'
                if (pickup_longitude <= -74.0127):
                    return u'2nd'
            if (pickup_latitude <= 40.71299):
                if (pickup_longitude > -73.99122):
                    if (pickup_latitude > 40.69164):
                        return u'2nd'
                    if (pickup_latitude <= 40.69164):
                        return u'2nd'
                if (pickup_longitude <= -73.99122):
                    if (pickup_latitude > 40.6923):
                        if (pickup_latitude > 40.70943):
                            return u'2nd'
                        if (pickup_latitude <= 40.70943):
                            if (pickup_longitude > -74.01579):
                                if (tpep_pickup_datetime_day_of_week is None):
                                    return u'2nd'
                                if (tpep_pickup_datetime_day_of_week > 5):
                                    return u'2nd'
                                if (tpep_pickup_datetime_day_of_week <= 5):
                                    return u'2nd'
                            if (pickup_longitude <= -74.01579):
                                return u'2nd'
                    if (pickup_latitude <= 40.6923):
                        return u'2nd'							

def predict_tip_exists(pickup_longitude=None,
                       pickup_latitude=None,
                       tpep_pickup_datetime_day_of_month=None,
                       tpep_pickup_datetime_day_of_week=None,
                       tpep_pickup_datetime_hour=None,
                       tpep_pickup_datetime_minute=None,
                       tpep_pickup_datetime_second=None):
    """ Predictor for tip_exists from model/5dc58f885e269e31e6000677

        Predictive model by BigML - Machine Learning Made Easy
    """
    if (pickup_latitude is None):
        return u'True'
    if (pickup_latitude > 40.74894):
        if (tpep_pickup_datetime_day_of_month is None):
            return u'True'
        if (tpep_pickup_datetime_day_of_month > 4):
            if (tpep_pickup_datetime_hour is None):
                return u'True'
            if (tpep_pickup_datetime_hour > 18):
                if (tpep_pickup_datetime_day_of_week is None):
                    return u'True'
                if (tpep_pickup_datetime_day_of_week > 5):
                    if (pickup_longitude is None):
                        return u'True'
                    if (pickup_longitude > -73.87466):
                        return u'True'
                    if (pickup_longitude <= -73.87466):
                        if (pickup_longitude > -73.97063):
                            if (pickup_longitude > -73.94427):
                                return u'False'
                            if (pickup_longitude <= -73.94427):
                                if (pickup_latitude > 40.79525):
                                    return u'True'
                                if (pickup_latitude <= 40.79525):
                                    if (tpep_pickup_datetime_hour > 21):
                                        return u'True'
                                    if (tpep_pickup_datetime_hour <= 21):
                                        return u'True'
                        if (pickup_longitude <= -73.97063):
                            if (pickup_latitude > 40.76766):
                                return u'True'
                            if (pickup_latitude <= 40.76766):
                                if (pickup_longitude > -73.99254):
                                    if (pickup_latitude > 40.76333):
                                        return u'True'
                                    if (pickup_latitude <= 40.76333):
                                        if (pickup_longitude > -73.98128):
                                            return u'True'
                                        if (pickup_longitude <= -73.98128):
                                            return u'False'
                                if (pickup_longitude <= -73.99254):
                                    return u'True'
                if (tpep_pickup_datetime_day_of_week <= 5):
                    if (pickup_latitude > 40.77791):
                        if (pickup_longitude is None):
                            return u'True'
                        if (pickup_longitude > -73.94686):
                            return u'False'
                        if (pickup_longitude <= -73.94686):
                            if (pickup_longitude > -73.97318):
                                return u'True'
                            if (pickup_longitude <= -73.97318):
                                return u'True'
                    if (pickup_latitude <= 40.77791):
                        if (pickup_longitude is None):
                            return u'True'
                        if (pickup_longitude > -73.88862):
                            return u'True'
                        if (pickup_longitude <= -73.88862):
                            if (pickup_latitude > 40.76857):
                                if (tpep_pickup_datetime_hour > 20):
                                    return u'True'
                                if (tpep_pickup_datetime_hour <= 20):
                                    return u'True'
                            if (pickup_latitude <= 40.76857):
                                if (pickup_longitude > -73.98458):
                                    if (pickup_latitude > 40.76138):
                                        if (pickup_longitude > -73.97291):
                                            if (pickup_longitude > -73.91325):
                                                return u'False'
                                            if (pickup_longitude <= -73.91325):
                                                return u'True'
                                        if (pickup_longitude <= -73.97291):
                                            return u'True'
                                    if (pickup_latitude <= 40.76138):
                                        if (pickup_longitude > -73.97002):
                                            return u'True'
                                        if (pickup_longitude <= -73.97002):
                                            if (tpep_pickup_datetime_day_of_week > 4):
                                                return u'True'
                                            if (tpep_pickup_datetime_day_of_week <= 4):
                                                if (pickup_longitude > -73.97401):
                                                    return u'True'
                                                if (pickup_longitude <= -73.97401):
                                                    if (pickup_latitude > 40.75693):
                                                        return u'True'
                                                    if (pickup_latitude <= 40.75693):
                                                        return u'True'
                                if (pickup_longitude <= -73.98458):
                                    if (pickup_longitude > -74.00515):
                                        if (pickup_longitude > -73.99455):
                                            if (pickup_latitude > 40.75614):
                                                return u'True'
                                            if (pickup_latitude <= 40.75614):
                                                return u'True'
                                        if (pickup_longitude <= -73.99455):
                                            return u'True'
                                    if (pickup_longitude <= -74.00515):
                                        return u'True'
            if (tpep_pickup_datetime_hour <= 18):
                if (pickup_longitude is None):
                    return u'True'
                if (pickup_longitude > -73.87585):
                    if (pickup_latitude > 40.76669):
                        if (tpep_pickup_datetime_day_of_week is None):
                            return u'True'
                        if (tpep_pickup_datetime_day_of_week > 3):
                            return u'True'
                        if (tpep_pickup_datetime_day_of_week <= 3):
                            return u'True'
                    if (pickup_latitude <= 40.76669):
                        return u'False'
                if (pickup_longitude <= -73.87585):
                    if (pickup_longitude > -73.94389):
                        return u'False'
                    if (pickup_longitude <= -73.94389):
                        if (tpep_pickup_datetime_day_of_week is None):
                            return u'True'
                        if (tpep_pickup_datetime_day_of_week > 5):
                            if (pickup_latitude > 40.76512):
                                if (pickup_longitude > -73.99501):
                                    if (pickup_longitude > -73.98648):
                                        if (pickup_longitude > -73.95826):
                                            if (pickup_latitude > 40.78547):
                                                return u'True'
                                            if (pickup_latitude <= 40.78547):
                                                if (pickup_longitude > -73.95336):
                                                    return u'True'
                                                if (pickup_longitude <= -73.95336):
                                                    return u'True'
                                        if (pickup_longitude <= -73.95826):
                                            if (pickup_latitude > 40.78328):
                                                if (pickup_latitude > 40.79507):
                                                    return u'True'
                                                if (pickup_latitude <= 40.79507):
                                                    return u'True'
                                            if (pickup_latitude <= 40.78328):
                                                if (pickup_longitude > -73.97602):
                                                    return u'True'
                                                if (pickup_longitude <= -73.97602):
                                                    if (pickup_latitude > 40.77318):
                                                        return u'True'
                                                    if (pickup_latitude <= 40.77318):
                                                        return u'True'
                                    if (pickup_longitude <= -73.98648):
                                        return u'True'
                                if (pickup_longitude <= -73.99501):
                                    return u'False'
                            if (pickup_latitude <= 40.76512):
                                if (pickup_longitude > -73.97251):
                                    if (pickup_longitude > -73.94626):
                                        return u'False'
                                    if (pickup_longitude <= -73.94626):
                                        if (tpep_pickup_datetime_second is None):
                                            return u'True'
                                        if (tpep_pickup_datetime_second > 0):
                                            if (pickup_latitude > 40.76165):
                                                return u'True'
                                            if (pickup_latitude <= 40.76165):
                                                return u'True'
                                        if (tpep_pickup_datetime_second <= 0):
                                            return u'False'
                                if (pickup_longitude <= -73.97251):
                                    if (pickup_longitude > -73.99455):
                                        if (tpep_pickup_datetime_hour > 3):
                                            if (tpep_pickup_datetime_hour > 13):
                                                if (tpep_pickup_datetime_day_of_month > 24):
                                                    return u'True'
                                                if (tpep_pickup_datetime_day_of_month <= 24):
                                                    if (tpep_pickup_datetime_minute is None):
                                                        return u'False'
                                                    if (tpep_pickup_datetime_minute > 46):
                                                        return u'True'
                                                    if (tpep_pickup_datetime_minute <= 46):
                                                        return u'False'
                                            if (tpep_pickup_datetime_hour <= 13):
                                                if (pickup_latitude > 40.75917):
                                                    return u'False'
                                                if (pickup_latitude <= 40.75917):
                                                    return u'False'
                                        if (tpep_pickup_datetime_hour <= 3):
                                            return u'True'
                                    if (pickup_longitude <= -73.99455):
                                        return u'True'
                        if (tpep_pickup_datetime_day_of_week <= 5):
                            if (tpep_pickup_datetime_hour > 9):
                                if (pickup_longitude > -74.00147):
                                    if (pickup_longitude > -73.96588):
                                        if (tpep_pickup_datetime_hour > 16):
                                            if (pickup_latitude > 40.797):
                                                return u'False'
                                            if (pickup_latitude <= 40.797):
                                                if (pickup_latitude > 40.77455):
                                                    return u'True'
                                                if (pickup_latitude <= 40.77455):
                                                    return u'True'
                                        if (tpep_pickup_datetime_hour <= 16):
                                            if (tpep_pickup_datetime_hour > 11):
                                                if (pickup_longitude > -73.94767):
                                                    return u'False'
                                                if (pickup_longitude <= -73.94767):
                                                    if (tpep_pickup_datetime_minute is None):
                                                        return u'True'
                                                    if (tpep_pickup_datetime_minute > 49):
                                                        return u'True'
                                                    if (tpep_pickup_datetime_minute <= 49):
                                                        if (tpep_pickup_datetime_day_of_month > 17):
                                                            if (tpep_pickup_datetime_second is None):
                                                                return u'True'
                                                            if (tpep_pickup_datetime_second > 8):
                                                                return u'True'
                                                            if (tpep_pickup_datetime_second <= 8):
                                                                return u'False'
                                                        if (tpep_pickup_datetime_day_of_month <= 17):
                                                            if (pickup_latitude > 40.79214):
                                                                return u'False'
                                                            if (pickup_latitude <= 40.79214):
                                                                if (tpep_pickup_datetime_minute > 24):
                                                                    return u'False'
                                                                if (tpep_pickup_datetime_minute <= 24):
                                                                    return u'True'
                                            if (tpep_pickup_datetime_hour <= 11):
                                                if (tpep_pickup_datetime_day_of_month > 8):
                                                    if (pickup_latitude > 40.83193):
                                                        return u'False'
                                                    if (pickup_latitude <= 40.83193):
                                                        if (tpep_pickup_datetime_second is None):
                                                            return u'True'
                                                        if (tpep_pickup_datetime_second > 58):
                                                            return u'False'
                                                        if (tpep_pickup_datetime_second <= 58):
                                                            return u'True'
                                                if (tpep_pickup_datetime_day_of_month <= 8):
                                                    return u'True'
                                    if (pickup_longitude <= -73.96588):
                                        if (tpep_pickup_datetime_hour > 17):
                                            if (pickup_longitude > -73.98378):
                                                if (pickup_latitude > 40.76988):
                                                    return u'True'
                                                if (pickup_latitude <= 40.76988):
                                                    return u'True'
                                            if (pickup_longitude <= -73.98378):
                                                return u'True'
                                        if (tpep_pickup_datetime_hour <= 17):
                                            if (tpep_pickup_datetime_day_of_month > 6):
                                                if (pickup_longitude > -73.98428):
                                                    if (pickup_latitude > 40.76177):
                                                        if (pickup_longitude > -73.97457):
                                                            if (tpep_pickup_datetime_hour > 10):
                                                                if (tpep_pickup_datetime_hour > 15):
                                                                    return u'True'
                                                                if (tpep_pickup_datetime_hour <= 15):
                                                                    if (tpep_pickup_datetime_second is None):
                                                                        return u'True'
                                                                    if (tpep_pickup_datetime_second > 57):
                                                                        return u'False'
                                                                    if (tpep_pickup_datetime_second <= 57):
                                                                        if (tpep_pickup_datetime_hour > 14):
                                                                            return u'False'
                                                                        if (tpep_pickup_datetime_hour <= 14):
                                                                            return u'True'
                                                            if (tpep_pickup_datetime_hour <= 10):
                                                                return u'True'
                                                        if (pickup_longitude <= -73.97457):
                                                            if (tpep_pickup_datetime_day_of_month > 27):
                                                                return u'True'
                                                            if (tpep_pickup_datetime_day_of_month <= 27):
                                                                if (tpep_pickup_datetime_day_of_month > 24):
                                                                    return u'True'
                                                                if (tpep_pickup_datetime_day_of_month <= 24):
                                                                    if (pickup_latitude > 40.77935):
                                                                        return u'True'
                                                                    if (pickup_latitude <= 40.77935):
                                                                        if (tpep_pickup_datetime_minute is None):
                                                                            return u'True'
                                                                        if (tpep_pickup_datetime_minute > 1):
                                                                            if (tpep_pickup_datetime_minute > 7):
                                                                                if (pickup_longitude > -73.97734):
                                                                                    return u'True'
                                                                                if (pickup_longitude <= -73.97734):
                                                                                    return u'True'
                                                                            if (tpep_pickup_datetime_minute <= 7):
                                                                                return u'True'
                                                                        if (tpep_pickup_datetime_minute <= 1):
                                                                            return u'True'
                                                    if (pickup_latitude <= 40.76177):
                                                        if (pickup_longitude > -73.96969):
                                                            return u'True'
                                                        if (pickup_longitude <= -73.96969):
                                                            if (pickup_longitude > -73.97626):
                                                                if (tpep_pickup_datetime_day_of_week > 2):
                                                                    return u'True'
                                                                if (tpep_pickup_datetime_day_of_week <= 2):
                                                                    return u'True'
                                                            if (pickup_longitude <= -73.97626):
                                                                if (pickup_longitude > -73.97873):
                                                                    return u'True'
                                                                if (pickup_longitude <= -73.97873):
                                                                    return u'True'
                                                if (pickup_longitude <= -73.98428):
                                                    if (pickup_longitude > -73.99428):
                                                        if (pickup_latitude > 40.75192):
                                                            if (pickup_latitude > 40.75579):
                                                                if (pickup_latitude > 40.75904):
                                                                    return u'True'
                                                                if (pickup_latitude <= 40.75904):
                                                                    return u'False'
                                                            if (pickup_latitude <= 40.75579):
                                                                return u'True'
                                                        if (pickup_latitude <= 40.75192):
                                                            return u'False'
                                                    if (pickup_longitude <= -73.99428):
                                                        return u'True'
                                            if (tpep_pickup_datetime_day_of_month <= 6):
                                                if (pickup_latitude > 40.75225):
                                                    if (pickup_longitude > -74.00015):
                                                        return u'True'
                                                    if (pickup_longitude <= -74.00015):
                                                        return u'False'
                                                if (pickup_latitude <= 40.75225):
                                                    return u'False'
                                if (pickup_longitude <= -74.00147):
                                    return u'True'
                            if (tpep_pickup_datetime_hour <= 9):
                                if (tpep_pickup_datetime_hour > 6):
                                    if (pickup_longitude > -73.9969):
                                        if (pickup_latitude > 40.76517):
                                            if (pickup_latitude > 40.79404):
                                                return u'True'
                                            if (pickup_latitude <= 40.79404):
                                                if (pickup_longitude > -73.98793):
                                                    if (tpep_pickup_datetime_day_of_month > 5):
                                                        if (pickup_longitude > -73.95667):
                                                            return u'True'
                                                        if (pickup_longitude <= -73.95667):
                                                            if (pickup_longitude > -73.97051):
                                                                return u'True'
                                                            if (pickup_longitude <= -73.97051):
                                                                return u'True'
                                                    if (tpep_pickup_datetime_day_of_month <= 5):
                                                        return u'True'
                                                if (pickup_longitude <= -73.98793):
                                                    return u'True'
                                        if (pickup_latitude <= 40.76517):
                                            if (pickup_longitude > -73.97431):
                                                return u'True'
                                            if (pickup_longitude <= -73.97431):
                                                if (tpep_pickup_datetime_hour > 7):
                                                    if (pickup_longitude > -73.99168):
                                                        if (pickup_longitude > -73.98941):
                                                            return u'True'
                                                        if (pickup_longitude <= -73.98941):
                                                            return u'True'
                                                    if (pickup_longitude <= -73.99168):
                                                        return u'True'
                                                if (tpep_pickup_datetime_hour <= 7):
                                                    return u'True'
                                    if (pickup_longitude <= -73.9969):
                                        return u'True'
                                if (tpep_pickup_datetime_hour <= 6):
                                    if (pickup_longitude > -73.98675):
                                        if (pickup_latitude > 40.81262):
                                            return u'False'
                                        if (pickup_latitude <= 40.81262):
                                            if (tpep_pickup_datetime_day_of_week > 1):
                                                if (pickup_longitude > -73.97035):
                                                    return u'True'
                                                if (pickup_longitude <= -73.97035):
                                                    return u'True'
                                            if (tpep_pickup_datetime_day_of_week <= 1):
                                                return u'True'
                                    if (pickup_longitude <= -73.98675):
                                        return u'False'
        if (tpep_pickup_datetime_day_of_month <= 4):
            if (pickup_latitude > 40.7645):
                if (pickup_latitude > 40.80567):
                    return u'False'
                if (pickup_latitude <= 40.80567):
                    if (pickup_longitude is None):
                        return u'True'
                    if (pickup_longitude > -73.88802):
                        return u'True'
                    if (pickup_longitude <= -73.88802):
                        if (pickup_longitude > -73.94389):
                            return u'False'
                        if (pickup_longitude <= -73.94389):
                            if (pickup_longitude > -73.98629):
                                if (pickup_longitude > -73.96119):
                                    if (pickup_longitude > -73.94654):
                                        return u'False'
                                    if (pickup_longitude <= -73.94654):
                                        if (pickup_latitude > 40.79328):
                                            return u'False'
                                        if (pickup_latitude <= 40.79328):
                                            return u'True'
                                if (pickup_longitude <= -73.96119):
                                    if (pickup_latitude > 40.76587):
                                        if (tpep_pickup_datetime_hour is None):
                                            return u'False'
                                        if (tpep_pickup_datetime_hour > 18):
                                            return u'True'
                                        if (tpep_pickup_datetime_hour <= 18):
                                            if (pickup_longitude > -73.96469):
                                                return u'False'
                                            if (pickup_longitude <= -73.96469):
                                                return u'False'
                                    if (pickup_latitude <= 40.76587):
                                        return u'False'
                            if (pickup_longitude <= -73.98629):
                                return u'True'
            if (pickup_latitude <= 40.7645):
                if (tpep_pickup_datetime_day_of_week is None):
                    return u'False'
                if (tpep_pickup_datetime_day_of_week > 6):
                    return u'False'
                if (tpep_pickup_datetime_day_of_week <= 6):
                    if (pickup_longitude is None):
                        return u'False'
                    if (pickup_longitude > -73.97042):
                        return u'False'
                    if (pickup_longitude <= -73.97042):
                        if (pickup_longitude > -73.99275):
                            if (pickup_longitude > -73.97249):
                                return u'False'
                            if (pickup_longitude <= -73.97249):
                                if (tpep_pickup_datetime_hour is None):
                                    return u'False'
                                if (tpep_pickup_datetime_hour > 19):
                                    return u'False'
                                if (tpep_pickup_datetime_hour <= 19):
                                    if (tpep_pickup_datetime_hour > 4):
                                        if (tpep_pickup_datetime_hour > 13):
                                            return u'False'
                                        if (tpep_pickup_datetime_hour <= 13):
                                            return u'False'
                                    if (tpep_pickup_datetime_hour <= 4):
                                        return u'False'
                        if (pickup_longitude <= -73.99275):
                            return u'False'
    if (pickup_latitude <= 40.74894):
        if (tpep_pickup_datetime_day_of_month is None):
            return u'True'
        if (tpep_pickup_datetime_day_of_month > 5):
            if (pickup_longitude is None):
                return u'True'
            if (pickup_longitude > -73.97014):
                if (pickup_latitude > 40.73215):
                    return u'False'
                if (pickup_latitude <= 40.73215):
                    if (pickup_latitude > 40.7066):
                        return u'True'
                    if (pickup_latitude <= 40.7066):
                        if (pickup_longitude > -73.81012):
                            if (pickup_longitude > -73.79062):
                                if (pickup_longitude > -73.78907):
                                    return u'True'
                                if (pickup_longitude <= -73.78907):
                                    return u'True'
                            if (pickup_longitude <= -73.79062):
                                return u'True'
                        if (pickup_longitude <= -73.81012):
                            return u'False'
            if (pickup_longitude <= -73.97014):
                if (tpep_pickup_datetime_hour is None):
                    return u'True'
                if (tpep_pickup_datetime_hour > 18):
                    if (pickup_latitude > 40.69113):
                        if (pickup_longitude > -74.00707):
                            if (pickup_latitude > 40.74553):
                                if (pickup_longitude > -73.97539):
                                    return u'True'
                                if (pickup_longitude <= -73.97539):
                                    return u'True'
                            if (pickup_latitude <= 40.74553):
                                if (pickup_longitude > -73.99327):
                                    if (pickup_latitude > 40.72739):
                                        if (tpep_pickup_datetime_day_of_month > 30):
                                            return u'True'
                                        if (tpep_pickup_datetime_day_of_month <= 30):
                                            if (pickup_longitude > -73.973):
                                                return u'True'
                                            if (pickup_longitude <= -73.973):
                                                if (pickup_latitude > 40.73812):
                                                    if (pickup_latitude > 40.74157):
                                                        return u'True'
                                                    if (pickup_latitude <= 40.74157):
                                                        return u'True'
                                                if (pickup_latitude <= 40.73812):
                                                    if (tpep_pickup_datetime_second is None):
                                                        return u'True'
                                                    if (tpep_pickup_datetime_second > 49):
                                                        return u'True'
                                                    if (tpep_pickup_datetime_second <= 49):
                                                        if (tpep_pickup_datetime_second > 32):
                                                            return u'True'
                                                        if (tpep_pickup_datetime_second <= 32):
                                                            return u'True'
                                    if (pickup_latitude <= 40.72739):
                                        if (tpep_pickup_datetime_second is None):
                                            return u'True'
                                        if (tpep_pickup_datetime_second > 46):
                                            return u'True'
                                        if (tpep_pickup_datetime_second <= 46):
                                            return u'True'
                                if (pickup_longitude <= -73.99327):
                                    if (tpep_pickup_datetime_day_of_week is None):
                                        return u'True'
                                    if (tpep_pickup_datetime_day_of_week > 4):
                                        if (pickup_latitude > 40.73946):
                                            return u'True'
                                        if (pickup_latitude <= 40.73946):
                                            if (tpep_pickup_datetime_minute is None):
                                                return u'True'
                                            if (tpep_pickup_datetime_minute > 4):
                                                if (pickup_latitude > 40.70796):
                                                    if (pickup_latitude > 40.72126):
                                                        if (tpep_pickup_datetime_minute > 54):
                                                            return u'True'
                                                        if (tpep_pickup_datetime_minute <= 54):
                                                            return u'True'
                                                    if (pickup_latitude <= 40.72126):
                                                        return u'True'
                                                if (pickup_latitude <= 40.70796):
                                                    return u'True'
                                            if (tpep_pickup_datetime_minute <= 4):
                                                return u'True'
                                    if (tpep_pickup_datetime_day_of_week <= 4):
                                        if (pickup_longitude > -74.00489):
                                            if (tpep_pickup_datetime_day_of_month > 27):
                                                return u'True'
                                            if (tpep_pickup_datetime_day_of_month <= 27):
                                                if (tpep_pickup_datetime_second is None):
                                                    return u'True'
                                                if (tpep_pickup_datetime_second > 13):
                                                    return u'True'
                                                if (tpep_pickup_datetime_second <= 13):
                                                    return u'True'
                                        if (pickup_longitude <= -74.00489):
                                            return u'True'
                        if (pickup_longitude <= -74.00707):
                            if (tpep_pickup_datetime_day_of_week is None):
                                return u'True'
                            if (tpep_pickup_datetime_day_of_week > 5):
                                return u'True'
                            if (tpep_pickup_datetime_day_of_week <= 5):
                                return u'True'
                    if (pickup_latitude <= 40.69113):
                        return u'True'
                if (tpep_pickup_datetime_hour <= 18):
                    if (tpep_pickup_datetime_hour > 10):
                        if (tpep_pickup_datetime_hour > 17):
                            if (tpep_pickup_datetime_day_of_week is None):
                                return u'True'
                            if (tpep_pickup_datetime_day_of_week > 5):
                                return u'True'
                            if (tpep_pickup_datetime_day_of_week <= 5):
                                if (pickup_longitude > -74.00605):
                                    if (pickup_latitude > 40.72032):
                                        if (pickup_latitude > 40.74584):
                                            return u'True'
                                        if (pickup_latitude <= 40.74584):
                                            return u'True'
                                    if (pickup_latitude <= 40.72032):
                                        return u'True'
                                if (pickup_longitude <= -74.00605):
                                    return u'True'
                        if (tpep_pickup_datetime_hour <= 17):
                            if (tpep_pickup_datetime_day_of_month > 8):
                                if (pickup_longitude > -73.97779):
                                    return u'True'
                                if (pickup_longitude <= -73.97779):
                                    if (pickup_latitude > 40.74621):
                                        return u'True'
                                    if (pickup_latitude <= 40.74621):
                                        if (pickup_latitude > 40.71269):
                                            if (pickup_longitude > -74.0062):
                                                if (pickup_latitude > 40.7183):
                                                    if (tpep_pickup_datetime_hour > 16):
                                                        return u'True'
                                                    if (tpep_pickup_datetime_hour <= 16):
                                                        if (pickup_latitude > 40.72081):
                                                            if (tpep_pickup_datetime_day_of_week is None):
                                                                return u'True'
                                                            if (tpep_pickup_datetime_day_of_week > 5):
                                                                if (pickup_longitude > -73.98214):
                                                                    return u'True'
                                                                if (pickup_longitude <= -73.98214):
                                                                    if (pickup_longitude > -74.0033):
                                                                        if (pickup_latitude > 40.74144):
                                                                            return u'True'
                                                                        if (pickup_latitude <= 40.74144):
                                                                            if (tpep_pickup_datetime_minute is None):
                                                                                return u'True'
                                                                            if (tpep_pickup_datetime_minute > 28):
                                                                                return u'True'
                                                                            if (tpep_pickup_datetime_minute <= 28):
                                                                                return u'True'
                                                                    if (pickup_longitude <= -74.0033):
                                                                        return u'True'
                                                            if (tpep_pickup_datetime_day_of_week <= 5):
                                                                if (pickup_longitude > -73.98242):
                                                                    return u'True'
                                                                if (pickup_longitude <= -73.98242):
                                                                    if (pickup_longitude > -74.00508):
                                                                        if (pickup_latitude > 40.73603):
                                                                            if (pickup_longitude > -73.9946):
                                                                                return u'True'
                                                                            if (pickup_longitude <= -73.9946):
                                                                                return u'True'
                                                                        if (pickup_latitude <= 40.73603):
                                                                            if (tpep_pickup_datetime_day_of_month > 12):
                                                                                return u'True'
                                                                            if (tpep_pickup_datetime_day_of_month <= 12):
                                                                                return u'True'
                                                                    if (pickup_longitude <= -74.00508):
                                                                        return u'True'
                                                        if (pickup_latitude <= 40.72081):
                                                            return u'True'
                                                if (pickup_latitude <= 40.7183):
                                                    return u'True'
                                            if (pickup_longitude <= -74.0062):
                                                return u'True'
                                        if (pickup_latitude <= 40.71269):
                                            return u'True'
                            if (tpep_pickup_datetime_day_of_month <= 8):
                                if (pickup_longitude > -73.98537):
                                    return u'True'
                                if (pickup_longitude <= -73.98537):
                                    return u'True'
                    if (tpep_pickup_datetime_hour <= 10):
                        if (tpep_pickup_datetime_hour > 5):
                            if (tpep_pickup_datetime_day_of_week is None):
                                return u'True'
                            if (tpep_pickup_datetime_day_of_week > 5):
                                if (pickup_longitude > -73.98148):
                                    return u'True'
                                if (pickup_longitude <= -73.98148):
                                    return u'True'
                            if (tpep_pickup_datetime_day_of_week <= 5):
                                if (tpep_pickup_datetime_hour > 9):
                                    return u'True'
                                if (tpep_pickup_datetime_hour <= 9):
                                    if (pickup_latitude > 40.74638):
                                        return u'True'
                                    if (pickup_latitude <= 40.74638):
                                        if (tpep_pickup_datetime_day_of_week > 2):
                                            if (pickup_latitude > 40.73834):
                                                return u'True'
                                            if (pickup_latitude <= 40.73834):
                                                if (pickup_longitude > -74.00228):
                                                    return u'True'
                                                if (pickup_longitude <= -74.00228):
                                                    return u'True'
                                        if (tpep_pickup_datetime_day_of_week <= 2):
                                            return u'True'
                        if (tpep_pickup_datetime_hour <= 5):
                            if (tpep_pickup_datetime_day_of_week is None):
                                return u'True'
                            if (tpep_pickup_datetime_day_of_week > 5):
                                if (tpep_pickup_datetime_hour > 3):
                                    return u'True'
                                if (tpep_pickup_datetime_hour <= 3):
                                    if (pickup_latitude > 40.70585):
                                        if (pickup_latitude > 40.73878):
                                            return u'True'
                                        if (pickup_latitude <= 40.73878):
                                            if (pickup_longitude > -73.99269):
                                                return u'True'
                                            if (pickup_longitude <= -73.99269):
                                                return u'True'
                                    if (pickup_latitude <= 40.70585):
                                        return u'True'
                            if (tpep_pickup_datetime_day_of_week <= 5):
                                if (tpep_pickup_datetime_hour > 0):
                                    if (tpep_pickup_datetime_hour > 4):
                                        return u'True'
                                    if (tpep_pickup_datetime_hour <= 4):
                                        if (tpep_pickup_datetime_hour > 3):
                                            return u'False'
                                        if (tpep_pickup_datetime_hour <= 3):
                                            return u'True'
                                if (tpep_pickup_datetime_hour <= 0):
                                    return u'True'
        if (tpep_pickup_datetime_day_of_month <= 5):
            if (tpep_pickup_datetime_day_of_month > 2):
                if (tpep_pickup_datetime_hour is None):
                    return u'True'
                if (tpep_pickup_datetime_hour > 18):
                    return u'True'
                if (tpep_pickup_datetime_hour <= 18):
                    if (tpep_pickup_datetime_hour > 9):
                        if (pickup_longitude is None):
                            return u'True'
                        if (pickup_longitude > -74.01024):
                            if (pickup_latitude > 40.74629):
                                return u'True'
                            if (pickup_latitude <= 40.74629):
                                if (pickup_longitude > -73.98383):
                                    return u'True'
                                if (pickup_longitude <= -73.98383):
                                    return u'True'
                        if (pickup_longitude <= -74.01024):
                            return u'False'
                    if (tpep_pickup_datetime_hour <= 9):
                        if (pickup_longitude is None):
                            return u'True'
                        if (pickup_longitude > -73.97456):
                            return u'True'
                        if (pickup_longitude <= -73.97456):
                            return u'True'
            if (tpep_pickup_datetime_day_of_month <= 2):
                if (tpep_pickup_datetime_hour is None):
                    return u'True'
                if (tpep_pickup_datetime_hour > 19):
                    return u'True'
                if (tpep_pickup_datetime_hour <= 19):
                    if (pickup_latitude > 40.71699):
                        if (pickup_longitude is None):
                            return u'True'
                        if (pickup_longitude > -73.89763):
                            return u'False'
                        if (pickup_longitude <= -73.89763):
                            if (tpep_pickup_datetime_hour > 2):
                                if (pickup_longitude > -73.98341):
                                    return u'True'
                                if (pickup_longitude <= -73.98341):
                                    if (pickup_longitude > -73.98575):
                                        return u'False'
                                    if (pickup_longitude <= -73.98575):
                                        return u'True'
                            if (tpep_pickup_datetime_hour <= 2):
                                return u'True'
                    if (pickup_latitude <= 40.71699):
                        return u'False'



args = parser.parse_args()
# print(args)
address = ' '.join(args.address)                #string
day_of_month = args.day_of_month                #number {1 to 31}
hour = args.hour                                #number {1 to 23}
minute = args.minute                            #number {1 to 59}
second = args.second                            #number {1 to 59}
day_of_week = args.day_of_week                  #number {1 to 7}

geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode(address)



if location is None:
    print(f'unknown location {address}')
else:
    # print(f'DEBUG: address: {address}, day_of_month: {day_of_month}, day_of_week: {day_of_week} hour: {hour}, minute: {minute}, second: {second}')
    # print(f'DEBUG: location coordinates: {location.latitude}/{location.longitude}')
    fare = predict_fare_split(location.longitude, location.latitude, day_of_month, day_of_week, hour)
    if fare is '1st':
        fare = 'less than ' + MEDIAN
    else:
        fare = 'more than ' + MEDIAN

    tip = predict_tip_exists(location.longitude, location.latitude, day_of_month, day_of_week, hour, minute, second)
    if tip is 'True':
        tip = 'a tip'
    else:
        tip = 'no tip'

    print(f'we predict that this ride will be {fare} and we expect {tip}')