import time

from win11toast import toast
from alerts_in_ua import Client as AlertsClient

from config import API


def message():
    toast("В вашій області повітряна тривога")


def alarm() -> bool:
    alerts_client = AlertsClient(token=API)
    alert_status = alerts_client.get_air_raid_alert_status('Рівненська область')
    if alert_status.status == 'active':
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        if alarm():
            message()
        time.sleep(1)