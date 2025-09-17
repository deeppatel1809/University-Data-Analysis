import pandas as pd
import matplotlib.pyplot as plt
import pytz
import os

def perform_all_analyses(departments, employees, counseling):

    if not os.path.exists('static/charts'):
        os.makedirs('static/charts')

    # 1 Employee Distribution
    
    employees_count_dict = dict()
    for i in range(len(departments)):
        employee_count = 0
        for j in range(len(employees)):
            if employees.loc[j, 'Department_ID'] == departments.loc[i, 'Department_ID']:
                employee_count += 1
        employees_count_dict[departments.loc[i, 'Department_Name']] = employee_count

    plt.bar(employees_count_dict.keys(), employees_count_dict.values())
    plt.xlabel('Department Name')
    plt.ylabel('Employee Count')
    plt.title('Employee Distribution Across Departments')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.tight_layout()
    plt.savefig('static/charts/employee_distribution.png')
    plt.clf()
    
    # 2 Employee Age
    
    today = pd.Timestamp.now(pytz.UTC)
    employees["Age"] = (today - employees["DOB"]).dt.days // 365

    age_groups = pd.cut(employees["Age"], bins=[20, 35, 50, 65], labels=["20-35", "35-50", "50-60"])
    age_group_counts = age_groups.value_counts()
    
    plt.pie(age_group_counts, labels=age_group_counts.index, autopct='%1.1f%%')
    plt.title('Employee Age Group Distribution')
    plt.tight_layout()
    plt.savefig('static/charts/employee_age_distribution.png')
    plt.clf()

    # 3 Employee Experience

    employees["Experience"] = (today - employees["DOJ"]).dt.days // 365

    plt.scatter(employees["Age"], employees["Experience"], color='red')
    plt.xlabel('Age')
    plt.ylabel('Experience')
    plt.title('Age vs. Experience of Employees')
    plt.tight_layout()
    plt.savefig('static/charts/age_vs_experience.png')
    plt.clf()

    # 4 Student Admissions by year

    counseling['Year'] = counseling['DOA'].dt.year
    department_id_to_name = departments.set_index('Department_ID')['Department_Name'].to_dict()
    counseling['Department_Name'] = counseling['Department_Admission'].map(department_id_to_name)
    admissions_by_dept = counseling.groupby(['Year', 'Department_Name']).size().unstack(fill_value=0)

    total_admissions_by_year = admissions_by_dept.sum(axis=1)
    plt.plot(total_admissions_by_year.index, total_admissions_by_year, label='Total Admissions', color='red')
    plt.xlabel('Year')
    plt.ylabel('Number of Admissions')
    plt.title('Total Student Admissions by Year')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig('static/charts/total_student_admissions_by_year.png')
    plt.clf()

    # 5 Student Admissions by Department

    counseling['Year'] = counseling['DOA'].dt.year
    department_id_to_name = departments.set_index('Department_ID')['Department_Name'].to_dict()
    counseling['Department_Name'] = counseling['Department_Admission'].map(department_id_to_name)
    admissions_by_dept = counseling.groupby(['Year', 'Department_Name']).size().unstack(fill_value=0)

    imgUrls = []

    for dept in admissions_by_dept.columns:
        plt.plot(admissions_by_dept.index, admissions_by_dept[dept], label=dept, color='green')
        plt.xlabel('Year')
        plt.ylabel('Number of Admissions')
        plt.title('Student Admissions Across Department')
        plt.legend(title='Department')
        plt.grid()
        plt.tight_layout()
        plt.savefig(f'static/charts/student_admissions_by_department_{dept.replace(" ","")}.png')
        plt.clf()
        imgUrls.append(f'static/charts/student_admissions_by_department_{dept.replace(" ","")}.png')

    # 6 Course Popularity
    
    course_popularity = counseling['Department_Admission'].value_counts()
    course_popularity.index = course_popularity.index.map(department_id_to_name)
    plt.figure(figsize=(10,6))
    plt.pie(course_popularity, labels=course_popularity.index, autopct='%1.1f%%')
    plt.title('Course Popularity')
    plt.tight_layout()
    plt.savefig('static/charts/course_popularity.png')
    plt.clf()

    # 7 Total Admissions by Department

    addmissions_by_dept = counseling['Department_Admission'].value_counts()
    addmissions_by_dept.index = addmissions_by_dept.index.map(department_id_to_name)
    
    plt.bar(addmissions_by_dept.index, addmissions_by_dept.values)
    plt.xlabel('Department Name')
    plt.ylabel('Number of Admissions')
    plt.title(' Total Admissions Across Departments')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.tight_layout()
    plt.savefig('static/charts/total_admissions_by_department.png')
    plt.clf()

    # 8 Student-Teacher Ratio by Department

    student_count_by_dept = counseling['Department_Admission'].value_counts()
    student_count_by_dept.index = student_count_by_dept.index.map(department_id_to_name)
    
    teacher_count_by_dept = employees['Department_ID'].map(department_id_to_name).value_counts()
    
    student_teacher_ratio = student_count_by_dept / teacher_count_by_dept

    plt.bar(student_teacher_ratio.index, student_teacher_ratio.values, color='purple')
    plt.xlabel('Department Name')
    plt.ylabel('Student-Teacher Ratio')
    plt.title('Student-Teacher Ratio by Department')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.tight_layout()
    plt.savefig('static/charts/student_teacher_ratio_by_department.png')
    plt.clf()

    # 9 Gender ratio of students

    gender_counts_by_dept = counseling.groupby(['Department_Admission', 'Gender']).size().unstack(fill_value=0)
    gender_counts_by_dept = gender_counts_by_dept[['Male', 'Female']]
    gender_counts_by_dept.index = gender_counts_by_dept.index.map(department_id_to_name)
    
    gender_ratio_by_dept = gender_counts_by_dept.div(gender_counts_by_dept.sum(axis=1), axis=0)

    gender_ratio_by_dept.plot(kind='barh', stacked=True, figsize=(10,6), color=['blue', 'pink'])
    plt.xlabel('Gender Ratio')
    plt.ylabel('Department Name')
    plt.title('Gender Ratio of Students Across Departments')
    plt.legend(title='Gender')
    plt.tight_layout()
    plt.savefig('static/charts/gender_ratio_by_department.png')
    plt.clf()

    # 10 top couseses list according to admissions

    top_courses = counseling['Department_Admission'].value_counts()
    top_courses.index = top_courses.index.map(department_id_to_name)
    
    top_courses_df = pd.DataFrame({
        'sr': [i+1 for i in range(len(top_courses))],
        'Department_Name': top_courses.index,
    })

    # 11 Additional textual analyses

    avg_age = employees["Age"].mean().round(2)
    avg_experience = employees["Experience"].mean().round(2)

    highest_admissions_dept = addmissions_by_dept.idxmax()
    lowest_admissions_dept = addmissions_by_dept.idxmin()

    overall_gender_distribution = gender_counts_by_dept.sum()

    textual_analysis = {
        "avg_age": avg_age,
        "avg_experience": avg_experience,
        "highest_admissions_dept": highest_admissions_dept,
        "lowest_admissions_dept": lowest_admissions_dept,
        "overall_gender_distribution": overall_gender_distribution,
    }

    # 12 Student Choices vs Admissions

    student_choices = counseling['Department_Choices'].value_counts()
    student_choices.index = student_choices.index.map(department_id_to_name)

    student_choices_vs_admissions = pd.DataFrame({
        'Department_Name': student_choices.index,
        'Choices_Count': student_choices.values,
        'Admissions_Count': addmissions_by_dept.reindex(student_choices.index).values
    })

    student_choices_vs_admissions.set_index('Department_Name', inplace=True)

    student_choices_vs_admissions.plot(kind='bar')
    plt.xlabel('Department Name')
    plt.ylabel('Count')
    plt.title('Student Choices vs Admissions')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.tight_layout()
    plt.savefig('static/charts/student_choices_vs_admissions.png')
    plt.clf()

    return imgUrls,top_courses_df,textual_analysis