import js2py

# 在js代码中导入python模块并使用
# 使用pyimport语法
js_code = '''
pyimport requests
console.log("导入成功");
var response = requests.get("http://www.baidu.com");
console.log(response.url);
console.log(response.content);
'''
# 执行js代码，
js2py.eval_js(js_code)
