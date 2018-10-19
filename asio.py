import asyncio
import concurrent.futures
import requests

async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor, 
                requests.post( "http://localhost:5000/api/auth/signin" ,json={
	                "usernameOrEmail" : "minhlevan104@gmail.com",
	                "password" : "minh123"
                })
            )
            for i in range(1000)
        ]
        for response in await asyncio.gather(*futures):
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(main())