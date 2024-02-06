# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinkoff/invest/grpc/orders.proto
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

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n tinkoff/invest/grpc/orders.proto\x12%tinkoff.public.invest.api.contract.v1\x1a tinkoff/invest/grpc/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x33tinkoff/invest/grpc/google/api/field_behavior.proto\"\'\n\x13TradesStreamRequest\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\"\xaa\x01\n\x14TradesStreamResponse\x12J\n\x0corder_trades\x18\x01 \x01(\x0b\x32\x32.tinkoff.public.invest.api.contract.v1.OrderTradesH\x00\x12;\n\x04ping\x18\x02 \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x42\t\n\x07payload\"\x96\x02\n\x0bOrderTrades\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n\tdirection\x18\x03 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12\x0c\n\x04\x66igi\x18\x04 \x01(\t\x12\x41\n\x06trades\x18\x05 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderTrade\x12\x12\n\naccount_id\x18\x06 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x07 \x01(\t\"\xa0\x01\n\nOrderTrade\x12-\n\tdate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12?\n\x05price\x18\x02 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08quantity\x18\x03 \x01(\x03\x12\x10\n\x08trade_id\x18\x04 \x01(\t\"\x8f\x04\n\x10PostOrderRequest\x12\x15\n\x04\x66igi\x18\x01 \x01(\tB\x02\x18\x01H\x00\x88\x01\x01\x12\x15\n\x08quantity\x18\x02 \x01(\x03\x42\x03\xe0\x41\x02\x12\x44\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x01\x88\x01\x01\x12M\n\tdirection\x18\x04 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirectionB\x03\xe0\x41\x02\x12\x17\n\naccount_id\x18\x05 \x01(\tB\x03\xe0\x41\x02\x12I\n\norder_type\x18\x06 \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderTypeB\x03\xe0\x41\x02\x12\x15\n\x08order_id\x18\x07 \x01(\tB\x03\xe0\x41\x02\x12\x15\n\rinstrument_id\x18\x08 \x01(\t\x12M\n\rtime_in_force\x18\t \x01(\x0e\x32\x36.tinkoff.public.invest.api.contract.v1.TimeInForceType\x12\x44\n\nprice_type\x18\n \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.PriceTypeB\x07\n\x05_figiB\x08\n\x06_price\"\x93\x08\n\x11PostOrderResponse\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x62\n\x17\x65xecution_report_status\x18\x02 \x01(\x0e\x32\x41.tinkoff.public.invest.api.contract.v1.OrderExecutionReportStatus\x12\x16\n\x0elots_requested\x18\x03 \x01(\x03\x12\x15\n\rlots_executed\x18\x04 \x01(\x03\x12N\n\x13initial_order_price\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14\x65xecuted_order_price\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12total_order_amount\x18\x07 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12initial_commission\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\x13\x65xecuted_commission\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x44\n\taci_value\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x0c\n\x04\x66igi\x18\x0b \x01(\t\x12H\n\tdirection\x18\x0c \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12Q\n\x16initial_security_price\x18\r \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x44\n\norder_type\x18\x0e \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderType\x12\x0f\n\x07message\x18\x0f \x01(\t\x12P\n\x16initial_order_price_pt\x18\x10 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x16\n\x0einstrument_uid\x18\x11 \x01(\t\x12\x18\n\x10order_request_id\x18\x14 \x01(\t\"D\n\x12\x43\x61ncelOrderRequest\x12\x17\n\naccount_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x15\n\x08order_id\x18\x02 \x01(\tB\x03\xe0\x41\x02\"?\n\x13\x43\x61ncelOrderResponse\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x8c\x01\n\x14GetOrderStateRequest\x12\x17\n\naccount_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x15\n\x08order_id\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12\x44\n\nprice_type\x18\x03 \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.PriceType\"+\n\x10GetOrdersRequest\x12\x17\n\naccount_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\"V\n\x11GetOrdersResponse\x12\x41\n\x06orders\x18\x01 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderState\"\x8a\t\n\nOrderState\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x62\n\x17\x65xecution_report_status\x18\x02 \x01(\x0e\x32\x41.tinkoff.public.invest.api.contract.v1.OrderExecutionReportStatus\x12\x16\n\x0elots_requested\x18\x03 \x01(\x03\x12\x15\n\rlots_executed\x18\x04 \x01(\x03\x12N\n\x13initial_order_price\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14\x65xecuted_order_price\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12total_order_amount\x18\x07 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Q\n\x16\x61verage_position_price\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12initial_commission\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\x13\x65xecuted_commission\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x0c\n\x04\x66igi\x18\x0b \x01(\t\x12H\n\tdirection\x18\x0c \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12Q\n\x16initial_security_price\x18\r \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x41\n\x06stages\x18\x0e \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderStage\x12M\n\x12service_commission\x18\x0f \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08\x63urrency\x18\x10 \x01(\t\x12\x44\n\norder_type\x18\x11 \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderType\x12.\n\norder_date\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einstrument_uid\x18\x13 \x01(\t\x12\x18\n\x10order_request_id\x18\x14 \x01(\t\"r\n\nOrderStage\x12@\n\x05price\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08quantity\x18\x02 \x01(\x03\x12\x10\n\x08trade_id\x18\x03 \x01(\t\"\xa4\x02\n\x13ReplaceOrderRequest\x12\x17\n\naccount_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x15\n\x08order_id\x18\x06 \x01(\tB\x03\xe0\x41\x02\x12\x1c\n\x0fidempotency_key\x18\x07 \x01(\tB\x03\xe0\x41\x02\x12\x15\n\x08quantity\x18\x0b \x01(\x03\x42\x03\xe0\x41\x02\x12\x44\n\x05price\x18\x0c \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x00\x88\x01\x01\x12I\n\nprice_type\x18\r \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.PriceTypeH\x01\x88\x01\x01\x42\x08\n\x06_priceB\r\n\x0b_price_type\"\x98\x01\n\x11GetMaxLotsRequest\x12\x17\n\naccount_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x1a\n\rinstrument_id\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12\x44\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x00\x88\x01\x01\x42\x08\n\x06_price\"\xe6\x04\n\x12GetMaxLotsResponse\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12[\n\nbuy_limits\x18\x02 \x01(\x0b\x32G.tinkoff.public.invest.api.contract.v1.GetMaxLotsResponse.BuyLimitsView\x12\x62\n\x11\x62uy_margin_limits\x18\x03 \x01(\x0b\x32G.tinkoff.public.invest.api.contract.v1.GetMaxLotsResponse.BuyLimitsView\x12]\n\x0bsell_limits\x18\x04 \x01(\x0b\x32H.tinkoff.public.invest.api.contract.v1.GetMaxLotsResponse.SellLimitsView\x12\x64\n\x12sell_margin_limits\x18\x05 \x01(\x0b\x32H.tinkoff.public.invest.api.contract.v1.GetMaxLotsResponse.SellLimitsView\x1a\x8e\x01\n\rBuyLimitsView\x12J\n\x10\x62uy_money_amount\x18\x01 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x14\n\x0c\x62uy_max_lots\x18\x02 \x01(\x03\x12\x1b\n\x13\x62uy_max_market_lots\x18\x03 \x01(\x03\x1a\'\n\x0eSellLimitsView\x12\x15\n\rsell_max_lots\x18\x01 \x01(\x03\"\xde\x01\n\x14GetOrderPriceRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\x12?\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12H\n\tdirection\x18\x0c \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12\x10\n\x08quantity\x18\r \x01(\x03\"\xe3\x07\n\x15GetOrderPriceResponse\x12M\n\x12total_order_amount\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14initial_order_amount\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x16\n\x0elots_requested\x18\x03 \x01(\x03\x12N\n\x13\x65xecuted_commission\x18\x07 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12R\n\x17\x65xecuted_commission_rub\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12service_commission\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12J\n\x0f\x64\x65\x61l_commission\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\\\n\nextra_bond\x18\x0c \x01(\x0b\x32\x46.tinkoff.public.invest.api.contract.v1.GetOrderPriceResponse.ExtraBondH\x00\x12`\n\x0c\x65xtra_future\x18\r \x01(\x0b\x32H.tinkoff.public.invest.api.contract.v1.GetOrderPriceResponse.ExtraFutureH\x00\x1a\xa4\x01\n\tExtraBond\x12\x44\n\taci_value\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Q\n\x17nominal_conversion_rate\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x1aX\n\x0b\x45xtraFuture\x12I\n\x0einitial_margin\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValueB\x12\n\x10instrument_extra*d\n\x0eOrderDirection\x12\x1f\n\x1bORDER_DIRECTION_UNSPECIFIED\x10\x00\x12\x17\n\x13ORDER_DIRECTION_BUY\x10\x01\x12\x18\n\x14ORDER_DIRECTION_SELL\x10\x02*n\n\tOrderType\x12\x1a\n\x16ORDER_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10ORDER_TYPE_LIMIT\x10\x01\x12\x15\n\x11ORDER_TYPE_MARKET\x10\x02\x12\x18\n\x14ORDER_TYPE_BESTPRICE\x10\x03*\x80\x02\n\x1aOrderExecutionReportStatus\x12\'\n#EXECUTION_REPORT_STATUS_UNSPECIFIED\x10\x00\x12 \n\x1c\x45XECUTION_REPORT_STATUS_FILL\x10\x01\x12$\n EXECUTION_REPORT_STATUS_REJECTED\x10\x02\x12%\n!EXECUTION_REPORT_STATUS_CANCELLED\x10\x03\x12\x1f\n\x1b\x45XECUTION_REPORT_STATUS_NEW\x10\x04\x12)\n%EXECUTION_REPORT_STATUS_PARTIALLYFILL\x10\x05*\x88\x01\n\x0fTimeInForceType\x12\x1d\n\x19TIME_IN_FORCE_UNSPECIFIED\x10\x00\x12\x15\n\x11TIME_IN_FORCE_DAY\x10\x01\x12\x1f\n\x1bTIME_IN_FORCE_FILL_AND_KILL\x10\x02\x12\x1e\n\x1aTIME_IN_FORCE_FILL_OR_KILL\x10\x03\x32\xa1\x01\n\x13OrdersStreamService\x12\x89\x01\n\x0cTradesStream\x12:.tinkoff.public.invest.api.contract.v1.TradesStreamRequest\x1a;.tinkoff.public.invest.api.contract.v1.TradesStreamResponse0\x01\x32\xaf\x07\n\rOrdersService\x12~\n\tPostOrder\x12\x37.tinkoff.public.invest.api.contract.v1.PostOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponse\x12\x84\x01\n\x0b\x43\x61ncelOrder\x12\x39.tinkoff.public.invest.api.contract.v1.CancelOrderRequest\x1a:.tinkoff.public.invest.api.contract.v1.CancelOrderResponse\x12\x7f\n\rGetOrderState\x12;.tinkoff.public.invest.api.contract.v1.GetOrderStateRequest\x1a\x31.tinkoff.public.invest.api.contract.v1.OrderState\x12~\n\tGetOrders\x12\x37.tinkoff.public.invest.api.contract.v1.GetOrdersRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.GetOrdersResponse\x12\x84\x01\n\x0cReplaceOrder\x12:.tinkoff.public.invest.api.contract.v1.ReplaceOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponse\x12\x81\x01\n\nGetMaxLots\x12\x38.tinkoff.public.invest.api.contract.v1.GetMaxLotsRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.GetMaxLotsResponse\x12\x8a\x01\n\rGetOrderPrice\x12;.tinkoff.public.invest.api.contract.v1.GetOrderPriceRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetOrderPriceResponseBa\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tinkoff.invest.grpc.orders_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _POSTORDERREQUEST.fields_by_name['figi']._options = None
  _POSTORDERREQUEST.fields_by_name['figi']._serialized_options = b'\030\001'
  _POSTORDERREQUEST.fields_by_name['quantity']._options = None
  _POSTORDERREQUEST.fields_by_name['quantity']._serialized_options = b'\340A\002'
  _POSTORDERREQUEST.fields_by_name['direction']._options = None
  _POSTORDERREQUEST.fields_by_name['direction']._serialized_options = b'\340A\002'
  _POSTORDERREQUEST.fields_by_name['account_id']._options = None
  _POSTORDERREQUEST.fields_by_name['account_id']._serialized_options = b'\340A\002'
  _POSTORDERREQUEST.fields_by_name['order_type']._options = None
  _POSTORDERREQUEST.fields_by_name['order_type']._serialized_options = b'\340A\002'
  _POSTORDERREQUEST.fields_by_name['order_id']._options = None
  _POSTORDERREQUEST.fields_by_name['order_id']._serialized_options = b'\340A\002'
  _CANCELORDERREQUEST.fields_by_name['account_id']._options = None
  _CANCELORDERREQUEST.fields_by_name['account_id']._serialized_options = b'\340A\002'
  _CANCELORDERREQUEST.fields_by_name['order_id']._options = None
  _CANCELORDERREQUEST.fields_by_name['order_id']._serialized_options = b'\340A\002'
  _GETORDERSTATEREQUEST.fields_by_name['account_id']._options = None
  _GETORDERSTATEREQUEST.fields_by_name['account_id']._serialized_options = b'\340A\002'
  _GETORDERSTATEREQUEST.fields_by_name['order_id']._options = None
  _GETORDERSTATEREQUEST.fields_by_name['order_id']._serialized_options = b'\340A\002'
  _GETORDERSREQUEST.fields_by_name['account_id']._options = None
  _GETORDERSREQUEST.fields_by_name['account_id']._serialized_options = b'\340A\002'
  _REPLACEORDERREQUEST.fields_by_name['account_id']._options = None
  _REPLACEORDERREQUEST.fields_by_name['account_id']._serialized_options = b'\340A\002'
  _REPLACEORDERREQUEST.fields_by_name['order_id']._options = None
  _REPLACEORDERREQUEST.fields_by_name['order_id']._serialized_options = b'\340A\002'
  _REPLACEORDERREQUEST.fields_by_name['idempotency_key']._options = None
  _REPLACEORDERREQUEST.fields_by_name['idempotency_key']._serialized_options = b'\340A\002'
  _REPLACEORDERREQUEST.fields_by_name['quantity']._options = None
  _REPLACEORDERREQUEST.fields_by_name['quantity']._serialized_options = b'\340A\002'
  _GETMAXLOTSREQUEST.fields_by_name['account_id']._options = None
  _GETMAXLOTSREQUEST.fields_by_name['account_id']._serialized_options = b'\340A\002'
  _GETMAXLOTSREQUEST.fields_by_name['instrument_id']._options = None
  _GETMAXLOTSREQUEST.fields_by_name['instrument_id']._serialized_options = b'\340A\002'
  _ORDERDIRECTION._serialized_start=6411
  _ORDERDIRECTION._serialized_end=6511
  _ORDERTYPE._serialized_start=6513
  _ORDERTYPE._serialized_end=6623
  _ORDEREXECUTIONREPORTSTATUS._serialized_start=6626
  _ORDEREXECUTIONREPORTSTATUS._serialized_end=6882
  _TIMEINFORCETYPE._serialized_start=6885
  _TIMEINFORCETYPE._serialized_end=7021
  _TRADESSTREAMREQUEST._serialized_start=195
  _TRADESSTREAMREQUEST._serialized_end=234
  _TRADESSTREAMRESPONSE._serialized_start=237
  _TRADESSTREAMRESPONSE._serialized_end=407
  _ORDERTRADES._serialized_start=410
  _ORDERTRADES._serialized_end=688
  _ORDERTRADE._serialized_start=691
  _ORDERTRADE._serialized_end=851
  _POSTORDERREQUEST._serialized_start=854
  _POSTORDERREQUEST._serialized_end=1381
  _POSTORDERRESPONSE._serialized_start=1384
  _POSTORDERRESPONSE._serialized_end=2427
  _CANCELORDERREQUEST._serialized_start=2429
  _CANCELORDERREQUEST._serialized_end=2497
  _CANCELORDERRESPONSE._serialized_start=2499
  _CANCELORDERRESPONSE._serialized_end=2562
  _GETORDERSTATEREQUEST._serialized_start=2565
  _GETORDERSTATEREQUEST._serialized_end=2705
  _GETORDERSREQUEST._serialized_start=2707
  _GETORDERSREQUEST._serialized_end=2750
  _GETORDERSRESPONSE._serialized_start=2752
  _GETORDERSRESPONSE._serialized_end=2838
  _ORDERSTATE._serialized_start=2841
  _ORDERSTATE._serialized_end=4003
  _ORDERSTAGE._serialized_start=4005
  _ORDERSTAGE._serialized_end=4119
  _REPLACEORDERREQUEST._serialized_start=4122
  _REPLACEORDERREQUEST._serialized_end=4414
  _GETMAXLOTSREQUEST._serialized_start=4417
  _GETMAXLOTSREQUEST._serialized_end=4569
  _GETMAXLOTSRESPONSE._serialized_start=4572
  _GETMAXLOTSRESPONSE._serialized_end=5186
  _GETMAXLOTSRESPONSE_BUYLIMITSVIEW._serialized_start=5003
  _GETMAXLOTSRESPONSE_BUYLIMITSVIEW._serialized_end=5145
  _GETMAXLOTSRESPONSE_SELLLIMITSVIEW._serialized_start=5147
  _GETMAXLOTSRESPONSE_SELLLIMITSVIEW._serialized_end=5186
  _GETORDERPRICEREQUEST._serialized_start=5189
  _GETORDERPRICEREQUEST._serialized_end=5411
  _GETORDERPRICERESPONSE._serialized_start=5414
  _GETORDERPRICERESPONSE._serialized_end=6409
  _GETORDERPRICERESPONSE_EXTRABOND._serialized_start=6135
  _GETORDERPRICERESPONSE_EXTRABOND._serialized_end=6299
  _GETORDERPRICERESPONSE_EXTRAFUTURE._serialized_start=6301
  _GETORDERPRICERESPONSE_EXTRAFUTURE._serialized_end=6389
  _ORDERSSTREAMSERVICE._serialized_start=7024
  _ORDERSSTREAMSERVICE._serialized_end=7185
  _ORDERSSERVICE._serialized_start=7188
  _ORDERSSERVICE._serialized_end=8131
# @@protoc_insertion_point(module_scope)
