import pandas as pd

def load_data():
    
    dep_info = pd.read_csv("csv\\Department_Information.csv")
    emp_info = pd.read_csv("csv\\Employee_Information.csv")
    student_info = pd.read_csv("csv\\Student_Counceling_Information.csv")

    dep_info['DOE'] = pd.to_datetime(dep_info['DOE'])
    emp_info.rename(columns = {'Employee ID':'Employee_ID'}, inplace = True)
    emp_info['DOB'] = pd.to_datetime(emp_info['DOB'])
    emp_info['DOJ'] = pd.to_datetime(emp_info['DOJ'])
    student_info['DOB'] = pd.to_datetime(student_info['DOB'])
    student_info['DOA'] = pd.to_datetime(student_info['DOA'])

    dep_info.drop([6,8,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39],axis = 'index', inplace = True)
    dep_info.loc[5, 'Department_Name'] = 'Computer Science and Engineering'
    dep_info.loc[9, 'Department_Name'] = 'Humanities and Social Science'
    dep_info.loc[12, 'Department_Name'] = 'Metallurgical Engineering'
    dep_info.loc[20, 'Department_Name'] = 'Environmental Science and Engineering'
    dep_info.index = range(len(dep_info))

    l = []

    for i in range(0,len(dep_info)):
        l.append(dep_info.loc[i, 'Department_ID'])

    for i in range(0,len(emp_info)):
        if emp_info.loc[i, 'Department_ID'] not in l:
            emp_info.drop(i, axis = 0, inplace = True)
    
    emp_info.index = range(len(emp_info))

    for i in range(0,len(student_info)):
        if student_info.loc[i, 'Department_Admission'] not in l:
            student_info.drop(i, axis = 0, inplace = True)
    
    student_info.index = range(len(student_info))

    for i in range(0,len(student_info)):
        if student_info.loc[i, 'Department_Choices'] not in l:
            student_info.drop(i, axis = 0, inplace = True)

    student_info.index = range(len(student_info))

    student_info.drop_duplicates(inplace = True)

    return dep_info, emp_info, student_info