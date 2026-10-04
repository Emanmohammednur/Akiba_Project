usd = float(input("Enter USD Amount: "))
exchange_rate= float(input("Enter Exchange Rate: "))

etb= usd * exchange_rate

print("=================================================")
print("                CURRENCY EXCHANGE                ")
print("=================================================\n")
print(f"USD Amount: {usd}\n")
print(f"Exchange Rate: 1 USD = {exchange_rate} ETB\n")
print(f"ETB Amount: {etb:,} ETB")
print("=================================================")


