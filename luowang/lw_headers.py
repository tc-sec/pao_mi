import random


def get_headers2():
    '''
    设置多个请求头，实际是多账号
    封装成为列表的列表，确保choice之后返回的两个请求头中cookie是一致的
    请求头过一段时间就会改变，需要重新从浏览器中复制更换
    :return:
    '''
    headers = [
        [
            {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Authorization': 'Bearer1591770944322-640fd86f-145f-452a-ad18-1f2c2cd8b8f3',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Length': '853',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryOLBTheinO0rm8mLD',
                'Cookie': 'Hm_lvt_7b7f8c848620f517ba2e97ac5881177a=1591767998; localeLanguage=zh; luonetUUID=exTsQS3BE21591768000093; deviceId=exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b; connect.sid=s%3A6c9NkWaeX47pq71X8vaI949AJ0UwJ1F_.kL6PIyeriVllvoN5yr6qyP97AaFpPGSLaZ7W5zqZviM; user-token={%22access_token%22:%221591770944322-640fd86f-145f-452a-ad18-1f2c2cd8b8f3%22%2C%22refresh_token%22:%22e444f188-09da-4003-abf1-4bac8b9eaa1c%22%2C%22scope%22:%22select%22%2C%22token_type%22:%22bearer%22%2C%22expires_in%22:604799}; Hm_lpvt_7b7f8c848620f517ba2e97ac5881177a=1591770944; JSESSIONID=7FCC58BB9D1471AA5CE0A72306CB57E3',
                'deviceId': 'exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b',
                'Host': 'www.luonet.com',
                'If-Modified-Since': 'Thu, 01 Jun 1970 00:00:00 GMT',
                'Origin': 'https://www.luonet.com',
                'Referer': 'https://www.luonet.com/billboard/celebrity/hot',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'shouldIntercept': 'true',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            },
            {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Authorization': 'Bearer1591770944322-640fd86f-145f-452a-ad18-1f2c2cd8b8f3',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'Hm_lvt_7b7f8c848620f517ba2e97ac5881177a=1591767998; localeLanguage=zh; luonetUUID=exTsQS3BE21591768000093; deviceId=exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b; connect.sid=s%3A6c9NkWaeX47pq71X8vaI949AJ0UwJ1F_.kL6PIyeriVllvoN5yr6qyP97AaFpPGSLaZ7W5zqZviM; user-token={%22access_token%22:%221591770944322-640fd86f-145f-452a-ad18-1f2c2cd8b8f3%22%2C%22refresh_token%22:%22e444f188-09da-4003-abf1-4bac8b9eaa1c%22%2C%22scope%22:%22select%22%2C%22token_type%22:%22bearer%22%2C%22expires_in%22:604799}; Hm_lpvt_7b7f8c848620f517ba2e97ac5881177a=1591770997; JSESSIONID=25CFB54A6826E96FFC7A74D4460B217D',
                'deviceId': 'exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b',
                'Host': 'www.luonet.com',
                'If-Modified-Since': 'Thu, 01 Jun 1970 00:00:00 GMT',
                'Referer': 'https://www.luonet.com/billboard/detail?uid=663731372826840&type=1&from=celebrity-hot&fromCategory=douyin-celebrity',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'shouldIntercept': 'true',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            },
        ],
        [
            {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Authorization': 'Bearer1591771044913-6bba95d3-c11c-4f17-9716-0874dc86b25e',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Length': '853',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary418Ciw8TF7HdTwVE',
                'Cookie': 'Hm_lvt_7b7f8c848620f517ba2e97ac5881177a=1591767998; localeLanguage=zh; luonetUUID=exTsQS3BE21591768000093; deviceId=exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b; connect.sid=s%3A6c9NkWaeX47pq71X8vaI949AJ0UwJ1F_.kL6PIyeriVllvoN5yr6qyP97AaFpPGSLaZ7W5zqZviM; user-token={%22access_token%22:%221591771044913-6bba95d3-c11c-4f17-9716-0874dc86b25e%22%2C%22refresh_token%22:%22ea11b3d7-65d1-45c9-927c-4b99f1f09dad%22%2C%22scope%22:%22select%22%2C%22token_type%22:%22bearer%22%2C%22expires_in%22:604799}; Hm_lpvt_7b7f8c848620f517ba2e97ac5881177a=1591771044; JSESSIONID=D8C128745AC0DCB901984DF477A35236',
                'deviceId': 'exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b',
                'Host': 'www.luonet.com',
                'If-Modified-Since': 'Thu, 01 Jun 1970 00:00:00 GMT',
                'Origin': 'https://www.luonet.com',
                'Referer': 'https://www.luonet.com/billboard/celebrity/hot',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'shouldIntercept': 'true',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            },
            {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Authorization': 'Bearer1591771044913-6bba95d3-c11c-4f17-9716-0874dc86b25e',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'Hm_lvt_7b7f8c848620f517ba2e97ac5881177a=1591767998; localeLanguage=zh; luonetUUID=exTsQS3BE21591768000093; deviceId=exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b; connect.sid=s%3A6c9NkWaeX47pq71X8vaI949AJ0UwJ1F_.kL6PIyeriVllvoN5yr6qyP97AaFpPGSLaZ7W5zqZviM; user-token={%22access_token%22:%221591771044913-6bba95d3-c11c-4f17-9716-0874dc86b25e%22%2C%22refresh_token%22:%22ea11b3d7-65d1-45c9-927c-4b99f1f09dad%22%2C%22scope%22:%22select%22%2C%22token_type%22:%22bearer%22%2C%22expires_in%22:604799}; Hm_lpvt_7b7f8c848620f517ba2e97ac5881177a=1591771082; JSESSIONID=7A388AC033ACDB0817573142508B9C67',
                'deviceId': 'exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b',
                'Host': 'www.luonet.com',
                'If-Modified-Since': 'Thu, 01 Jun 1970 00:00:00 GMT',
                'Referer': 'https://www.luonet.com/billboard/detail?uid=663731372826840&type=1&from=celebrity-hot&fromCategory=douyin-celebrity',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'shouldIntercept': 'true',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            },
        ],
        [
            {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Authorization': 'Bearer1591771163918-db5736ef-aafd-4011-b2ee-d61c05fca7cf',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Length': '853',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryn0Q0gUy9cQvxrTz1',
                'Cookie': 'Hm_lvt_7b7f8c848620f517ba2e97ac5881177a=1591767998; localeLanguage=zh; luonetUUID=exTsQS3BE21591768000093; deviceId=exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b; connect.sid=s%3A6c9NkWaeX47pq71X8vaI949AJ0UwJ1F_.kL6PIyeriVllvoN5yr6qyP97AaFpPGSLaZ7W5zqZviM; user-token={%22access_token%22:%221591771163918-db5736ef-aafd-4011-b2ee-d61c05fca7cf%22%2C%22refresh_token%22:%2279f69e5c-3b8f-40b2-bf6b-329ba4cfefc8%22%2C%22scope%22:%22select%22%2C%22token_type%22:%22bearer%22%2C%22expires_in%22:604799}; Hm_lpvt_7b7f8c848620f517ba2e97ac5881177a=1591771164; JSESSIONID=7D7054F98B254127E530C8F52E3D8DD3',
                'deviceId': 'exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b',
                'Host': 'www.luonet.com',
                'If-Modified-Since': 'Thu, 01 Jun 1970 00:00:00 GMT',
                'Origin': 'https://www.luonet.com',
                'Referer': 'https://www.luonet.com/billboard/celebrity/hot',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'shouldIntercept': 'true',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            },
            {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Authorization': 'Bearer1591771163918-db5736ef-aafd-4011-b2ee-d61c05fca7cf',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'Hm_lvt_7b7f8c848620f517ba2e97ac5881177a=1591767998; localeLanguage=zh; luonetUUID=exTsQS3BE21591768000093; deviceId=exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b; connect.sid=s%3A6c9NkWaeX47pq71X8vaI949AJ0UwJ1F_.kL6PIyeriVllvoN5yr6qyP97AaFpPGSLaZ7W5zqZviM; user-token={%22access_token%22:%221591771163918-db5736ef-aafd-4011-b2ee-d61c05fca7cf%22%2C%22refresh_token%22:%2279f69e5c-3b8f-40b2-bf6b-329ba4cfefc8%22%2C%22scope%22:%22select%22%2C%22token_type%22:%22bearer%22%2C%22expires_in%22:604799}; Hm_lpvt_7b7f8c848620f517ba2e97ac5881177a=1591771195; JSESSIONID=80D09AE07CE0B95E57B94A9E9E65E3CE',
                'deviceId': 'exTsQS3BE21591768000093-6b1c6d8dd24d62f41a42f503e033737b',
                'Host': 'www.luonet.com',
                'If-Modified-Since': 'Thu, 01 Jun 1970 00:00:00 GMT',
                'Referer': 'https://www.luonet.com/billboard/detail?uid=663731372826840&type=1&from=celebrity-hot&fromCategory=douyin-celebrity',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'shouldIntercept': 'true',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            },
        ]
    ]
    headers = random.choice(headers)
    return headers
