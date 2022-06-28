'''
数据 crud
添加数据 crate
读取数据 read
修改数据 update
删除数据 delete
'''
'''
单条数据添加
    1.实例化类，创建表数据
    2.将梳理添加到session（add）
    3.提交更新（commit）
    4.关闭session
批量数据添加
'''
'''
批量数据添加
    1.多次实例化类，创建多条表数据
    2.将多个实例依次添加到session中（add）或者一次性添加到session中（add_all）
    3.提交更新（commit）
    4.关闭session
'''
'''
查询数据：
  查询表中全部数据
    格式：类.query.all()
    
  条件查询
    格式：类.query.filter_by(条件).单条或多条
    查询单条数据
        类.query.filter_by(条件).first()
    查询多条数据
        类.query.filter_by(条件).all（）
  
  多条件查询
    查询单条数据
        类.query.filter_by(条件).filter_by(条件).....first()
    查询多条数据 
         类.query.filter_by(条件).filter_by(条件).....all（）     
'''
'''
修改数据
    方式一:
        首先查询出来需要的数据
        对查询出来的数据对象进行修改
        提交session
    方式二:
        给定查询条件进行查询后,直接进行update操作
        提交session
'''
'''
删除数据
    方式一：
        查询数据
        对查询出来的数据对象进行删除操作
        提交session
    方式二：
        给定查询条件进行查询后，直接进行delete操作
        提交session
'''