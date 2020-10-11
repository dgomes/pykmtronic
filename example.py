import asyncio
import aiohttp
import time
import logging

logging.basicConfig(level=logging.DEBUG)

from pykmtronic.auth import Auth
from pykmtronic.hub import KMTronicHubAPI

async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, "http://192.168.1.247", "admin", "admin")
        api = KMTronicHubAPI(auth)

        relays = await api.async_get_relays()

        r = relays[0]

        print("is relay1 ON?", r.is_on)
        await r.turn_on()
        time.sleep(2)
        print("is relay1 ON?", r.is_on)
            
        await r.turn_off()
        time.sleep(2)
        await api.async_update_relays()
        print("is relay1 ON?", r.is_on)
        

asyncio.run(main())
