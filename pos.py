import pandas as pd
import datetime
import eel

class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_order_count=[]
        self.datetime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        self.item_master=item_master
    
    def add_item_order(self,item_code,item_count):
        self.item_order_list.append(item_code)
        self.item_order_count.append(item_count)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

    def display_order_list(self,item_code):
        for i in self.item_master:
            if i.item_code == item_code:
                return i.item_name,i.price
    
    def add_order(self,item_code,item_count):
        self.order = item_code
        self.count = item_count
        self.add_item_order(self.order,self.count)
        eel.clear_info()

    def display_order_data(self):
        self.sum = 0
        self.count = 0
        for i,j in zip(self.item_order_list,self.item_order_count):
            item_data = self.display_order_list(i)
            self.sum += item_data[1] * int(j)
            self.count += int(j)
            eel.view_log_data('商品名：{0},価格：{1}円,{2}個'.format(item_data[0],item_data[1],j))
            # self.write_receipt('商品名：{0},価格：{1}円,{2}個'.format(item_data[0],item_data[1],j))
        eel.view_log_sum('合計個数：{0}個,合計金額{1}円'.format(self.count,self.sum))
        # self.write_receipt('合計個数：{0}個,合計金額{1}円'.format(self.count,self.sum))
       

    def compute_change(self,money):
        change = int(money) - self.sum          
        if change>=0:    
            eel.view_log_change(change)
            
        else:
            eel.view_log_change('お預かり金額が不足しています')
                
    def write_receipt(self,data):
        with open(self.datetime,mode='a',encoding='utf-8') as f:
            f.write(data + '\n')


        

def add_item_master_from_csv(csv_path):
    item_master =[]
    df = pd.read_csv(csv_path,dtype={'item_code':object})
    for item_code,item_name,price in zip(list(df.item_code),list(df.item_name),list(df.price)):
        item_master.append(Item(item_code,item_name,price))
    return item_master



    
    
### メイン処理
def main():
    # マスタ登録
    item_master = add_item_master_from_csv('item_master.csv')
    
    # オーダー登録
    order=Order(item_master)
    order.add_order()

    
    # オーダー表示
    order.display_order_data()

    order.compute_change()
    
if __name__ == "__main__":
    main()