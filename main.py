import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import *
import mysql.connector
def add_data():
    # 获取文本框中的数据
    weapon_name = entry1.get()

    # 建立数据库连接
    db = pymysql.connect(host='localhost', user='root', passwd='1138754072Aa', port=3306, db='test_uu')

    # 创建游标对象
    cursor = db.cursor()
    table_name = weapon_name
    # 执行插入语句将数据添加到表中
    query = """
CREATE TABLE IF NOT EXISTS {} (
    
    buy_price FLOAT,
    sell_price FlOAT,
    weapon_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""".format(table_name)
    cursor.execute(query)
    db.commit()

    # 关闭数据库连接
    db.close()

    # 更新下拉列表框的选项值
    update_combobox()

def update_combobox():
    # 建立数据库连接
    db = pymysql.connect(host='localhost', user='root', passwd='1138754072Aa', port=3306, db='test_uu')

    # 创建游标对象
    cursor = db.cursor()

    # 执行查询语句获取数据
    query =  "SHOW TABLES"
    cursor.execute(query)
    data_list =[row[0] for row in cursor.fetchall()]





    # 关闭数据库连接
    db.close()

    # 更新下拉列表框的选项值
    data_combobox['values'] = data_list

def delete_data():
   combox_value =data_combobox.get()
   db = pymysql.connect(host='localhost', user='root', passwd='1138754072Aa', port=3306, db='test_uu')

   # 创建游标对象
   cursor = db.cursor()

   # 执行查询语句获取数据
   query =f"DROP TABLE {combox_value}"
   cursor.execute(query)
   db.commit()
   cursor.close()
   db.close()
   update_combobox()





def get_table_data(event):
    selected_table = data_combobox.get()  # 获取选中的表名
    column_name1 = "buy_price"  # 指定要显示的列名
    column_name2 = "sell_price"
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='1138754072Aa', port=3306, db='test_uu')
    cursor = db.cursor()

    # 查询数据
    query1 = f"SELECT {column_name1} FROM {selected_table}"
    cursor.execute(query1)
    results1 = cursor.fetchall()

    # 清空Listbox
    listbox1.delete(0, 'end')
    num_buy=0
    # 将数据添加到Listbox中
    for row in results1:
        if row[0]is not None:
            num_buy +=1
        listbox1.insert('end', row[0])

    query2 = f"SELECT {column_name2} FROM {selected_table}"
    cursor.execute(query2)
    results2 = cursor.fetchall()

    # 清空Listbox
    listbox2.delete(0, 'end')
    num_sell = 0
    # 将数据添加到Listbox中
    for row in results2:
        if row[0]is not None:
            num_sell+=1
        listbox2.insert('end', row[0])

    query3 = f"SELECT SUM(buy_price) AS total_buy_price FROM {selected_table}"
    cursor.execute(query3)
    result = cursor.fetchone()
    total_buy_price = result[0]
    label2.config(text="总买入: {:.2f}".format(total_buy_price)+'数量'+str(num_buy))

    query4 = f"SELECT SUM(sell_price) AS total_sell_price FROM {selected_table}"
    cursor.execute(query4)
    result = cursor.fetchone()
    total_sell_price = result[0]
    label3.config(text="总卖出: {:.2f}".format(total_sell_price)+'数量'+str(num_sell))

    cursor.execute("SHOW TABLES;")
    table_names = cursor.fetchall()

    # 初始化总销售价格为0
    all_total_sell_price = 0
    all_total_buy_price = 0
    # 遍历所有表
    for table in table_names:
        table_name = table[0]

        # 执行查询，获取当前表的sell_price列的和
        cursor.execute("SELECT SUM(sell_price) FROM {};".format(table_name))
        result = cursor.fetchone()
        sell_price_sum = result[0]

        # 如果sum函数返回的结果不为空，则将其累加到总销售价格
        if sell_price_sum is not None:
            all_total_sell_price += sell_price_sum

        cursor.execute("SELECT SUM(buy_price) FROM {};".format(table_name))
        result = cursor.fetchone()
        buy_price_sum = result[0]

        # 如果sum函数返回的结果不为空，则将其累加到总销售价格
        if buy_price_sum is not None:
            all_total_buy_price += buy_price_sum

    label4.config(text="利润: {:.2f}".format(all_total_sell_price-all_total_buy_price))






    # 关闭数据库连接
    cursor.close()
    db.close()








def add_buy():
    selected_table = data_combobox.get()  # 获取选中的表名
    buy_price = entry2.get()  # 获取entry2中的数据

    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='1138754072Aa', port=3306, db='test_uu')
    cursor = db.cursor()

    # 插入数据
    query = f"INSERT INTO {selected_table} (buy_price) VALUES ('{buy_price}')"
    cursor.execute(query)
    db.commit()

    query1 = f"SELECT buy_price FROM {selected_table}"
    cursor.execute(query1)
    results1 = cursor.fetchall()

    # 清空Listbox1
    listbox1.delete(0, 'end')

    # 将数据添加到Listbox1中
    for row in results1:
        listbox1.insert('end', row[0])
    # 关闭数据库连接
    cursor.close()
    db.close()


def add_sell():
    selected_table = data_combobox.get()  # 获取选中的表名
    sell_price = entry3.get()  # 获取entry2中的数据

    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='1138754072Aa', port=3306, db='test_uu')
    cursor = db.cursor()

    # 插入数据
    query = f"INSERT INTO {selected_table} (sell_price) VALUES ('{sell_price}')"
    cursor.execute(query)
    db.commit()

    query1 = f"SELECT sell_price FROM {selected_table}"
    cursor.execute(query1)
    results1 = cursor.fetchall()

    # 清空Listbox1
    listbox2.delete(0, 'end')

    # 将数据添加到Listbox1中
    for row in results1:
        listbox2.insert('end', row[0])
    # 关闭数据库连接
    cursor.close()
    db.close()



def delete_buy():
    selected_table = data_combobox.get()  # 获取选中的表名
    ##buy_price = entry2.get()  # 获取entry2中的数据
    selected_data  = listbox1.curselection()
    buy_price = listbox1.get(selected_data)

    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='1138754072Aa', port=3306, db='test_uu')
    cursor = db.cursor()

    # 插入数据
    query = f"DELETE FROM {selected_table} WHERE buy_price = '{buy_price}'"
    cursor.execute(query)
    db.commit()

    query1 = f"SELECT buy_price FROM {selected_table}"
    cursor.execute(query1)
    results1 = cursor.fetchall()

    # 清空Listbox1
    listbox1.delete(0, 'end')

    # 将数据添加到Listbox1中
    for row in results1:
        listbox1.insert('end', row[0])
    # 关闭数据库连接
    cursor.close()
    db.close()


def delete_sell():
    selected_table = data_combobox.get()  # 获取选中的表名
    selected_index = listbox2.curselection()  # 获取选中项的索引
    if selected_index:
        sell_price = listbox2.get(selected_index[0])  # 获取选中项的唯一sell_price值

        # 连接数据库
        db = pymysql.connect(host='localhost', user='root', passwd='1138754072Aa', port=3306, db='test_uu')
        cursor = db.cursor()

        # 删除数据
        query = f"DELETE FROM {selected_table} WHERE sell_price = '{sell_price}'"
        cursor.execute(query)
        db.commit()

        # 重新获取数据
        query1 = f"SELECT sell_price FROM {selected_table}"
        cursor.execute(query1)
        results1 = cursor.fetchall()

        # 清空Listbox2
        listbox2.delete(0, 'end')

        # 将数据添加到Listbox2中
        for row in results1:
            listbox2.insert('end', row[0])

        # 关闭数据库连接
        cursor.close()
        db.close()








root_window = tk.Tk()
root_window.title("测试程序")

# 创建标签
label1 = tk.Label(root_window, text="添加武器种类")
label1.grid(row=2, column=1, padx=10, pady=10)  # 设置行列位置和内边距



label2 = tk.Label(root_window, text="历史买入数据")
label2.grid(row=1, column=3, padx=100, pady=10)  # 设置行列位置和内边距

label3 = tk.Label(root_window, text="历史卖出数据")
label3.grid(row=1, column=7, padx=100, pady=10)  # 设置行列位置和内边距

label4 = tk.Label(root_window, text="历史卖出数据")
label4.grid(row=1, column=10, padx=10, pady=10)  # 设置行列位置和内边距


# 文本框添加武器
entry1 = tk.Entry(root_window)
entry1.grid(row=2, column=2, padx=10, pady=10)  # 设置行列位置和内边距



# 文本框添加武器


entry2 = tk.Entry(root_window)
entry2.grid(row=3, column=3, padx=20, pady=20)  # 设置行列位置和内边距

entry3 = tk.Entry(root_window)
entry3.grid(row=3, column=7, padx=20, pady=20)  # 设置行列位置和内边距





button = tk.Button(root_window, text="添加数据", command=add_data)
button.grid(row=3, column=1,  padx=10, pady=10)  # 设置行列位置和内边距

button2 = tk.Button(root_window, text="删除数据", command=delete_data)
button2.grid(row=3, column=2,  padx=10, pady=10)  # 设置行列位置和内边距

button3 = tk.Button(root_window, text="+", command=add_buy)
button3.grid(row=3, column=4,  padx=10, pady=10)  # 设置行列位置和内边距

button4 = tk.Button(root_window, text="+", command=add_sell)
button4.grid(row=3, column=8,  padx=10, pady=10)  # 设置行列位置和内边距

button5 = tk.Button(root_window, text="-", command=delete_buy)
button5.grid(row=3, column=5,  padx=10, pady=10)  # 设置行列位置和内边距

button6 = tk.Button(root_window, text="-", command=delete_sell)
button6.grid(row=3, column=9,  padx=10, pady=10)  # 设置行列位置和内边距





listbox1 =Listbox(root_window)
listbox1.grid(row=2, column=3,  padx=10, pady=10)

listbox2 =Listbox(root_window)
listbox2.grid(row=2, column=7,  padx=10, pady=10)





# 建立数据库连接
db = pymysql.connect(host='localhost', user='root', passwd='1138754072Aa', port=3306, db='test_uu')

# 创建游标对象
cursor = db.cursor()

# 执行查询语句获取数据
query = "SHOW TABLES"
cursor.execute(query)
data_list = [row[0] for row in cursor.fetchall()]

# 关闭数据库连接
db.close()

# 创建下拉列表框并设置数据
data_combobox = ttk.Combobox(root_window, state='readonly', values=data_list)
data_combobox.grid(row=1, column=2,  padx=5, pady=5)  # 设置行列位置和内边距
data_combobox.bind("<<ComboboxSelected>>", get_table_data)
root_window.mainloop()


