import asyncio
import aiohttp
import time
from http.client import HTTPConnection
from urllib.parse import urlparse

def site_is_online(url, timeout = 2):
    """ Return True if the target URL is online.
    Raise an exception otherwise.
    """
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]

    for port in (80, 443):
        connection = HTTPConnection(host = host, port = port, timeout = timeout)
        try:
            start_time = time.perf_counter()
            connection.request("HEAD", "/")
            end_time = time.perf_counter()
            response_time = end_time - start_time
            return True, response_time
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error

async def async_site_is_online(url, timeout = 2):
    """ Return True if the target URL is online.
    Raise an exception otherwise.
    """
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for scheme in ("http", "https"):
        target_url = scheme + "://" + host
        async with aiohttp.ClientSession() as session:
            try:
                start_time = time.perf_counter()
                await session.head(target_url, timeout = timeout)
                end_time = time.perf_counter()
                time_response = end_time - start_time
                return True, time_response
            except asyncio.exceptions.TimeoutError:
                error = Exception("timed out")
            except Exception as e:
                error = e
    raise error
