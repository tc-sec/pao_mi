ll = [{
                        "购买方式": "公开版",
                        "版本": "64GB",
                        "skuId": 100004770235,
                        "颜色": "黑色"
                    }, {
                        "购买方式": "保值换新版",
                        "版本": "64GB",
                        "skuId": 100013694864,
                        "颜色": "黑色"
                    }, {
                        "购买方式": "官方AppleCare+版",
                        "版本": "64GB",
                        "skuId": 100013531844,
                        "颜色": "黑色"
                    }, {
                        "购买方式": "AirPods Pro套装",
                        "版本": "64GB",
                        "skuId": 100005492547,
                        "颜色": "黑色"
                    }
    ]
for l in ll:
    l.pop('skuId')
    print(list(l.values()))