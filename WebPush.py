import datetime

class WebPush():
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language

    def send_push(self):
        print("* " + self.__class__.__name__ + " Gönderildi")
        
        return self

    def get_push_info(self):
        print("* Push Bilgileri: " + str(self.__dict__))
        
        return self

class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, trigger_page):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language)

        self.trigger_page = trigger_page

class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, send_date):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language)

        self.send_date = send_date

class SegmentPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, segment_name):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language)
        
        self.segment_name = segment_name

class PriceAlertPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, price_info, discount_rate):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language)

        self.price_info = price_info
        self.discount_rate = discount_rate

    def discountPrice(self):
        return self.price_info - self.price_info * self.discount_rate

class InStockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, stock_info):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language)

        self.stock_info = stock_info

    def stockUpdate(self):
        self.stock_info = not self.stock_info

        return self.stock_info

# TriggerPush
print("\n------------------------------------------------------------\nTriggerPush\n------------------------------------------------------------")

TriggerPush("Desktop", True, 15, datetime.datetime(2022, 1, 1).strftime("%m/%d/%Y"), datetime.datetime(2022, 2, 1).strftime("%m/%d/%Y"), "tr_TR", "HomePage").send_push().get_push_info()

# BulkPush
print("\n------------------------------------------------------------\nBulkPush\n------------------------------------------------------------")

BulkPush("Mobile", True, 10, datetime.datetime(2022, 4, 1).strftime("%m/%d/%Y"), datetime.datetime(2022, 5, 1).strftime("%m/%d/%Y"), "en_US", 10).send_push().get_push_info()

# SegmentPush
print("\n------------------------------------------------------------\nSegmentPush\n------------------------------------------------------------")

SegmentPush("Desktop", True, 50, datetime.datetime(2022, 7, 1).strftime("%m/%d/%Y"), datetime.datetime(2022, 10, 1).strftime("%m/%d/%Y"), "tr_TR", "DiscountBuyers").send_push().get_push_info()

# PriceAlertPush
print("\n------------------------------------------------------------\nPriceAlertPush\n------------------------------------------------------------")

priceAlertPush = PriceAlertPush("Desktop", True, 10, datetime.datetime(2022, 5, 1).strftime("%m/%d/%Y"), datetime.datetime(2022, 9, 1).strftime("%m/%d/%Y"), "tr_TR", 250, 0.3)
priceAlertPush.send_push().get_push_info()

print("* İndirimli Fiyat: " + str(priceAlertPush.discountPrice()))

# InStockPush
print("\n------------------------------------------------------------\nInStockPush\n------------------------------------------------------------")

inStockPush = InStockPush("Desktop", True, 10, datetime.datetime(2022, 5, 1).strftime("%m/%d/%Y"), datetime.datetime(2022, 9, 1).strftime("%m/%d/%Y"), "tr_TR", False)
inStockPush.send_push().get_push_info()

print("* Stok durumu: " + str(inStockPush.stockUpdate()))
