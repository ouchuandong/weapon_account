import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import *
def add_data():
    # 获取文本框中的数据
    weapon_name = entry1.get()

    # 建立数据库连接
    db = pymysql.connect(host='localhost', user='root', passwd='****', port=3306, db='t****')

    # 创建游标对象
    cursor = db.cursor()
    table_name = weapon_name
    # 执行插入语句将数据添加到表中
    query = """
CREATE TABLE IF NOT EXISTS {} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    buy_price FLOAT,
    sell_price FlOAT,
    weapon_name VARCHAR(255)
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
    db = pymysql.connect(host='localhost', user='root', passwd='****', port=3306, db='****')

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
   db = pymysql.connect(host='localhost', user='root', passwd='1****', port=3306, db='t****u')

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
    db = pymysql.connect(host='localhost', user='root', passwd='1****a', port=3306, db='t****uu')
    cursor = db.cursor()

    # 查询数据
    query1 = f"SELECT {column_name1} FROM {selected_table}"
    cursor.execute(query1)
    results1 = cursor.fetchall()

    # 清空Listbox
    listbox1.delete(0, 'end')

    # 将数据添加到Listbox中
    for row in results1:
        listbox1.insert('end', row[0])

    query2 = f"SELECT {column_name2} FROM {selected_table}"
    cursor.execute(query2)
    results2 = cursor.fetchall()

    # 清空Listbox
    listbox2.delete(0, 'end')

    # 将数据添加到Listbox中
    for row in results2:
        listbox2.insert('end', row[0])



    # 关闭数据库连接
    cursor.close()
    db.close()


def add_buy():
    selected_table = data_combobox.get()  # 获取选中的表名
    buy_price = entry2.get()  # 获取entry2中的数据

    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='1****', port=3306, db='te****u')
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
    db = pymysql.connect(host='localhost', user='root', passwd='****', port=3306, db='****')
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






















root_window = tk.Tk()
root_window.title("测试程序")

# 创建标签
label = tk.Label(root_window, text="添加武器种类")
label.grid(row=2, column=1, padx=10, pady=10)  # 设置行列位置和内边距



label = tk.Label(root_window, text="历史买入数据")
label.grid(row=1, column=3, padx=100, pady=10)  # 设置行列位置和内边距

label = tk.Label(root_window, text="历史卖出数据")
label.grid(row=1, column=7, padx=100, pady=10)  # 设置行列位置和内边距


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





listbox1 =Listbox(root_window)
listbox1.grid(row=2, column=3,  padx=10, pady=10)

listbox2 =Listbox(root_window)
listbox2.grid(row=2, column=7,  padx=10, pady=10)






# 建立数据库连接
db = pymysql.connect(host='localhost', user='root', passwd='****', port=3306, db='****')

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
