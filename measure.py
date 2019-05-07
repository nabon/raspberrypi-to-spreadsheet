#!/usr/bin/env python3

import json
import urllib.request
from bme280i2c import BME280I2C
from tsl2561 import TSL2561
from tsl2572 import TSL2572
from datetime import datetime

def main():
    bme280ch1 = BME280I2C(0x76)
    bme280ch2 = BME280I2C(0x77)
    tsl2561 = TSL2561(0x29)
    tsl2572 = TSL2572(0x39)
    r1 = bme280ch1.meas()
    r2 = bme280ch2.meas()
    r3 = tsl2561.meas_single()
    r4 = tsl2572.meas_single()

    jsondata = {"date":datetime.now().strftime("%Y/%m/%d %H:%M:%S")}

    if not (r1 or r2 or r3):
        print("No Sensor Available")

    if r1:
        jsondata["temperature"] = "{:.1f}".format(bme280ch1.T)
        jsondata["atmospheric-pressure"] = "{:.1f}".format(bme280ch1.P)
        jsondata["humidity"] = "{:.1f}".format(bme280ch1.H)

#    if r2:
#    if r3:

    if r4:
        jsondata["illuminance"] = "{:.1f}".format(tsl2572.lux)

    url = "<URL of web application>"
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(url, json.dumps(jsondata).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()

if __name__ == "__main__":
    main()
