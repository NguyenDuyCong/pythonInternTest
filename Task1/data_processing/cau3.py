# -*-coding:utf-8-*-
"""
3. Truy cập theo địa chỉ https://www.shopify.com tạo 1 site test (click start free trial)
Login vào site test vừa tạo, lấy info APi theo hướng dẫn: https://litextension.com/migration-guides/how-to-get-api/get-api-from-shopify
vào tab customer tạo thử 1 vài customer
Lấy customer từ site vừa tạo sử dụng api, lưu ra file
	- lấy hết customer về, lưu vào 1 file csv, bỏ qua k cần lưu addresss
	- docs:
https://shopify.dev/tutorials/authenticate-a-private-app-with-shopify-admin#make-authenticated-requests
https://shopify.dev/docs/admin-api/rest/reference/customers/customer#index-2020-04
"""
import requests
import json
import csv

api_key = "82b56e723ab35e83dff56ee1ebfef88f"
password = ""
hostname = "congnguyen-uet.myshopify.com"
version = "2020-10"
resource = "customers"

# url format: https://{apikey}:{password}@{hostname}/admin/api/{version}/{resource}.json
api_url = "https://" + api_key + ":" + password + "@" + hostname + "/admin/api/" + version + "/" + resource + ".json"
headers = {"Accept": "application/json", "Content-Type": "application/json"}
r = requests.get(api_url, headers=headers)
# get data format json from requests
data = r.json()

# save json string to customers_data.json file
with open('customers_data.json', 'w') as file:
    json.dump(data, file)
print(data)

# data = {"customers": [{"id":...},{"id":...}...]}
# customers_data = [{"id":...},{"id":...}]
customers_data = data['customers']
for customer in customers_data:
    customer.pop('addresses')
# print(customers_data[0])

with open('data_file.csv', 'w') as file:
    csv_writer = csv.writer(file)
    count = 0

    for customer in customers_data:
        # write row includes header
        if count == 0:
            header = customer.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(customer.values())

    file.close()
