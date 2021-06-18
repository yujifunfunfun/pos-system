import eel
from pos import Order
import pos


item_master = pos.add_item_master_from_csv('item_master.csv')
order = Order(item_master)
@eel.expose
def add_order(item_code,item_count):
    order.add_order(item_code,item_count)

@eel.expose
def display_order_data():
    order.display_order_data()

@eel.expose
def compute_change(money):
    order.compute_change(money)

eel.init('template')
eel.start('index.html')