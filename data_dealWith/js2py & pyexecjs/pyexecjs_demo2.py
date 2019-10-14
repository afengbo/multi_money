import execjs

# 简单使用：直接调用方法/函数
ret = execjs.eval("'red yellow blue'.split(' ')")
print(ret)
# 由于现在console命令是node的环境下运行，因此该语句不会出现在python的终端上
execjs.eval("console.log(123)")
