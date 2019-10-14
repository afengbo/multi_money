import js2py

# 将sum函数传入js的上下文执行环境中进行使用
print("sum: ", sum([1,2,3]))
context = js2py.EvalJs({'python_sum': sum})
print("context.python_sum: ", context.python_sum)
js_code = '''
python_sum([1,2,3])
'''
print("js_code运行结果: ", context.eval(js_code))
