"""In this code file I have basic async function that I can use in my future coding projectsl."""
import asyncio # Importing asyncio module
import httplib2 # basic module that allows api calls

async def get_request_test():
    """Basic async function that makes a get request to a website and prints the response."""
    h = httplib2.Http()
    header = {"Accept" : "*/*"}
    response = h.request(uri="https://reqbin.com/echo", headers=header)
    return response

async def function_that_makes_a_get_request():
    """waits for a multiple get requests and prints the response."""
    results = await asyncio.gather(*[get_request_test() for _ in range(10)])
    for i in results:
        print(i)

async def hello_world_test():
    """Basic async function that prints "Hello world" then waits for 1 second
    and print "Hello again!"."""
    print("Hello world")
    await asyncio.sleep(1)
    print("Hello again!")

if __name__ == "__main__":
    # asyncio.run(hello_world_test())
    asyncio.run(function_that_makes_a_get_request())