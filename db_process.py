import pymysql as pm


class db_process:
    def __init__(self):
        self.db = pm.connect(host='localhost', user='root', password='123456', db='hrms', port=3306)
        print('连接数据库成功')
        self.cur = self.db.cursor()

        self.dict_column = {'staff_num': 0, 'staff_name': 1, 'gender': 2, 'age': 3, 'phone': 4, 'marriage': 5,
                            'post': 6, 'department_num': 7, 'department_name': 1}
        self.class_column = ['gender', 'marriage', 'post', 'department_num', 'department_name']

    # 登录函数，输入：账号，密码
    # 返回是否存在账号，是否密码正确
    def sign(self, account, password):
        self.cur.execute('select * from admin')
        result = self.cur.fetchall()
        account_list = []
        for i in range(len(result)):
            account_list[i] = result[i][0]
        if account not in account_list:
            print('账号不存在')
        else:
            if str(password) == result[account_list.index(account)][1]:
                print('登录成功')
            else:
                print('密码错误')


    # 显示表所有信息，输入表名(string)类型
    def show_all_info(self, sheet):
        self.cur.execute(f'select * from {sheet}')
        wholesheet = self.cur.fetchall()
        print(wholesheet)
        return wholesheet

    # 删除表某列信息，输入表名(string)类型，对应主码号
    def delete_info(self, sheet, num):
        self.cur.execute(f'delete from {sheet} where {sheet}_num = {num}')
        print('删除成功')
        self.db.commit()

    # 单属性搜索，输入：查询表名，查询属性，查询属性信息(可选)  (全string类型)
    # 返回 员工号，姓名，性别，年龄，电话，婚姻，岗位，所在部门号，所在部门名称
    def search_info(self, sheet, search_prop, search_info):
        self.cur.execute(
            f'select staff_num, staff_name, gender, age, phone, marriage, post, staff.department_num, department_name from staff left join department d on staff.department_num = d.department_num where {search_prop} = {search_info}')
        result = self.cur.fetchall()
        print(result)
        return result

    # 增加员工行信息，输入：列表(list类型)
    def append_info(self, info):
        self.cur.execute(
            f'insert into staff values {info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7]}')
        self.db.commit()

    # 增加部门行信息，输入：列表(list类型)
    def append_department_info(self, info):
        self.cur.execute(
            f'insert into staff values {info[0], info[1]}')
        self.db.commit()

    # 单修改信息：输入 修改表名，主码号，修改属性，修改信息(全为string类型)
    def change_info(self, sheet, num, change_prop, change_info):
        self.cur.execute(f'select * from {sheet} where {sheet}_num = num')
        result = self.cur.fetchall()
        l = list(result[0])
        if sheet == 'staff':
            l[self.dict_column[f'{change_prop}']] = str(change_info)  # 修改员工表对应属性的信息
            self.delete_info('staff', num)
            self.append_info(l)

        if sheet == 'department':  # 修改部门表对应属性的信息
            if change_prop == 'department_num':
                l[0] = str(change_info)
            else:
                l[self.dict_column[f'{change_prop}']] = str(change_info)
            self.delete_info('department', num)
            self.append_info(l)

    # 单排序信息: 输入 排序表名, 排序属性, 是否倒序(默认否)
    def sort_info(self, sheet, sort_prop, deacendin=False):
        if not deacendin:
            self.cur.execute(f'select * from {sheet} order by {sort_prop}')
            result = self.cur.fetchall()
            return result
        else:
            self.cur.execute(f'select * from {sheet} order by {sort_prop} DESC ')
            result = self.cur.fetchall()
            return result

    # 单属性分类信息: 输入 排序表名, 分类属性, 分类标签
    def classify_info(self, sheet, sort_prop, sort_info):
        if sort_prop not in self.class_column:
            print('该属性无法分类')
        else:
            self.cur.execute(f'select * from {sheet} where {sort_prop} = {sort_info}')
        result = self.cur.fetchall()
        return result

    # 年龄范围分类: 输入 范围方式('>','=','<'需要是string类型), 分类标签数字或者string都行
    def age_info(self, mode, age_num):
        self.cur.execute(
            f'select staff_num, staff_name, gender, age, phone, marriage, post, staff.department_num, department_name from staff left join department d on staff.department_num = d.department_num where age {mode} {age_num}')
        result = self.cur.fetchall()
        print(result)
        return result

    # TODO:两属性联合查找
    def combine_info(self):
        pass

# def test_class(self):
#     print('test_np')
