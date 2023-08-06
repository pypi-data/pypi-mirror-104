"""
    Binance ticker class.
    Copyright (C) 2021  Emerson Dove

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import websocket
from Blankly.exchanges.IExchange_Websocket import IExchangeWebsocket
import Blankly.exchanges.Binance.websocket_utils as websocket_utils
import collections
import json
import Blankly
import threading
import traceback


class Tickers(IExchangeWebsocket):
    def __init__(self, symbol, stream, log=None, WEBSOCKET_URL="wss://stream.binance.com:9443/ws"):
        """
        Create and initialize the ticker
        Args:
            symbol: Currency to initialize on such as "btcusdt"
            stream: Stream to use, such as "depth" or "trade"
            log: Fill this with a path to a log file that should be created
            WEBSOCKET_URL: Default websocket URL feed.
        """
        self.__id = symbol
        self.__stream = stream
        self.__message_callback = websocket_utils.switch_type(stream)

        # Initialize log file
        if log is not None:
            self.__log = True
            self.__filePath = log
            try:
                self.__file = open(log, 'x+')
                self.__file.write(
                    "event_time,system_time,event_type,symbol,trade_id,price,quantity,buyer_order_id,seller_order_id,"
                    "trade_time,buyer_is_maker\n")
            except FileExistsError:
                self.__file = open(log, 'a')
        else:
            self.__log = False

        self.URL = WEBSOCKET_URL
        self.ws = None
        self.__response = None
        self.__most_recent_tick = None
        self.__most_recent_time = None
        # Create the thread object here
        self.__thread = threading.Thread(target=self.read_websocket)
        self.__callbacks = []
        # This is created so that we know when a message has come back that we're waiting for
        self.__message_count = 0

        # Reload preferences
        self.__preferences = Blankly.utils.load_user_preferences()
        buffer_size = self.__preferences["settings"]["websocket_buffer_size"]
        self.__ticker_feed = collections.deque(maxlen=buffer_size)
        self.__time_feed = collections.deque(maxlen=buffer_size)

        # Start the websocket
        self.start_websocket()

    def start_websocket(self):
        """
        Restart websocket if it was asked to stop.
        """
        if self.ws is None:
            self.ws = websocket.WebSocketApp(self.URL,
                                             on_open=self.on_open,
                                             on_message=self.on_message,
                                             on_error=self.on_error,
                                             on_close=self.on_close)
            self.__thread = threading.Thread(target=self.read_websocket)
            self.__thread.start()
        else:
            if self.__thread.is_alive():
                print("Already running...")
                pass
            else:
                # Use recursion to restart, continue appending to time feed and ticker feed
                self.ws = None
                self.start_websocket()

    def read_websocket(self):
        # Main thread to sit here and run
        """
        Response from trade streams
        {
            'e': 'trade',  # Event Type
            'E': 1619149864634,  # Event time
            's': 'BTCUSDT', # Symbol
            't': 787178035,  # Trade ID
            'p': '50322.05000000',  # Price
            'q': '0.00577200',  # Quantity
            'b': 5644954701,  # Buyer order id
            'a': 5644954632,  # Seller order id
            'T': 1619149864634,  # Trade time
            'm': False,  # Is the buyer the market maker?
            'M': True  # Ignore
        }

        Similar ticks with coinbase pro
        {
            'type': 'ticker',
            'product_id': 'BTC-USD',
            'price': '50141.55',
            'time': 1619286924.397969,
            'trade_id': 160775277,
        }
        """
        self.ws.run_forever()
        # This repeats the close behavior just in case something happens

    def on_message(self, ws, message):
        self.__message_count += 1
        message = json.loads(message)
        try:
            self.__most_recent_time = message['E']
            self.__time_feed.append(self.__most_recent_time)
            self.__most_recent_tick = message
            self.__ticker_feed.append(self.__most_recent_tick)
            # Run callbacks on message
            for i in self.__callbacks:
                i(message)

            if self.__log:
                if self.__message_count % 100 == 0:
                    self.__file.close()
                    self.__file = open(self.__filePath, 'a')
                line = self.__message_callback(message)
                self.__file.write(line)
        except KeyError:
            try:
                if message['result'] is None:
                    self.__response = message
            except KeyError:
                traceback.print_exc()

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        # This repeats the close behavior just in case something happens
        pass

    def on_open(self, ws):
        request = """
        {
            "method": "SUBSCRIBE",
            "params": [
                \"""" + self.__id + "@" + self.__stream + """\"
            ],
            "id": 1
        }
        """
        ws.send(request)

    """ Required in manager """
    def is_websocket_open(self):
        return self.__thread.is_alive()

    def get_currency_id(self):
        return self.__id

    """ Required in manager """
    def append_callback(self, obj):
        self.__callbacks.append(obj)

    """ Define a variable each time so there is no array manipulation """
    """ Required in manager """
    def get_most_recent_tick(self):
        return self.__most_recent_tick

    """ Required in manager """
    def get_most_recent_time(self):
        return self.__most_recent_time

    """ Required in manager """
    def get_time_feed(self):
        return list(self.__time_feed)

    """ Parallel with time feed """
    """ Required in manager """
    def get_feed(self):
        return list(self.__ticker_feed)

    """ Required in manager """
    def get_response(self):
        return self.__response

    """ Required in manager """
    def close_websocket(self):
        if self.__thread.is_alive():
            self.ws.close()
        else:
            print("Websocket for " + self.__id + '@' + self.__stream + " is already closed")

    """ Required in manager """
    def restart_ticker(self):
        self.start_websocket()
