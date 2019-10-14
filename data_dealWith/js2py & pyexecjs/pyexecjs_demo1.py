import execjs

default_runtime = execjs.get()
print(default_runtime)    # ExternalRuntime(Node.js (V8))
print(default_runtime.name)    # Node.js (V8)

import execjs.runtime_names
# 也可以显示指定名称
node = execjs.get(execjs.runtime_names.Node)
print(node)    # ExternalRuntime(Node.js (V8))
