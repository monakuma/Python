price=int(input("料金を入力"))
number=int(input("人数を入力"))
payment=int(price//number)
print(("お支払いは{}円です").format(payment))
# 文字列補完
print(f"お支払いは{payment}円です")