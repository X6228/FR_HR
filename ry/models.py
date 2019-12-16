from django.db import models

#人员基本信息
class Person(models.Model):
    Id_Number = models.CharField(max_length=30,verbose_name="身份证号")           #身份证号
    Name = models.CharField(max_length=20,verbose_name="姓名")                    #姓名
    Gender = models.CharField(max_length=4,verbose_name="性别",blank=True)                   #性别
    Nation = models.CharField(max_length=4,verbose_name="民族",blank=True)                  #民族
    Birthday = models.DateField(verbose_name="出生年月",blank=True,null=True)                           #出生年月
    WorkTime = models.DateField(verbose_name="参加工作时间",blank=True,null=True)                       #参加工作时间
    Marital_Stauts = models.CharField(max_length=8,verbose_name="婚姻状况",blank=True)     #婚姻状况
    Native_Place = models.CharField(max_length=20,verbose_name="籍贯",blank=True)      #籍贯
    Politial_Stauts = models.CharField(max_length=20,blank=True,verbose_name="政治面貌")   #政治面貌
    Personal_Stauts = models.CharField(max_length=20,blank=True,verbose_name="个人身份")   #个人身份
    Phone_Number = models.CharField(max_length=20,blank=True,verbose_name="电话号码")      #电话号码
    Work_Unit = models.CharField(max_length=100,blank=True,verbose_name="所在单位")        #所在单位
    Work_Stauts = models.CharField(max_length=8,blank=True,verbose_name="在岗状态")        #在岗状态
    Photo = models.ImageField(upload_to='photo',verbose_name='近照',default="/static/photo/nophoto.jpg")                        #照片 
    Freely1 = models.CharField(max_length=8,blank=True)            #备用字段1
    Freely2 = models.CharField(max_length=8,blank=True)            #备用字段2
    Freely3 = models.CharField(max_length=8,blank=True)            #备用字段3

    def __str__(self):
        return f"{self.Name}(身份证号:{self.Id_Number})"

#学习经历
class Study(models.Model):
    Id_Number = models.CharField(max_length=30,verbose_name="身份证号")         #身份证号
    Begin_Date = models.DateField(verbose_name="开始时间")                     #开始时间
    Finish_Date = models.DateField(blank=True,null=True,verbose_name="毕业时间")                    #毕业时间
    Education = models.CharField(max_length=8,verbose_name="学历层次")          #学历层次
    Degree = models.CharField(max_length=8,verbose_name="学位")             #学位
    School = models.CharField(max_length=100,verbose_name="毕业学校")           #毕业学校
    Major = models.CharField(max_length=30,verbose_name="所学专业")             #所学专业
    Modality = models.CharField(max_length=30,verbose_name="学习形式")          #学习形式

    def __str__(self):
        return self.Id_Number
    
#工作经历
class Experience(models.Model):
    Id_Number = models.CharField(max_length=30,verbose_name="身份证号")         #身份证号
    Begin_Date = models.DateField(verbose_name="开始时间")                     #开始时间
    Finish_Date = models.DateField(verbose_name="结束时间")                    #结束时间
    Work_Unit = models.CharField(max_length=50,verbose_name="工作单位")         #工作单位
    Position = models.CharField(max_length=20,verbose_name="职务（岗位）")          #职务（岗位）
    Pay_Family = models.CharField(max_length=20,verbose_name="工资结构")        #工资结构
    Pay_Level = models.CharField(max_length=20,verbose_name="待遇层次")         #待遇层次


#年度考核
class Appraise(models.Model):
    Id_Number = models.CharField(max_length=30,verbose_name="身份证号")         #身份证号
    Year = models.DateField(verbose_name="考核年度")                           #考核年度
    Grade = models.CharField(max_length=8,verbose_name="考核结果")              #考核结果
    Remarks = models.CharField(max_length=100,verbose_name="备注")          #备注

#家庭成员
class Family(models.Model):
    Id_Number = models.CharField(max_length=30,verbose_name="身份证号")         #身份证号
    Relation = models.CharField(max_length=8,verbose_name="关系")           #关系
    Name = models.CharField(max_length=20,verbose_name="姓名")              #姓名
    Birthday = models.DateField(verbose_name="出生年月")                       #出生年月
    Remarks = models.CharField(max_length=100,verbose_name="备注")          #备注

#备注
class Comments(models.Model):
    Id_Number = models.CharField(max_length=30,verbose_name="身份证号")         #身份证号
    Remarks = models.CharField(max_length=100,verbose_name="备注")          #备注

