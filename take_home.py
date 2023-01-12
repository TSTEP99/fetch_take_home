from datetime import date
import json
import os
import psycopg2

def read():
    os.system('awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue > temp.json')
    with open('temp.json', 'r') as file:
        # load the json data from the file
        data = json.load(file)

    body_string = data["Messages"][0]["Body"]
    body_data = json.loads(body_string)
    
    return body_data

def encrypt(data):

    IP_MAP= [4, 2, 8, 7, 1, 9, 0, 3, 5, 6]
    DEVICE_MAP = [1, 3, 4, 0, 6, 8, 2, 9, 7, 5]
    print(data)
    ip = data["ip"]
    device_id = data["device_id"]

    masked_ip = "" 
    masked_device_id = ""

    for s in ip:
        if s == ".":
            masked_ip = masked_ip + s
        else:
            masked_ip = masked_ip + str(IP_MAP[int(s)])

    for s in device_id:
        if s == "-":
            masked_device_id = masked_device_id + s
        else:
            masked_device_id = masked_device_id + str(DEVICE_MAP[int(s)])

    masked_ip = masked_ip[9:]+masked_ip[3:9]+ masked_ip[:3]
    #print(masked_device_id[7:10],masked_device_id[3:7],masked_device_id[:3],masked_device_id[10])
    masked_device_id = masked_device_id[7:10]+masked_device_id[3:7]+masked_device_id[:3]+masked_device_id[10]

    data["ip"] = masked_ip
    data["device_id"] = masked_device_id

    return data

def write(data):
    conn = psycopg2.connect("dbname=postgres user=postgres password=postgres port=5432 host=localhost")
    create_date = date.today()
    SQL1 = "INSERT INTO user_logins(user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) VALUES(%s,%s,%s,%s,%s,%s,%s)"  

    with conn:
        with conn.cursor() as curs:
            curs.execute(SQL1,(data["user_id"],data["device_type"],data["ip"],data["device_id"],data["locale"],data["app_version"][0],create_date))


    # with conn:
    #     with conn.cursor() as curs:
    #         curs.execute("SELECT * FROM user_logins")
    #         records = curs.fetchall()   
    # print(records)
    # conn.close()

if __name__=="__main__":
    while True:
        data = read()
        if "foo" in data:
            break
        encrypt_data = encrypt(data)
        write(encrypt_data)

