filename='student.txt'
import os
def main():
    while True:
        stumenu()
        choice=int(input("请选择您的服务类型："))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input("您确定要退出系统吗？y/n:")
                if answer=='y' or answer=='Y':
                    print("谢谢您的使用！！！")
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()
def stumenu():
    print("==========================================================学生信息管理系统============================================")
    print("-----------------------------------------------------------主界面功能菜单-------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1.录入学生信息")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t3.删除学生信息")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t4.修改学生信息")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t5.成绩排序")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t7.显示所有学生信息")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t0.退出系统")
    print("----------------------------------------------------------------------------------------------------------------------------")
def insert():
    student_list=[]
    while True:
        id=input("请输入学生的学号（如1001）：")
        if not id:
            break
        name=input("请输入学生姓名：")
        if not name:
            break
        try:
            english=int(input("请输入学生英语成绩："))
            python=int(input("请输入学生python成绩："))
            modian=int(input("请输入学生模电成绩："))
            dawu=int(input("请输入学生大学物理成绩："))
        except:
            print("输入无效，学生成绩不是整数，请重新输入！！！")
            continue
        #录入信息保存
        student={'id':id,'name':name,'english':english,'python':python,'modian':modian,'dawu':dawu}
        #添加到列表中
        student_list.append(student)
        answer=input("请选择是否继续添加y/n：")
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    save(student_list)
    print("学生信息录入完毕！")
def save(lst):
    try:
        stu_txt = open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input("按学号查询请输入1，按姓名查询请输入2：")
            if mode=='1':
                id=input("请输入学生的学号：")
            elif mode=='2':
                name=input("请输入学生的姓名：")
            else:
                print("您的输入有误，请重新输入！")
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input("请选择是否继续查找y/n:")
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break

        else:
            print("此学生暂未保存！")
            return
def show_student(lst):
    if len(lst)==0:
        print("没有此学生信息，无数据显示！！！")
        return
#定义格式
    format_title='{:^6}\t{:^12}\t{:^10}\t{:^8}\t{:^8}\t{:^8}\t{:20}'
    print(format_title.format('id','姓名','英语成绩','python成绩','模电成绩','大学物理成绩','总成绩'))
    format_data='{:^6}\t{:^12}\t{:^10}\t{:^12}\t{:^12}\t{:^9}\t{:9}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('modian'),
                                 item.get('dawu'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('modian'))+int(item.get('dawu'))
                                     ))
def delete():
    while True:
        student_id=input("请输入删除学生的学号：")
        if student_id !='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f"学号为{student_id}的学生已被删除")
                    else:
                        print(f"未找到学号为{student_id}的学生")
            else:
                print("无学生信息")
                break
            show()
            answer=input("请选择是否继续删除y/n:")
            if answer=='y' or answer=='Y':
                continue
            else:
                break
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input("请输入要修改学生的学号：")
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id']==student_id:
                print("找到了这名学生，可以修改信息")
                while True:
                    try:
                        d['name']=input("请输入姓名：")
                        d['english']=input("请输入英语成绩：")
                        d['python'] = input("请输入python成绩：")
                        d['modian'] = input("请输入模电成绩：")
                        d['dawu'] = input("请输入大学物理成绩：")
                    except:
                        print("您的输入有误，请重新输入！")
                    else:
                        break
                wfile.write(str(d)+'\n')
                print("修改成功")
            else:
                wfile.write(str(d) + '\n')
        answer = input("请选择是否修改y/n:")
        if answer == 'y' or answer == 'Y':
            modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
        student_new=[]
        for item in student_list:
            d=dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_dasc=input("请选择升序（1）还是降序（0）：")
    if asc_or_dasc=='1':
        asc_or_dasc_bool=True
    elif asc_or_dasc=='0':
        asc_or_dasc_bool=False
    else:
        print("您的输入有误，请重新输入！！")
        sort()
    mode=input("请选择排序方式，按英语成绩排序请按1，按python成绩查询请按2，按模电成绩查询请按3，按大学物理成绩查询请按4，按总成绩查询请按0：")
    if mode=='1':
        student_new.sort(key=lambda x: int(x['english']),reverse=asc_or_dasc_bool)
    elif mode=='2':
        student_new.sort(key=lambda x: int(x['python']),reverse=asc_or_dasc_bool)
    elif mode=='3':
        student_new.sort(key=lambda x: int(x['modian']), reverse=asc_or_dasc_bool)
    elif mode=='4':
        student_new.sort(key=lambda x: int(x['dawu']),reverse=asc_or_dasc_bool)
    elif mode=='0':
        student_new.sort(key=lambda x: int(x['english'])+int(x['python'])+ int(x['modian'])+int(x['dawu']),reverse=asc_or_dasc_bool)
    else:
        print("您的输入有误，请重新输入！！！")
        sort()
    show_student(student_new)
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print("还没有录入学生信息")
    else:
        print("暂未保存数据")
def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            for item in students:
                student_list.append(eval(item))
            if student_list:
                show_student(student_list)
    else:
        print("还没有录入数据")
if __name__ == '__main__':
    main()
