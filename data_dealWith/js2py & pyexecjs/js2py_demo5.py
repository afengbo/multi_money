import js2py
# 前提：先安装好nodejs，并使用 npm install crypto-js 安装
# crypto-js是node中数据加密、解密算法库

# 获取nodejs中环境中安装的crypto-js模块
CryptoJS = js2py.require('crypto-js')
data = [{'data1': "hello world"}, {'data2': 666}]
JSON = js2py.eval_js('JSON')   # 获取js中的JSON对象
ciphertext = CryptoJS.AES.encrypt(JSON.stringify(data), 'secret key 123')
print("ciphertext: ", ciphertext)
bytes = CryptoJS.AES.decrypt(ciphertext.toString(), 'secret key 123')
print("bytes: ", bytes)
decryptedData = JSON.parse(bytes.toString(CryptoJS.enc.Utf8)).to_list()
print("decryptedData: ", decryptedData)
