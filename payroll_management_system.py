#Class 12 IP Project
#Swaroop2sky 

#PYTHON CODE
#👇👇👇👇👇👇👇👇👇👇👇

from sqlalchemy import create_engine

import pandas as pd

import datetime

import subprocess

cnx = create_engine('mysql+pymysql://root:123@localhost:3306/payroll').connect()


def emp_entry():

 ec = eval(input("Enter employee code : "))

 fn = input("Enter First Name of Employee: ")

 ln = input("Enter Last Name of Employee: ")

 dg = input("Enter Designation : ")

 ge=input("Enter Gender : ")

 db = input("Enter Date of Birth : ")

 dj = input("Enter Date of Joining : ")

 mb =input("Enter Mobile Number : ")

 pn =input("Enter PAN Number : ")

 ac= input("Enter Bank Account Number: ")
 fc = input("Enter IFSC code of Bank Account : ")

 sl = eval(input("Enter Pay Level : "))

 bs=eval(input("Enter Basic Salary: "))

 ta=eval(input("Enter Transport Allowance : ")) 

 hr=input("Enter employee is Eligible for HRA Y/N : ")

 np=input("Enter employee is Eligible for NPS Y/N : ") 

 data = [[ec, fn, ln, dg, sl, ge, db, dj, mb, pn, ac, fc,bs,ta,hr,np]]

 df = pd.DataFrame(data,columns=['ecode','fname', 'lname', 'desig', 'level', 

'gender','dob','doj','mob','pan','acno','ifsc','basic','ta','hrayn','npsyn'])

 df.to_sql(name = 'emp', con = cnx, if_exists = 'append', index = False)


def per_setter() :

 dap=eval(input("Enter DA Percentage : "))

 hrp=eval(input("Enter HRA Percentage: ")) 

 data = [[dap,hrp]]

 df = pd.DataFrame(data,columns=['dap','hrap'])

 df.to_sql(name = 'setter', con = cnx, if_exists = 'replace', index = False)
 
 def salary_entry():
  
  while True:
   try:
    y = eval(input("Enter the salary year (press enter for current year otherwise input new year: " + str(datetime.datetime.today().strftime('%Y'))))
   except:
    y = str(datetime.datetime.today().strftime('%Y'))
    break
    
    while True:
    	try:
    		m = eval(input("Enter the salary month (press enter for current month otherwise input new month: " + str(datetime.datetime.today().strftime('%m'))))
    	except:
    		m = str(datetime.datetime.today().strftime('%m'))
    		break

 sql="select * from emp "

 df=pd.read_sql(sql,cnx)

 print("enter salary details for the " + str(m) + "/" + str(y))
 lec=[]

 llevel=[]

 lec = df["ECODE"]

 l1=[]

 ly = []

 lm = []

 allw = []

 deduc = []

 lfee = []

 it = []

 for x in df["ECODE"]:
 	print("Employee Code : " + str(x) + "\n")

 	l1.append(eval(input("Enter No of days worked : ")))

 	allw.append(eval(input("Enter other allowance (or 0): ")))

 	deduc.append(eval(input("Enter other deductions (or 0): ")))

 	it.append(eval(input("Enter income tax to be deducted (or 0): ")))

 	lfee.append(eval(input("Enter other License fee (or 0): ")))

 	ly.append(y)
 	lm.append(m)
 	
 sql="select * from pay"

 df1=pd.read_sql(sql,cnx)

 df1["YEAR"] = ly

 df1["MONTH"] = lm

 df1["ECODE"] = lec

 df1["NODAYS"] = l1

 df1 = pd.merge(df,df1,on='ECODE')

 df1["BASIC"] = df1["BASIC"]/30 * df1["NODAYS"]

 df1["DA"] = df1["BASIC"] * DP/100

 df1["DATA"] = df1["TA"] * DP /100

 df1["HRA"] = df1["TA"] * HP /100

 df1["NPS_M"] = (df1["BASIC"] + df1["DA"] ) * 10 /100

 df1["OTHER_ALLW"] = allw

 df1["GROSS"] = df1["BASIC"] + df1["DA"] + df1["DATA"] + df1["HRA"] + df1["NPS_M"] + df1["OTHER_ALLW"]

 df1["NPS_O"] = df1["NPS_M"]

 df1["GPF"] = df1["BASIC"] * 6/100

 df1["LCFEE"] = lfee
 df1["ITAX"] = it

 df1["ODEDUCT"] = deduc

 df1["TOTAL_DEDUC"] = df1["ITAX"] + df1["NPS_M"] + df1["NPS_O"] + df1["GPF"] + df1["ODEDUCT"] + df1["LCFEE"]

 df1["NETSAL"] = df1["GROSS"] - df1["TOTAL_DEDUC"]

 df1.to_csv('C:\Payroll\SALARY.csv', mode = 'w')

 

def Date_operations():

 x = datetime.datetime.today().strftime('%Y-%m-%d')

 print(x)


def Sdf_show():

 df = pd.read_csv('c:\payroll\salary.csv')

 print(df)


def Show_Rates():

 sql = "select * from setter"

 df = pd.read_sql(sql, cnx)

 print(df)


def Show_EMP():
 sql = "select * from EMP"

 df = pd.read_sql(sql, cnx)

 print(df)


def Salary_show():
 subprocess.call('C:\Program Files\Microsoft Office\Office15\excel c:\payroll\salary.csv')
 
 DP = 0

 HP = 0

 sql="select * from setter"

 df=pd.read_sql(sql,cnx)

 DP = df["dap"][0]

 HP = df["hrap"][0]

 while (True):

  print("1 : Add EMPOYEE DETAILS")

  print("2 : SHOW EMPOYEE DETAILS")

  print("3 : FIX DA AND HRA RATES")
  print("4 : SHOW CURRENT DA AND HRA RATES")

  print("5 : PAYBILL ENTRY ")

  print("6 : SHOW PAYBILL")

  print("7 : SHOW PAYBILL (CSV FILE IN EXCEL)")

  print("8 : Exit")

  choice = int(input("Please Select An Above Option: ")) 

  if(choice == 1):
  	emp_entry()

  elif (choice==2):
  	Show_EMP() 

  elif (choice==3): 

 	 per_setter() 

  elif (choice==4): 

  	Show_Rates()

  elif (choice==5): 

 	 salary_entry()

  elif (choice == 6):

 	 Sdf_show()
  elif (choice == 7):
  	Salary_show()

  elif (choice == 8):
  	break

  else:
 	 print(" Wrong choice..........")