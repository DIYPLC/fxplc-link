import asyncio
from contextlib import closing
from fxplc.client.FXPLCClient import FXPLCClient
from fxplc.transports.TransportSerial import TransportSerial

"""
Clone PLC FX3U-24MR link test.

from fxplc.transports.TransportSerial import TransportSerial
     ^     ^          ^                      ^
     |     |          |                      |
     dir   dir        file                  class
"""

async def main():
    transport = TransportSerial(port="COM1", baudrate=38400)
    with closing(FXPLCClient(transport)) as fx:
        Y0 = await fx.read_bit("Y0")
        print("Y0 =", Y0)
        X0 = await fx.read_bit("X0")
        print("X0 =", X0)
        M500 = await fx.read_bit("M500")
        print("M500 =", M500)
        D201 = await fx.read_int("D201")
        print("D201 =", D201)
        D201 = D201 + 1
        await fx.write_int("D201", D201)

asyncio.run(main())
input("press any key for exit...")
