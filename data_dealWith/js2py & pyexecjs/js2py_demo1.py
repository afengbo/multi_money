import js2py

js2py.eval_js('console.log( "Hello World!" )')
# 'Hello World!'
func_js = '''
function add(a, b) {
    return a + b
}
'''
add = js2py.eval_js(func_js)
print(add(1, 2))
# 3
