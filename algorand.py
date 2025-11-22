def create_account():
    # stubbed account object (for demo only)
    account = {
        "address": "SAMPLEADDRESS",
        "private_key": "KEEP_THIS_SAFE"
    }
    return account

def main():
    acct = create_account()
    print("Account address:", acct["address"])
    print("This is a demo account. Replace with real code before submission.")

if __name__ == "__main__":
    main()
