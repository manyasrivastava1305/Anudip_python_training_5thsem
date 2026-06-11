# Student enrollment data for university courses is stored below. 
# Sample Data 
# enrollment = { 
#     "Python": 45, 
#     "Java": 38, 
#     "Data Science": 52, 
#     "Web Development": 34, 
#     "Machine Learning": 41, 
#     "Cloud Computing": 29, 
#     "Cyber Security": 33, 
#     "DBMS": 48, 
#     "Networking": 26, 
# } 
# "Operating Systems": 37 
# Tasks 
# 1. Display courses having more than 40 enrollments.  
# 2. Find the most and least popular courses.  
# 3. Calculate total enrollments.  
# 4. Create lists:  
# o High Demand (>40)  
# o Medium Demand (30–40)  
# o Low Demand (<30)  
# 5. Count courses requiring promotional activities (<35 enrollments). 
# Sample Data (Fixed syntax to properly include Operating Systems inside the dictionary)
enrollment = { 
    "Python": 45, 
    "Java": 38, 
    "Data Science": 52, 
    "Web Development": 34, 
    "Machine Learning": 41, 
    "Cloud Computing": 29, 
    "Cyber Security": 33, 
    "DBMS": 48, 
    "Networking": 26, 
    "Operating Systems": 37 
}

# --- Validation: Ensure the enrollment dataset is not empty ---
if not enrollment:
    print("Error: Enrollment database is empty! Cannot perform analysis.")
else:
    # 1. Display courses having more than 40 enrollments
    print("Courses with more than 40 enrollments:")
    has_popular_courses = False
    for course, count in enrollment.items():
        if count > 40:
            print(course, "-", count, "students")
            has_popular_courses = True
            
    if not has_popular_courses:
        print("None")
    print("-" * 40)

    # 2. Find the most and least popular courses
    # Finding the specific keys (Course Names) safely using max and min
    most_popular = max(enrollment, key=enrollment.get)
    least_popular = min(enrollment, key=enrollment.get)
    
    print("Most Popular Course:", most_popular, "with", enrollment[most_popular], "students")
    print("Least Popular Course:", least_popular, "with", enrollment[least_popular], "students")
    print("-" * 40)

    # 3. Calculate total enrollments
    total_enrollments = sum(enrollment.values())
    print("Total University Enrollments:", total_enrollments, "students")
    print("-" * 40)

    # 4. Create demand lists
    high_demand = []
    medium_demand = []
    low_demand = []
    
    for course, count in enrollment.items():
        # Input Validation: Skip invalid or negative enrollment numbers if they exist
        if count < 0:
            print("Validation Warning: Negative enrollment found for", course, "- Skipped!")
            continue
            
        if count > 40:
            high_demand.append(course)
        elif count >= 30:
            medium_demand.append(course)
        else:
            low_demand.append(course)
            
    print("High Demand Courses:", high_demand)
    print("Medium Demand Courses:", medium_demand)
    print("Low Demand Courses:", low_demand)
    print("-" * 40)

    # 5. Count courses requiring promotional activities (<35 enrollments)
    promo_count = 0
    for count in enrollment.values():
        if count < 35:
            promo_count += 1
            
    print("Number of courses requiring promotional activities:", promo_count)
