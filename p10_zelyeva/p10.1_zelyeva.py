salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
d1 = list(map(lambda i:round(i*1.3,2),salary_list))
d2 = list(map(lambda i:round(i*0.3,2),salary_list))
print("Salary table:")
for i in range(0,len(salary_list)):
    print(salary_list[i],d1[i],d2[i])
