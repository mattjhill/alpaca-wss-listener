import logging
import time 

from alpaca_trade_api.stream import Stream
from alpaca_trade_api.common import URL

log = logging.getLogger(__name__)


async def handle_trade_updates(event):
    log.info(event)

async def handle_bars(event):
    log.info({'event': 'bar', 'bar': event})

def run_connection(conn):
    try:
        conn.run()
    except Exception as e:
        log.warning(f'Exception from websocket connection: {e}')
    finally:
        log.warning("Trying to re-establish connection")
        time.sleep(3)
        run_connection(conn)

def main():
    logging.basicConfig(level=logging.INFO)
    stream = Stream(data_feed='sip', base_url=URL('https://paper-api.alpaca.markets'))
    stream.subscribe_trade_updates(handle_trade_updates)
    stream.subscribe_bars(handle_bars, '*')
    stream.run()

if __name__ == "__main__":
    main()