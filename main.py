import logging

from alpaca_trade_api.stream import Stream
from alpaca_trade_api.common import URL

log = logging.getLogger(__name__)


async def handle_event(event):
    log.info(event)

def run_connection(conn):
    try:
        conn.run()
    except Exception as e:
        print(f'Exception from websocket connection: {e}')
    finally:
        print("Trying to re-establish connection")
        time.sleep(3)
        run_connection(conn)

def main():
    logging.basicConfig(level=logging.INFO)
    stream = Stream(data_feed='sip', raw_data=True, base_url=URL('https://paper-api.alpaca.markets'))
    stream.subscribe_trade_updates(handle_event)
    stream.subscribe_bars(handle_event, '*')
    stream.run()

if __name__ == "__main__":
    main()