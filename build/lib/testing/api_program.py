from woocommerce import API
import pprint

wcapi = API(
    url="http://localhost:7888/site",
    consumer_key="ck_66def9128cb372bf9fd9ecf362eb142a7ed41026",
    consumer_secret="cs_a488a05b34bc6fbfbe53b5b3397e8b823d4af330",
    version="wc/v3"
)


r = wcapi.get("products")
print(r.json())