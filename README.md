<div align="center">
<h1>
数据库后端连接方式
</h1>
</div>

# 臭的

## TODO List
- [x] 基础增、删、查、改，增加信息函数添加检查是否已存在主码的功能
- [x] 实现属性排序查找、年龄范围分类查找
- [x] 登录函数，注册函数
- [ ] 二到多属性联合查找
 
## Intro
1. 实现方法：Python `class:db_process`
2. 使用方法：
```python
from db_process import db_process
db = db_process() # 初始化
# 使用函数(例子)
db.append_info('staff',['20001', '李四', '女', '23', '18112341266', '未婚', '经理', '002'])
 ```

## 方法

* sign_in(self, account, password)

  `登录函数，输入：账号，密码`

  `返回是否存在账号，是否密码正确`


* sign_up(self, account, password)

  `注册函数，输入：账号，密码`
  
  `返回是否存在账号，是否注册成功`


* show_all_info(self, sheet)

  `显示表所有信息，输入表名(string)类型`


* delete_info(self, sheet, num)

    `删除表某列信息，输入表名(string)类型，对应主码号`


* search_info(self, sheet, search_prop, search_info)

    `单属性搜索，输入：查询表名，查询属性，查询属性信息(可选)  (全string类型)`
    
    `返回 员工号，姓名，性别，年龄，电话，婚姻，岗位，所在部门号，所在部门名称`


* append_info(self, info)

    `增加员工行信息，输入：列表(list类型)`


* append_department_info(self, info)

    `增加部门行信息，输入：列表(list类型)`


* change_info(self, sheet, num, change_prop, change_info)

    `单修改信息：输入 修改表名，主码号，修改属性，修改信息(全为string类型)`


* sort_info(self, sheet, sort_prop, deacendin=False)

    `单排序信息: 输入 排序表名, 排序属性, 是否倒序(默认否)`


* classify_info(self, sheet, sort_prop, sort_info)

    `单属性分类信息: 输入 排序表名, 分类属性, 分类标签`


* age_info(self, mode, age_num)

    `年龄范围分类: 输入 范围方式('>','=','<'需要是string类型), 分类标签数字或者string都行`

