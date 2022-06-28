'''
ORM
什么是持久化（Persistence）
    把数据保存到可永久保存的存储设备中（如磁盘）。持久化的主要应用是将内存中的数据存储在关系型的数据库中欧冠，当然也可以存储在磁盘文件中，xml数据文件中等等。
什么是ORM
    Object Relational Mapping 对象关系映射
    作用是在关系型数据库和对象之前做一个映射，这样在具体操作数据库的时候，就不需要再去和复杂的SQL语句打交道，只需要像平时操作对象一样就可以了
ORM与SQL的对比
    数据库的每一行数据都想相当于user类的一个实例
    -----sql-----
    sql="select username,email,gender FROM User WHERE id =1"
    res=db.execSql(sql)
    name =res[0]
    ----ORM----
    #使用orm查询数据，定义ORM、对象，get值
    res = db.session.query(User.username,User.email,User.gender) filter (User.id=1).firsr()
    name=res.username
ORM优缺点
    优点
        隐藏了数据访问细节
        ORM使我们构造固化数据结构变得非常简单
    缺点
        性能下降，添加了关联操作，性能不可避免的会下降一些
        无法解决特别复杂的数据库操作
'''