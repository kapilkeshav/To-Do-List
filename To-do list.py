import pandas as pd
import openpyxl


def add_task(task):
    global t_row
    global sno
    global ctr
    t_row.append(task)
    sno.append(ctr+1)
    ctr+=1
    return t_row,sno

def save():
    global writer
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()

sno=[]
t_row=[]
a_row=[]
ctr = 0

df = pd.read_excel("project.xlsx")
n=int(input("How many tasks you want to add? "))

for i in range(n):
    print(f"Add Task {i+1}:")
    add_task(input().title())
    a_row.append('no')
df1 = pd.DataFrame({'Task':t_row,
                    'Status':a_row},index=sno)

writer = pd.ExcelWriter('project.xlsx', engine='openpyxl')  
save()

df.style.hide_index()
print(df1)
while(a_row.count('Yes')!=n):
    comp = int(input("Which Task have you completed? (Enter task no.)"))
    df1.at[comp,'Status']='Yes'
    a_row[comp-1]='Yes'
    df.style.hide_index()
    print(df1)
save()

           




    
