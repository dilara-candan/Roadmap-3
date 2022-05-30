import time

class WebPush():
    platform = "Web"
    optin = True
    global_frequency_capping = 1
    start_date = time.time()
    end_date = time.time() + 86400
    language = "tr_TR"
    push_type = ""

    def send_push(self):
        print("Push Gönderildi")

class TriggerPush(WebPush):
    def __init__(self, trigger_page):
        if (type(trigger_page) != str):
            print("Hatalı sayfa tipi")

        self.push_type = "TriggerPush"
        self.trigger_page = trigger_page

class BulkPush(WebPush):
    def __init__(self, send_date):
        if (type(send_date) != int or send_date < time.time()):
            print("Hatalı gönderim tarihi")

        self.push_type = "BulkPush"
        self.send_date = send_date

class SegmentPush(WebPush):
    def __init__(self, segment_name: str):
        if (type(segment_name) != str):
            print("Hatalı segment ismi")

        self.push_type = "SegmentPush"
        self.segment_name = segment_name

class PriceAlertPush(WebPush):
    def __init__(self):
        self.push_type = "PriceAlertPush"

    def discountPrice(self, price_info, discount_rate):
        return price_info - (price_info * discount_rate / 100)

class InStockPush(WebPush):
    def __init__(self):
        self.stock_info = True
        self.push_type = "InStockPush"

    def stockUpdate(self):
        self.stock_info = not self.stock_info

        return self.stock_info

# TriggerPush
print("\n------------------------------------------------------------\nTriggerPush\n------------------------------------------------------------")
test1 = TriggerPush("HomePage")

print("PushType : " + test1.push_type)

test1.send_push()

# BulkPush
print("\n------------------------------------------------------------\nBulkPush\n------------------------------------------------------------")
test2 = BulkPush(1656150514)

print("PushType : " + test2.push_type)

test2.send_push()

# SegmentPush
print("\n------------------------------------------------------------\nSegmentPush\n------------------------------------------------------------")
test3 = SegmentPush("Segment1")

print("PushType : " + test3.push_type)

test3.send_push()

# PriceAlertPush
print("\n------------------------------------------------------------\nPriceAlertPush\n------------------------------------------------------------")
test4 = PriceAlertPush()

print("Discounted Price : " + str(test4.discountPrice(50, 10)))
print("PushType : " + test4.push_type)

test4.send_push()

# InStockPush
print("\n------------------------------------------------------------\nInStockPush\n------------------------------------------------------------")
test5 = InStockPush()

print("Stock Update : " + str(test5.stockUpdate()))
print("Stock Update : " + str(test5.stockUpdate()))
print("PushType : " + test5.push_type)

test5.send_push()
