import requests

url = "https://www.msmemart.com/msme/fetch_listings/0"

payload = {
    'searchText': '',
    'catalog': 'Supplier',
    'category': '90',
    'subcategory': '1297',
    'type': 'company-list',
    'csrf': '5dce5147397e0b5488258956c157a7e9',
    'pid': ''
}
headers = {
    'Cookie': 'unique_visitor=103.160.64.163; ci_session=ugut8l6dcsktp0o3sbk7acevudhduccr; csrf=5dce5147397e0b5488258956c157a7e9; ci_session=ugut8l6dcsktp0o3sbk7acevudhduccr; csrf=aac3c53559a50bfbaee9ff4b4f5e0c76',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}


def mainFunc():
    print("Request for data sent")

    response = requests.request(
        "POST", url, headers=headers, data=payload)

    print("Response received")
    print("========================================================================")
    print(response.content)


mainFunc()