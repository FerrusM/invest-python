# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinkoff/invest/grpc/marketdata.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from tinkoff.invest.grpc import (
    common_pb2 as tinkoff_dot_invest_dot_grpc_dot_common__pb2,
)
from tinkoff.invest.grpc.google.api import (
    field_behavior_pb2 as tinkoff_dot_invest_dot_grpc_dot_google_dot_api_dot_field__behavior__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$tinkoff/invest/grpc/marketdata.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a tinkoff/invest/grpc/common.proto\x1a\x33tinkoff/invest/grpc/google/api/field_behavior.proto\"\xf4\x04\n\x11MarketDataRequest\x12\x63\n\x19subscribe_candles_request\x18\x01 \x01(\x0b\x32>.tinkoff.public.invest.api.contract.v1.SubscribeCandlesRequestH\x00\x12h\n\x1csubscribe_order_book_request\x18\x02 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeOrderBookRequestH\x00\x12\x61\n\x18subscribe_trades_request\x18\x03 \x01(\x0b\x32=.tinkoff.public.invest.api.contract.v1.SubscribeTradesRequestH\x00\x12]\n\x16subscribe_info_request\x18\x04 \x01(\x0b\x32;.tinkoff.public.invest.api.contract.v1.SubscribeInfoRequestH\x00\x12h\n\x1csubscribe_last_price_request\x18\x05 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeLastPriceRequestH\x00\x12Y\n\x14get_my_subscriptions\x18\x06 \x01(\x0b\x32\x39.tinkoff.public.invest.api.contract.v1.GetMySubscriptionsH\x00\x42\t\n\x07payload\"\x94\x04\n!MarketDataServerSideStreamRequest\x12\x61\n\x19subscribe_candles_request\x18\x01 \x01(\x0b\x32>.tinkoff.public.invest.api.contract.v1.SubscribeCandlesRequest\x12\x66\n\x1csubscribe_order_book_request\x18\x02 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeOrderBookRequest\x12_\n\x18subscribe_trades_request\x18\x03 \x01(\x0b\x32=.tinkoff.public.invest.api.contract.v1.SubscribeTradesRequest\x12[\n\x16subscribe_info_request\x18\x04 \x01(\x0b\x32;.tinkoff.public.invest.api.contract.v1.SubscribeInfoRequest\x12\x66\n\x1csubscribe_last_price_request\x18\x05 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeLastPriceRequest\"\xc0\x07\n\x12MarketDataResponse\x12\x65\n\x1asubscribe_candles_response\x18\x01 \x01(\x0b\x32?.tinkoff.public.invest.api.contract.v1.SubscribeCandlesResponseH\x00\x12j\n\x1dsubscribe_order_book_response\x18\x02 \x01(\x0b\x32\x41.tinkoff.public.invest.api.contract.v1.SubscribeOrderBookResponseH\x00\x12\x63\n\x19subscribe_trades_response\x18\x03 \x01(\x0b\x32>.tinkoff.public.invest.api.contract.v1.SubscribeTradesResponseH\x00\x12_\n\x17subscribe_info_response\x18\x04 \x01(\x0b\x32<.tinkoff.public.invest.api.contract.v1.SubscribeInfoResponseH\x00\x12?\n\x06\x63\x61ndle\x18\x05 \x01(\x0b\x32-.tinkoff.public.invest.api.contract.v1.CandleH\x00\x12=\n\x05trade\x18\x06 \x01(\x0b\x32,.tinkoff.public.invest.api.contract.v1.TradeH\x00\x12\x45\n\torderbook\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.OrderBookH\x00\x12N\n\x0etrading_status\x18\x08 \x01(\x0b\x32\x34.tinkoff.public.invest.api.contract.v1.TradingStatusH\x00\x12;\n\x04ping\x18\t \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x12j\n\x1dsubscribe_last_price_response\x18\n \x01(\x0b\x32\x41.tinkoff.public.invest.api.contract.v1.SubscribeLastPriceResponseH\x00\x12\x46\n\nlast_price\x18\x0b \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.LastPriceH\x00\x42\t\n\x07payload\"\xd6\x01\n\x17SubscribeCandlesRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12L\n\x0binstruments\x18\x02 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.CandleInstrument\x12\x15\n\rwaiting_close\x18\x03 \x01(\x08\"\x8a\x01\n\x10\x43\x61ndleInstrument\x12\x10\n\x04\x66igi\x18\x01 \x01(\tB\x02\x18\x01\x12M\n\x08interval\x18\x02 \x01(\x0e\x32;.tinkoff.public.invest.api.contract.v1.SubscriptionInterval\x12\x15\n\rinstrument_id\x18\x03 \x01(\t\"\x89\x01\n\x18SubscribeCandlesResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12X\n\x15\x63\x61ndles_subscriptions\x18\x02 \x03(\x0b\x32\x39.tinkoff.public.invest.api.contract.v1.CandleSubscription\"\xa4\x02\n\x12\x43\x61ndleSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12M\n\x08interval\x18\x02 \x01(\x0e\x32;.tinkoff.public.invest.api.contract.v1.SubscriptionInterval\x12V\n\x13subscription_status\x18\x03 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\x12\x16\n\x0einstrument_uid\x18\x04 \x01(\t\x12\x15\n\rwaiting_close\x18\x05 \x01(\x08\x12\x11\n\tstream_id\x18\x06 \x01(\t\x12\x17\n\x0fsubscription_id\x18\x07 \x01(\t\"\xc4\x01\n\x19SubscribeOrderBookRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12O\n\x0binstruments\x18\x02 \x03(\x0b\x32:.tinkoff.public.invest.api.contract.v1.OrderBookInstrument\"\x9c\x01\n\x13OrderBookInstrument\x12\x10\n\x04\x66igi\x18\x01 \x01(\tB\x02\x18\x01\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12\x15\n\rinstrument_id\x18\x03 \x01(\t\x12M\n\x0forder_book_type\x18\x04 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.OrderBookType\"\x91\x01\n\x1aSubscribeOrderBookResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12^\n\x18order_book_subscriptions\x18\x02 \x03(\x0b\x32<.tinkoff.public.invest.api.contract.v1.OrderBookSubscription\"\x9f\x02\n\x15OrderBookSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12V\n\x13subscription_status\x18\x03 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\x12\x16\n\x0einstrument_uid\x18\x04 \x01(\t\x12\x11\n\tstream_id\x18\x05 \x01(\t\x12\x17\n\x0fsubscription_id\x18\x06 \x01(\t\x12M\n\x0forder_book_type\x18\x07 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.OrderBookType\"\xbd\x01\n\x16SubscribeTradesRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12K\n\x0binstruments\x18\x02 \x03(\x0b\x32\x36.tinkoff.public.invest.api.contract.v1.TradeInstrument\":\n\x0fTradeInstrument\x12\x10\n\x04\x66igi\x18\x01 \x01(\tB\x02\x18\x01\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\"\x85\x01\n\x17SubscribeTradesResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12U\n\x13trade_subscriptions\x18\x02 \x03(\x0b\x32\x38.tinkoff.public.invest.api.contract.v1.TradeSubscription\"\xbd\x01\n\x11TradeSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12V\n\x13subscription_status\x18\x02 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\x12\x16\n\x0einstrument_uid\x18\x03 \x01(\t\x12\x11\n\tstream_id\x18\x04 \x01(\t\x12\x17\n\x0fsubscription_id\x18\x05 \x01(\t\"\xba\x01\n\x14SubscribeInfoRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12J\n\x0binstruments\x18\x02 \x03(\x0b\x32\x35.tinkoff.public.invest.api.contract.v1.InfoInstrument\"9\n\x0eInfoInstrument\x12\x10\n\x04\x66igi\x18\x01 \x01(\tB\x02\x18\x01\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\"\x81\x01\n\x15SubscribeInfoResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12S\n\x12info_subscriptions\x18\x02 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.InfoSubscription\"\xbc\x01\n\x10InfoSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12V\n\x13subscription_status\x18\x02 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\x12\x16\n\x0einstrument_uid\x18\x03 \x01(\t\x12\x11\n\tstream_id\x18\x04 \x01(\t\x12\x17\n\x0fsubscription_id\x18\x05 \x01(\t\"\xc4\x01\n\x19SubscribeLastPriceRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12O\n\x0binstruments\x18\x02 \x03(\x0b\x32:.tinkoff.public.invest.api.contract.v1.LastPriceInstrument\">\n\x13LastPriceInstrument\x12\x10\n\x04\x66igi\x18\x01 \x01(\tB\x02\x18\x01\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\"\x91\x01\n\x1aSubscribeLastPriceResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12^\n\x18last_price_subscriptions\x18\x02 \x03(\x0b\x32<.tinkoff.public.invest.api.contract.v1.LastPriceSubscription\"\xc1\x01\n\x15LastPriceSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12V\n\x13subscription_status\x18\x02 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\x12\x16\n\x0einstrument_uid\x18\x03 \x01(\t\x12\x11\n\tstream_id\x18\x04 \x01(\t\x12\x17\n\x0fsubscription_id\x18\x05 \x01(\t\"\xea\x03\n\x06\x43\x61ndle\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12M\n\x08interval\x18\x02 \x01(\x0e\x32;.tinkoff.public.invest.api.contract.v1.SubscriptionInterval\x12>\n\x04open\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12>\n\x04high\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12=\n\x03low\x18\x05 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12?\n\x05\x63lose\x18\x06 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x0e\n\x06volume\x18\x07 \x01(\x03\x12(\n\x04time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rlast_trade_ts\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einstrument_uid\x18\n \x01(\t\"\xd2\x03\n\tOrderBook\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12\x15\n\ris_consistent\x18\x03 \x01(\x08\x12:\n\x04\x62ids\x18\x04 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12:\n\x04\x61sks\x18\x05 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12(\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x08limit_up\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x44\n\nlimit_down\x18\x08 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x16\n\x0einstrument_uid\x18\t \x01(\t\x12M\n\x0forder_book_type\x18\n \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.OrderBookType\"Z\n\x05Order\x12?\n\x05price\x18\x01 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08quantity\x18\x02 \x01(\x03\"\xf4\x01\n\x05Trade\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12H\n\tdirection\x18\x02 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.TradeDirection\x12?\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08quantity\x18\x04 \x01(\x03\x12(\n\x04time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einstrument_uid\x18\x06 \x01(\t\"\xfe\x01\n\rTradingStatus\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12T\n\x0etrading_status\x18\x02 \x01(\x0e\x32<.tinkoff.public.invest.api.contract.v1.SecurityTradingStatus\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x1alimit_order_available_flag\x18\x04 \x01(\x08\x12#\n\x1bmarket_order_available_flag\x18\x05 \x01(\x08\x12\x16\n\x0einstrument_uid\x18\x06 \x01(\t\"\x8e\x02\n\x11GetCandlesRequest\x12\x15\n\x04\x66igi\x18\x01 \x01(\tB\x02\x18\x01H\x00\x88\x01\x01\x12.\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02\x12,\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02\x12M\n\x08interval\x18\x04 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.CandleIntervalB\x04\xe2\x41\x01\x02\x12\x1a\n\rinstrument_id\x18\x05 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_figiB\x10\n\x0e_instrument_id\"\\\n\x12GetCandlesResponse\x12\x46\n\x07\x63\x61ndles\x18\x01 \x03(\x0b\x32\x35.tinkoff.public.invest.api.contract.v1.HistoricCandle\"\xdf\x02\n\x0eHistoricCandle\x12>\n\x04open\x18\x01 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12>\n\x04high\x18\x02 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12=\n\x03low\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12?\n\x05\x63lose\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x0e\n\x06volume\x18\x05 \x01(\x03\x12(\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bis_complete\x18\x07 \x01(\x08\"?\n\x14GetLastPricesRequest\x12\x10\n\x04\x66igi\x18\x01 \x03(\tB\x02\x18\x01\x12\x15\n\rinstrument_id\x18\x02 \x03(\t\"^\n\x15GetLastPricesResponse\x12\x45\n\x0blast_prices\x18\x01 \x03(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.LastPrice\"\x9c\x01\n\tLastPrice\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12?\n\x05price\x18\x02 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einstrument_uid\x18\x0b \x01(\t\"x\n\x13GetOrderBookRequest\x12\x15\n\x04\x66igi\x18\x01 \x01(\tB\x02\x18\x01H\x00\x88\x01\x01\x12\x13\n\x05\x64\x65pth\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x02\x12\x1a\n\rinstrument_id\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_figiB\x10\n\x0e_instrument_id\"\xf3\x04\n\x14GetOrderBookResponse\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12:\n\x04\x62ids\x18\x03 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12:\n\x04\x61sks\x18\x04 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12\x44\n\nlast_price\x18\x05 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x45\n\x0b\x63lose_price\x18\x06 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x42\n\x08limit_up\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x44\n\nlimit_down\x18\x08 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x31\n\rlast_price_ts\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0e\x63lose_price_ts\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0corderbook_ts\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einstrument_uid\x18\t \x01(\t\"g\n\x17GetTradingStatusRequest\x12\x15\n\x04\x66igi\x18\x01 \x01(\tB\x02\x18\x01H\x00\x88\x01\x01\x12\x1a\n\rinstrument_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_figiB\x10\n\x0e_instrument_id\"2\n\x19GetTradingStatusesRequest\x12\x15\n\rinstrument_id\x18\x01 \x03(\t\"w\n\x1aGetTradingStatusesResponse\x12Y\n\x10trading_statuses\x18\x01 \x03(\x0b\x32?.tinkoff.public.invest.api.contract.v1.GetTradingStatusResponse\"\xc2\x02\n\x18GetTradingStatusResponse\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12T\n\x0etrading_status\x18\x02 \x01(\x0e\x32<.tinkoff.public.invest.api.contract.v1.SecurityTradingStatus\x12\"\n\x1alimit_order_available_flag\x18\x03 \x01(\x08\x12#\n\x1bmarket_order_available_flag\x18\x04 \x01(\x08\x12 \n\x18\x61pi_trade_available_flag\x18\x05 \x01(\x08\x12\x16\n\x0einstrument_uid\x18\x06 \x01(\t\x12&\n\x1e\x62\x65stprice_order_available_flag\x18\x08 \x01(\x08\x12\x17\n\x0fonly_best_price\x18\t \x01(\x08\"\xc2\x01\n\x14GetLastTradesRequest\x12\x15\n\x04\x66igi\x18\x01 \x01(\tB\x02\x18\x01H\x00\x88\x01\x01\x12.\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02\x12,\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02\x12\x1a\n\rinstrument_id\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_figiB\x10\n\x0e_instrument_id\"U\n\x15GetLastTradesResponse\x12<\n\x06trades\x18\x01 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Trade\"\x14\n\x12GetMySubscriptions\"v\n\x15GetClosePricesRequest\x12]\n\x0binstruments\x18\x01 \x03(\x0b\x32\x42.tinkoff.public.invest.api.contract.v1.InstrumentClosePriceRequestB\x04\xe2\x41\x01\x02\"4\n\x1bInstrumentClosePriceRequest\x12\x15\n\rinstrument_id\x18\x01 \x01(\t\"s\n\x16GetClosePricesResponse\x12Y\n\x0c\x63lose_prices\x18\x01 \x03(\x0b\x32\x43.tinkoff.public.invest.api.contract.v1.InstrumentClosePriceResponse\"\x80\x02\n\x1cInstrumentClosePriceResponse\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x02 \x01(\t\x12?\n\x05price\x18\x0b \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12O\n\x15\x65vening_session_price\x18\x0c \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12(\n\x04time\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xf4\x0c\n\x16GetTechAnalysisRequest\x12i\n\x0eindicator_type\x18\x01 \x01(\x0e\x32K.tinkoff.public.invest.api.contract.v1.GetTechAnalysisRequest.IndicatorTypeB\x04\xe2\x41\x01\x02\x12\x1c\n\x0einstrument_uid\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02\x12.\n\x04\x66rom\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02\x12,\n\x02to\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02\x12g\n\x08interval\x18\x05 \x01(\x0e\x32O.tinkoff.public.invest.api.contract.v1.GetTechAnalysisRequest.IndicatorIntervalB\x04\xe2\x41\x01\x02\x12\x66\n\rtype_of_price\x18\x06 \x01(\x0e\x32I.tinkoff.public.invest.api.contract.v1.GetTechAnalysisRequest.TypeOfPriceB\x04\xe2\x41\x01\x02\x12\x0e\n\x06length\x18\x07 \x01(\x05\x12Z\n\tdeviation\x18\x08 \x01(\x0b\x32G.tinkoff.public.invest.api.contract.v1.GetTechAnalysisRequest.Deviation\x12Z\n\tsmoothing\x18\t \x01(\x0b\x32G.tinkoff.public.invest.api.contract.v1.GetTechAnalysisRequest.Smoothing\x1aO\n\tSmoothing\x12\x13\n\x0b\x66\x61st_length\x18\x01 \x01(\x05\x12\x13\n\x0bslow_length\x18\x02 \x01(\x05\x12\x18\n\x10signal_smoothing\x18\x03 \x01(\x05\x1a[\n\tDeviation\x12N\n\x14\x64\x65viation_multiplier\x18\x01 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\"\xdb\x03\n\x11IndicatorInterval\x12\"\n\x1eINDICATOR_INTERVAL_UNSPECIFIED\x10\x00\x12!\n\x1dINDICATOR_INTERVAL_ONE_MINUTE\x10\x01\x12#\n\x1fINDICATOR_INTERVAL_FIVE_MINUTES\x10\x02\x12&\n\"INDICATOR_INTERVAL_FIFTEEN_MINUTES\x10\x03\x12\x1f\n\x1bINDICATOR_INTERVAL_ONE_HOUR\x10\x04\x12\x1e\n\x1aINDICATOR_INTERVAL_ONE_DAY\x10\x05\x12\x1c\n\x18INDICATOR_INTERVAL_2_MIN\x10\x06\x12\x1c\n\x18INDICATOR_INTERVAL_3_MIN\x10\x07\x12\x1d\n\x19INDICATOR_INTERVAL_10_MIN\x10\x08\x12\x1d\n\x19INDICATOR_INTERVAL_30_MIN\x10\t\x12\x1d\n\x19INDICATOR_INTERVAL_2_HOUR\x10\n\x12\x1d\n\x19INDICATOR_INTERVAL_4_HOUR\x10\x0b\x12\x1b\n\x17INDICATOR_INTERVAL_WEEK\x10\x0c\x12\x1c\n\x18INDICATOR_INTERVAL_MONTH\x10\r\"\xa3\x01\n\x0bTypeOfPrice\x12\x1d\n\x19TYPE_OF_PRICE_UNSPECIFIED\x10\x00\x12\x17\n\x13TYPE_OF_PRICE_CLOSE\x10\x01\x12\x16\n\x12TYPE_OF_PRICE_OPEN\x10\x02\x12\x16\n\x12TYPE_OF_PRICE_HIGH\x10\x03\x12\x15\n\x11TYPE_OF_PRICE_LOW\x10\x04\x12\x15\n\x11TYPE_OF_PRICE_AVG\x10\x05\"\xa7\x01\n\rIndicatorType\x12\x1e\n\x1aINDICATOR_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11INDICATOR_TYPE_BB\x10\x01\x12\x16\n\x12INDICATOR_TYPE_EMA\x10\x02\x12\x16\n\x12INDICATOR_TYPE_RSI\x10\x03\x12\x17\n\x13INDICATOR_TYPE_MACD\x10\x04\x12\x16\n\x12INDICATOR_TYPE_SMA\x10\x05\"\xfc\x04\n\x17GetTechAnalysisResponse\x12m\n\x14technical_indicators\x18\x01 \x03(\x0b\x32O.tinkoff.public.invest.api.contract.v1.GetTechAnalysisResponse.TechAnalysisItem\x1a\xf1\x03\n\x10TechAnalysisItem\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12J\n\x0bmiddle_band\x18\x02 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x00\x88\x01\x01\x12I\n\nupper_band\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x01\x88\x01\x01\x12I\n\nlower_band\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x02\x88\x01\x01\x12\x45\n\x06signal\x18\x05 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x03\x88\x01\x01\x12\x43\n\x04macd\x18\x06 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x04\x88\x01\x01\x42\x0e\n\x0c_middle_bandB\r\n\x0b_upper_bandB\r\n\x0b_lower_bandB\t\n\x07_signalB\x07\n\x05_macd*\x81\x01\n\x12SubscriptionAction\x12#\n\x1fSUBSCRIPTION_ACTION_UNSPECIFIED\x10\x00\x12!\n\x1dSUBSCRIPTION_ACTION_SUBSCRIBE\x10\x01\x12#\n\x1fSUBSCRIPTION_ACTION_UNSUBSCRIBE\x10\x02*\x88\x04\n\x14SubscriptionInterval\x12%\n!SUBSCRIPTION_INTERVAL_UNSPECIFIED\x10\x00\x12$\n SUBSCRIPTION_INTERVAL_ONE_MINUTE\x10\x01\x12&\n\"SUBSCRIPTION_INTERVAL_FIVE_MINUTES\x10\x02\x12)\n%SUBSCRIPTION_INTERVAL_FIFTEEN_MINUTES\x10\x03\x12\"\n\x1eSUBSCRIPTION_INTERVAL_ONE_HOUR\x10\x04\x12!\n\x1dSUBSCRIPTION_INTERVAL_ONE_DAY\x10\x05\x12\x1f\n\x1bSUBSCRIPTION_INTERVAL_2_MIN\x10\x06\x12\x1f\n\x1bSUBSCRIPTION_INTERVAL_3_MIN\x10\x07\x12 \n\x1cSUBSCRIPTION_INTERVAL_10_MIN\x10\x08\x12 \n\x1cSUBSCRIPTION_INTERVAL_30_MIN\x10\t\x12 \n\x1cSUBSCRIPTION_INTERVAL_2_HOUR\x10\n\x12 \n\x1cSUBSCRIPTION_INTERVAL_4_HOUR\x10\x0b\x12\x1e\n\x1aSUBSCRIPTION_INTERVAL_WEEK\x10\x0c\x12\x1f\n\x1bSUBSCRIPTION_INTERVAL_MONTH\x10\r*\xc5\x03\n\x12SubscriptionStatus\x12#\n\x1fSUBSCRIPTION_STATUS_UNSPECIFIED\x10\x00\x12\x1f\n\x1bSUBSCRIPTION_STATUS_SUCCESS\x10\x01\x12,\n(SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND\x10\x02\x12\x36\n2SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID\x10\x03\x12(\n$SUBSCRIPTION_STATUS_DEPTH_IS_INVALID\x10\x04\x12+\n\'SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID\x10\x05\x12)\n%SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED\x10\x06\x12&\n\"SUBSCRIPTION_STATUS_INTERNAL_ERROR\x10\x07\x12)\n%SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS\x10\x08\x12.\n*SUBSCRIPTION_STATUS_SUBSCRIPTION_NOT_FOUND\x10\t*d\n\x0eTradeDirection\x12\x1f\n\x1bTRADE_DIRECTION_UNSPECIFIED\x10\x00\x12\x17\n\x13TRADE_DIRECTION_BUY\x10\x01\x12\x18\n\x14TRADE_DIRECTION_SELL\x10\x02*\x91\x03\n\x0e\x43\x61ndleInterval\x12\x1f\n\x1b\x43\x41NDLE_INTERVAL_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43\x41NDLE_INTERVAL_1_MIN\x10\x01\x12\x19\n\x15\x43\x41NDLE_INTERVAL_5_MIN\x10\x02\x12\x1a\n\x16\x43\x41NDLE_INTERVAL_15_MIN\x10\x03\x12\x18\n\x14\x43\x41NDLE_INTERVAL_HOUR\x10\x04\x12\x17\n\x13\x43\x41NDLE_INTERVAL_DAY\x10\x05\x12\x19\n\x15\x43\x41NDLE_INTERVAL_2_MIN\x10\x06\x12\x19\n\x15\x43\x41NDLE_INTERVAL_3_MIN\x10\x07\x12\x1a\n\x16\x43\x41NDLE_INTERVAL_10_MIN\x10\x08\x12\x1a\n\x16\x43\x41NDLE_INTERVAL_30_MIN\x10\t\x12\x1a\n\x16\x43\x41NDLE_INTERVAL_2_HOUR\x10\n\x12\x1a\n\x16\x43\x41NDLE_INTERVAL_4_HOUR\x10\x0b\x12\x18\n\x14\x43\x41NDLE_INTERVAL_WEEK\x10\x0c\x12\x19\n\x15\x43\x41NDLE_INTERVAL_MONTH\x10\r*g\n\rOrderBookType\x12\x1e\n\x1aORDERBOOK_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17ORDERBOOK_TYPE_EXCHANGE\x10\x01\x12\x19\n\x15ORDERBOOK_TYPE_DEALER\x10\x02\x32\x90\t\n\x11MarketDataService\x12\x81\x01\n\nGetCandles\x12\x38.tinkoff.public.invest.api.contract.v1.GetCandlesRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.GetCandlesResponse\x12\x8a\x01\n\rGetLastPrices\x12;.tinkoff.public.invest.api.contract.v1.GetLastPricesRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetLastPricesResponse\x12\x87\x01\n\x0cGetOrderBook\x12:.tinkoff.public.invest.api.contract.v1.GetOrderBookRequest\x1a;.tinkoff.public.invest.api.contract.v1.GetOrderBookResponse\x12\x93\x01\n\x10GetTradingStatus\x12>.tinkoff.public.invest.api.contract.v1.GetTradingStatusRequest\x1a?.tinkoff.public.invest.api.contract.v1.GetTradingStatusResponse\x12\x99\x01\n\x12GetTradingStatuses\x12@.tinkoff.public.invest.api.contract.v1.GetTradingStatusesRequest\x1a\x41.tinkoff.public.invest.api.contract.v1.GetTradingStatusesResponse\x12\x8a\x01\n\rGetLastTrades\x12;.tinkoff.public.invest.api.contract.v1.GetLastTradesRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetLastTradesResponse\x12\x8d\x01\n\x0eGetClosePrices\x12<.tinkoff.public.invest.api.contract.v1.GetClosePricesRequest\x1a=.tinkoff.public.invest.api.contract.v1.GetClosePricesResponse\x12\x90\x01\n\x0fGetTechAnalysis\x12=.tinkoff.public.invest.api.contract.v1.GetTechAnalysisRequest\x1a>.tinkoff.public.invest.api.contract.v1.GetTechAnalysisResponse2\xcd\x02\n\x17MarketDataStreamService\x12\x8b\x01\n\x10MarketDataStream\x12\x38.tinkoff.public.invest.api.contract.v1.MarketDataRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.MarketDataResponse(\x01\x30\x01\x12\xa3\x01\n\x1aMarketDataServerSideStream\x12H.tinkoff.public.invest.api.contract.v1.MarketDataServerSideStreamRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.MarketDataResponse0\x01\x42\x61\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tinkoff.invest.grpc.marketdata_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _CANDLEINSTRUMENT.fields_by_name['figi']._options = None
  _CANDLEINSTRUMENT.fields_by_name['figi']._serialized_options = b'\030\001'
  _ORDERBOOKINSTRUMENT.fields_by_name['figi']._options = None
  _ORDERBOOKINSTRUMENT.fields_by_name['figi']._serialized_options = b'\030\001'
  _TRADEINSTRUMENT.fields_by_name['figi']._options = None
  _TRADEINSTRUMENT.fields_by_name['figi']._serialized_options = b'\030\001'
  _INFOINSTRUMENT.fields_by_name['figi']._options = None
  _INFOINSTRUMENT.fields_by_name['figi']._serialized_options = b'\030\001'
  _LASTPRICEINSTRUMENT.fields_by_name['figi']._options = None
  _LASTPRICEINSTRUMENT.fields_by_name['figi']._serialized_options = b'\030\001'
  _GETCANDLESREQUEST.fields_by_name['figi']._options = None
  _GETCANDLESREQUEST.fields_by_name['figi']._serialized_options = b'\030\001'
  _GETCANDLESREQUEST.fields_by_name['from']._options = None
  _GETCANDLESREQUEST.fields_by_name['from']._serialized_options = b'\342A\001\002'
  _GETCANDLESREQUEST.fields_by_name['to']._options = None
  _GETCANDLESREQUEST.fields_by_name['to']._serialized_options = b'\342A\001\002'
  _GETCANDLESREQUEST.fields_by_name['interval']._options = None
  _GETCANDLESREQUEST.fields_by_name['interval']._serialized_options = b'\342A\001\002'
  _GETLASTPRICESREQUEST.fields_by_name['figi']._options = None
  _GETLASTPRICESREQUEST.fields_by_name['figi']._serialized_options = b'\030\001'
  _GETORDERBOOKREQUEST.fields_by_name['figi']._options = None
  _GETORDERBOOKREQUEST.fields_by_name['figi']._serialized_options = b'\030\001'
  _GETORDERBOOKREQUEST.fields_by_name['depth']._options = None
  _GETORDERBOOKREQUEST.fields_by_name['depth']._serialized_options = b'\342A\001\002'
  _GETTRADINGSTATUSREQUEST.fields_by_name['figi']._options = None
  _GETTRADINGSTATUSREQUEST.fields_by_name['figi']._serialized_options = b'\030\001'
  _GETLASTTRADESREQUEST.fields_by_name['figi']._options = None
  _GETLASTTRADESREQUEST.fields_by_name['figi']._serialized_options = b'\030\001'
  _GETLASTTRADESREQUEST.fields_by_name['from']._options = None
  _GETLASTTRADESREQUEST.fields_by_name['from']._serialized_options = b'\342A\001\002'
  _GETLASTTRADESREQUEST.fields_by_name['to']._options = None
  _GETLASTTRADESREQUEST.fields_by_name['to']._serialized_options = b'\342A\001\002'
  _GETCLOSEPRICESREQUEST.fields_by_name['instruments']._options = None
  _GETCLOSEPRICESREQUEST.fields_by_name['instruments']._serialized_options = b'\342A\001\002'
  _GETTECHANALYSISREQUEST.fields_by_name['indicator_type']._options = None
  _GETTECHANALYSISREQUEST.fields_by_name['indicator_type']._serialized_options = b'\342A\001\002'
  _GETTECHANALYSISREQUEST.fields_by_name['instrument_uid']._options = None
  _GETTECHANALYSISREQUEST.fields_by_name['instrument_uid']._serialized_options = b'\342A\001\002'
  _GETTECHANALYSISREQUEST.fields_by_name['from']._options = None
  _GETTECHANALYSISREQUEST.fields_by_name['from']._serialized_options = b'\342A\001\002'
  _GETTECHANALYSISREQUEST.fields_by_name['to']._options = None
  _GETTECHANALYSISREQUEST.fields_by_name['to']._serialized_options = b'\342A\001\002'
  _GETTECHANALYSISREQUEST.fields_by_name['interval']._options = None
  _GETTECHANALYSISREQUEST.fields_by_name['interval']._serialized_options = b'\342A\001\002'
  _GETTECHANALYSISREQUEST.fields_by_name['type_of_price']._options = None
  _GETTECHANALYSISREQUEST.fields_by_name['type_of_price']._serialized_options = b'\342A\001\002'
  _globals['_SUBSCRIPTIONACTION']._serialized_start=12780
  _globals['_SUBSCRIPTIONACTION']._serialized_end=12909
  _globals['_SUBSCRIPTIONINTERVAL']._serialized_start=12912
  _globals['_SUBSCRIPTIONINTERVAL']._serialized_end=13432
  _globals['_SUBSCRIPTIONSTATUS']._serialized_start=13435
  _globals['_SUBSCRIPTIONSTATUS']._serialized_end=13888
  _globals['_TRADEDIRECTION']._serialized_start=13890
  _globals['_TRADEDIRECTION']._serialized_end=13990
  _globals['_CANDLEINTERVAL']._serialized_start=13993
  _globals['_CANDLEINTERVAL']._serialized_end=14394
  _globals['_ORDERBOOKTYPE']._serialized_start=14396
  _globals['_ORDERBOOKTYPE']._serialized_end=14499
  _globals['_MARKETDATAREQUEST']._serialized_start=200
  _globals['_MARKETDATAREQUEST']._serialized_end=828
  _globals['_MARKETDATASERVERSIDESTREAMREQUEST']._serialized_start=831
  _globals['_MARKETDATASERVERSIDESTREAMREQUEST']._serialized_end=1363
  _globals['_MARKETDATARESPONSE']._serialized_start=1366
  _globals['_MARKETDATARESPONSE']._serialized_end=2326
  _globals['_SUBSCRIBECANDLESREQUEST']._serialized_start=2329
  _globals['_SUBSCRIBECANDLESREQUEST']._serialized_end=2543
  _globals['_CANDLEINSTRUMENT']._serialized_start=2546
  _globals['_CANDLEINSTRUMENT']._serialized_end=2684
  _globals['_SUBSCRIBECANDLESRESPONSE']._serialized_start=2687
  _globals['_SUBSCRIBECANDLESRESPONSE']._serialized_end=2824
  _globals['_CANDLESUBSCRIPTION']._serialized_start=2827
  _globals['_CANDLESUBSCRIPTION']._serialized_end=3119
  _globals['_SUBSCRIBEORDERBOOKREQUEST']._serialized_start=3122
  _globals['_SUBSCRIBEORDERBOOKREQUEST']._serialized_end=3318
  _globals['_ORDERBOOKINSTRUMENT']._serialized_start=3321
  _globals['_ORDERBOOKINSTRUMENT']._serialized_end=3477
  _globals['_SUBSCRIBEORDERBOOKRESPONSE']._serialized_start=3480
  _globals['_SUBSCRIBEORDERBOOKRESPONSE']._serialized_end=3625
  _globals['_ORDERBOOKSUBSCRIPTION']._serialized_start=3628
  _globals['_ORDERBOOKSUBSCRIPTION']._serialized_end=3915
  _globals['_SUBSCRIBETRADESREQUEST']._serialized_start=3918
  _globals['_SUBSCRIBETRADESREQUEST']._serialized_end=4107
  _globals['_TRADEINSTRUMENT']._serialized_start=4109
  _globals['_TRADEINSTRUMENT']._serialized_end=4167
  _globals['_SUBSCRIBETRADESRESPONSE']._serialized_start=4170
  _globals['_SUBSCRIBETRADESRESPONSE']._serialized_end=4303
  _globals['_TRADESUBSCRIPTION']._serialized_start=4306
  _globals['_TRADESUBSCRIPTION']._serialized_end=4495
  _globals['_SUBSCRIBEINFOREQUEST']._serialized_start=4498
  _globals['_SUBSCRIBEINFOREQUEST']._serialized_end=4684
  _globals['_INFOINSTRUMENT']._serialized_start=4686
  _globals['_INFOINSTRUMENT']._serialized_end=4743
  _globals['_SUBSCRIBEINFORESPONSE']._serialized_start=4746
  _globals['_SUBSCRIBEINFORESPONSE']._serialized_end=4875
  _globals['_INFOSUBSCRIPTION']._serialized_start=4878
  _globals['_INFOSUBSCRIPTION']._serialized_end=5066
  _globals['_SUBSCRIBELASTPRICEREQUEST']._serialized_start=5069
  _globals['_SUBSCRIBELASTPRICEREQUEST']._serialized_end=5265
  _globals['_LASTPRICEINSTRUMENT']._serialized_start=5267
  _globals['_LASTPRICEINSTRUMENT']._serialized_end=5329
  _globals['_SUBSCRIBELASTPRICERESPONSE']._serialized_start=5332
  _globals['_SUBSCRIBELASTPRICERESPONSE']._serialized_end=5477
  _globals['_LASTPRICESUBSCRIPTION']._serialized_start=5480
  _globals['_LASTPRICESUBSCRIPTION']._serialized_end=5673
  _globals['_CANDLE']._serialized_start=5676
  _globals['_CANDLE']._serialized_end=6166
  _globals['_ORDERBOOK']._serialized_start=6169
  _globals['_ORDERBOOK']._serialized_end=6635
  _globals['_ORDER']._serialized_start=6637
  _globals['_ORDER']._serialized_end=6727
  _globals['_TRADE']._serialized_start=6730
  _globals['_TRADE']._serialized_end=6974
  _globals['_TRADINGSTATUS']._serialized_start=6977
  _globals['_TRADINGSTATUS']._serialized_end=7231
  _globals['_GETCANDLESREQUEST']._serialized_start=7234
  _globals['_GETCANDLESREQUEST']._serialized_end=7504
  _globals['_GETCANDLESRESPONSE']._serialized_start=7506
  _globals['_GETCANDLESRESPONSE']._serialized_end=7598
  _globals['_HISTORICCANDLE']._serialized_start=7601
  _globals['_HISTORICCANDLE']._serialized_end=7952
  _globals['_GETLASTPRICESREQUEST']._serialized_start=7954
  _globals['_GETLASTPRICESREQUEST']._serialized_end=8017
  _globals['_GETLASTPRICESRESPONSE']._serialized_start=8019
  _globals['_GETLASTPRICESRESPONSE']._serialized_end=8113
  _globals['_LASTPRICE']._serialized_start=8116
  _globals['_LASTPRICE']._serialized_end=8272
  _globals['_GETORDERBOOKREQUEST']._serialized_start=8274
  _globals['_GETORDERBOOKREQUEST']._serialized_end=8394
  _globals['_GETORDERBOOKRESPONSE']._serialized_start=8397
  _globals['_GETORDERBOOKRESPONSE']._serialized_end=9024
  _globals['_GETTRADINGSTATUSREQUEST']._serialized_start=9026
  _globals['_GETTRADINGSTATUSREQUEST']._serialized_end=9129
  _globals['_GETTRADINGSTATUSESREQUEST']._serialized_start=9131
  _globals['_GETTRADINGSTATUSESREQUEST']._serialized_end=9181
  _globals['_GETTRADINGSTATUSESRESPONSE']._serialized_start=9183
  _globals['_GETTRADINGSTATUSESRESPONSE']._serialized_end=9302
  _globals['_GETTRADINGSTATUSRESPONSE']._serialized_start=9305
  _globals['_GETTRADINGSTATUSRESPONSE']._serialized_end=9627
  _globals['_GETLASTTRADESREQUEST']._serialized_start=9630
  _globals['_GETLASTTRADESREQUEST']._serialized_end=9824
  _globals['_GETLASTTRADESRESPONSE']._serialized_start=9826
  _globals['_GETLASTTRADESRESPONSE']._serialized_end=9911
  _globals['_GETMYSUBSCRIPTIONS']._serialized_start=9913
  _globals['_GETMYSUBSCRIPTIONS']._serialized_end=9933
  _globals['_GETCLOSEPRICESREQUEST']._serialized_start=9935
  _globals['_GETCLOSEPRICESREQUEST']._serialized_end=10053
  _globals['_INSTRUMENTCLOSEPRICEREQUEST']._serialized_start=10055
  _globals['_INSTRUMENTCLOSEPRICEREQUEST']._serialized_end=10107
  _globals['_GETCLOSEPRICESRESPONSE']._serialized_start=10109
  _globals['_GETCLOSEPRICESRESPONSE']._serialized_end=10224
  _globals['_INSTRUMENTCLOSEPRICERESPONSE']._serialized_start=10227
  _globals['_INSTRUMENTCLOSEPRICERESPONSE']._serialized_end=10483
  _globals['_GETTECHANALYSISREQUEST']._serialized_start=10486
  _globals['_GETTECHANALYSISREQUEST']._serialized_end=12138
  _globals['_GETTECHANALYSISREQUEST_SMOOTHING']._serialized_start=11152
  _globals['_GETTECHANALYSISREQUEST_SMOOTHING']._serialized_end=11231
  _globals['_GETTECHANALYSISREQUEST_DEVIATION']._serialized_start=11233
  _globals['_GETTECHANALYSISREQUEST_DEVIATION']._serialized_end=11324
  _globals['_GETTECHANALYSISREQUEST_INDICATORINTERVAL']._serialized_start=11327
  _globals['_GETTECHANALYSISREQUEST_INDICATORINTERVAL']._serialized_end=11802
  _globals['_GETTECHANALYSISREQUEST_TYPEOFPRICE']._serialized_start=11805
  _globals['_GETTECHANALYSISREQUEST_TYPEOFPRICE']._serialized_end=11968
  _globals['_GETTECHANALYSISREQUEST_INDICATORTYPE']._serialized_start=11971
  _globals['_GETTECHANALYSISREQUEST_INDICATORTYPE']._serialized_end=12138
  _globals['_GETTECHANALYSISRESPONSE']._serialized_start=12141
  _globals['_GETTECHANALYSISRESPONSE']._serialized_end=12777
  _globals['_GETTECHANALYSISRESPONSE_TECHANALYSISITEM']._serialized_start=12280
  _globals['_GETTECHANALYSISRESPONSE_TECHANALYSISITEM']._serialized_end=12777
  _globals['_MARKETDATASERVICE']._serialized_start=14502
  _globals['_MARKETDATASERVICE']._serialized_end=15670
  _globals['_MARKETDATASTREAMSERVICE']._serialized_start=15673
  _globals['_MARKETDATASTREAMSERVICE']._serialized_end=16006
# @@protoc_insertion_point(module_scope)
