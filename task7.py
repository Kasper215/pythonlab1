def process_addresses():
    addresses = [
        "www.google.com",
        "www.yandex",
        "example.net",
        "www.pythontutor",
        "github.com",
        "www.my-site.org"
    ]
    
    updated_addresses = [
        ("http://" + s if s.endswith(".com") else "http://" + s + ".com") 
        if s.startswith("www") 
        else s 
        for s in addresses
    ]
    
    print("Исходный список:")
    print(addresses)
    print("\nИзмененный список:")
    print(updated_addresses)

if __name__ == "__main__":
    process_addresses()
