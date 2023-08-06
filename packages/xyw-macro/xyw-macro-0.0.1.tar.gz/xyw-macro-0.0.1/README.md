# 快速开始

```python
import time
from xyw_macro import *


def func1():
    time.sleep(4)
    print('func1')


def func2():
    print('func2')


macro = Macro()
config1 = Configuration('01', 'part', Configuration.FUNCTION)
config1.add_command(Condition(VK('VK_F3'), '打印'), func1)
config2 = Configuration('02', 'all', Configuration.FUNCTION)
config2.add_command(Condition(VK('VK_F2'), '打印'), func2)

macro.add_config(config1)
macro.add_config(config2)
macro.run()

```

# Release Notes

## 0.0.1

- 初次发布，实现了键盘宏的基本功能