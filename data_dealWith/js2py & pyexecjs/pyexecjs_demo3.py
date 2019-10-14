import execjs

# 复杂使用：需要先对js代码进行预编译
js_code = '''
function f(temp) {
    console.log(temp);
    return "Hello World!";
};
'''

# 编译代码
js_context = execjs.compile(js_code)
# 利用call方法调用对应的方法
ret2 = js_context.call("f", "test")
print(ret2)
