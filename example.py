"""Example usage of pykmtronic."""
import asyncio
import aiohttp
import time
import logging

from pykmtronic.auth import Auth
from pykmtronic.hub import KMTronicHubAPI

logging.basicConfig(level=logging.DEBUG)


async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, "http://192.168.1.160", "admin", "admin")
        api = KMTronicHubAPI(auth)

        relays = await api.async_get_relays()

        r = relays[0]

        print("is relay1 ON?", r.is_energised)
        await r.energise()
        time.sleep(2)
        print("is relay1 ON?", r.is_energised)

        await r.de_energise()
        time.sleep(2)
        await api.async_update_relays()
        print("is relay1 ON?", r.is_energised)


        time.sleep(2)
        await r.toggle()
        time.sleep(2)
        await api.async_update_relays()
        print("is relay1 ON?", r.is_energised)
        time.sleep(2)
        await r.toggle()
        time.sleep(2)
        await api.async_update_relays()
        print("is relay1 ON?", r.is_energised)

asyncio.run(main())
