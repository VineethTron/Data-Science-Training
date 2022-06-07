
import pandas as pd
student_data = {"Student1":{"Name":"Vineeth", "StudentID":"19881A0550","SSC":"10.0", "INTER":"987","B-TECH":"9.27","PL":"JAVA","CareerOption":"MS"},
                "Student2":{"Name":"Sai", "StudentID":"19881A0530","SSC":"10.0", "INTER":"980","B-TECH":"9.0","PL":"Python","CareerOption":"JOB"},
                "Student3":{"Name":"Nikitha", "StudentID":"19881A0523","SSC":"10.0", "INTER":"985","B-TECH":"9.38","PL":"C","CareerOption":"START-UP"},
                "Student4":{"Name":"Saleem", "StudentID":"19881A0546","SSC":"9.8", "INTER":"970","B-TECH":"9.02","PL":"C++","CareerOption":"MS"},
                "Student5":{"Name":"Harsha", "StudentID":"19881A0544","SSC":"9.8", "INTER":"950","B-TECH":"9.33","PL":"R","CareerOption":"MS"},
                "Student6":{"Name":"Ramya", "StudentID":"19881A0521","SSC":"10.0", "INTER":"986","B-TECH":"9.10","PL":"JAVA","CareerOption":"JOB"},
                "Student7":{"Name":"AbhiRam", "StudentID":"19881A05G2","SSC":"9.8", "INTER":"975","B-TECH":"9.03","PL":"JAVA","CareerOption":"JOB"},
                "Student8":{"Name":"Prem", "StudentID":"19881A0268","SSC":"10.0", "INTER":"979","B-TECH":"9.11","PL":"Python","CareerOption":"MS"},
                "Student9":{"Name":"Siva", "StudentID":"19881A0299","SSC":"10.0", "INTER":"960","B-TECH":"9.44","PL":"JS","CareerOption":"JOB"},
                "Student10":{"Name":"Karan", "StudentID":"19881A0555","SSC":"10.0", "INTER":"900","B-TECH":"9.65","PL":"Perl","CareerOption":"MS"},
                }
dt = pd.DataFrame(student_data)
print(dt)

for student in student_data.items() :
    print(student,end="\n")