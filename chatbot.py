from api_handler import convert_currency

def main():
    print("👋 Welcome to RemitBeeBot!\n")

    try:
        # Ask user for input
        from_currency = input("Enter currency to convert FROM (e.g. USD): ").strip().upper()
        to_currency = input("Enter currency to convert TO (e.g. INR): ").strip().upper()
        amount_str = input(f"Enter amount in {from_currency}: ").strip()

        # Validate amount
        if not amount_str.replace('.', '', 1).isdigit():
            print("❌ Invalid amount. Please enter a number.")
            return

        amount = float(amount_str)

        # Fetch and display result
        print("\n🔄 Fetching live exchange rate...")
        rate, converted = convert_currency(from_currency, to_currency, amount)

        if rate is not None:
            print(f"\n💱 Rate: 1 {from_currency} = {rate:.4f} {to_currency}")
            print(f"💸 {amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
        else:
            print("⚠️ Conversion failed. Please check currency codes or try again later.")

    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print("❌ Unexpected error:", e)

if __name__ == "__main__":
    main()
