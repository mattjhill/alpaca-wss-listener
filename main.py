import logging

from alpaca_trade_api.stream import Stream

log = logging.getLogger(__name__)


async def handle_event(event):
    log.info(event)

def main():
    logging.basicConfig(level=logging.INFO)
    stream = Stream(data_feed='sip', raw_data=True)
    stream.subscribe_trade_updates(handle_event)
    stream.subscribe_bars(handle_event, '*')
    stream.run()

if __name__ == "__main__":
    main()