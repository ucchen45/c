# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:20:11 2023

@author: youxi
"""

def main():
    while True:
        print("1.添加書籍\n2.刪除書籍\n3.更新庫存\n4.顯示庫存\n5.退出")
        select=input("請輸入選項(1/2/3/4/5)：")
        if select=="1":
            new={"書名":"","數量":"","price":""}
            new["書名"]=input("請輸入書名：")
            new["價格"]=input("請輸入價格：")
            new["數量"]=input("請輸入數量：")
            books.append(new)
            print("書籍「{}」已成功加入庫存".format(new["書名"]))
            continue
        elif select=="2":
            delete=(input("請輸入書名："))
            for book in books:
                if delete==book["書名"]:
                    books.remove(book)
                    print(f"書籍「{delete}」已成功從庫存移除")
        elif select=="3":
            renew=input("請輸入書名：")
            for book in books:
                if renew==book["書名"]:
                    new_amount=input("請輸入更新數量：")
                    book["數量"]=new_amount
                    print("書籍「{}」的庫存已更新為{}本".format(book["書名"],new_amount))
        elif select=="4":
            for book in books:
                if "書名" in book:
                    name=book["書名"]
                    print(f"書名：{name}，",end="")
                    if "價格" in book:
                        price=book["價格"]
                        print(f"價格：{price}元，",end="")
                        if "數量" in book:
                            amount=book["數量"]
                            print(f"庫存：{amount}本")
        elif select=="5":
            print("感謝使用")
            break
        else:
            print("輸入錯誤")
            continue
books=[
       {"書名":"笑傲江湖(一)","價格":350,"數量":4},
       {"書名":"亦搖亦點頭","價格":500,"數量":7},
       {"書名":"中興國文","價格":330,"數量":5},
       {"書名":"科學超電磁砲01","價格":200,"數量":10}
       ]
main()