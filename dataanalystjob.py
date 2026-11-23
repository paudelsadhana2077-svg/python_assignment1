
required = {"python", "sql", "excel", "statistics"}

applicants = [
    {"name": "Ram", "age": 24, "cgpa": 3.4,
     "skills": {"python", "excel", "html"}},

    {"name": "Sita", "age": 37, "cgpa": 3.8,
     "skills": {"python", "sql", "excel", "statistics"}},

    {"name": "Gita", "age": 26, "cgpa": 3.6,
     "skills": {"python", "sql", "statistics", "tableau"}},

    {"name": "Hari", "age": 29, "cgpa": 2.7,
     "skills": {"sql", "excel", "statistics", "python"}}
]

shortlisted = []
extra_skills = set()

for applicant in applicants:

    name = applicant["name"]
    age = applicant["age"]
    cgpa = applicant["cgpa"]
    skills = applicant["skills"]

    # Find extra skills
    extra_skills.update(skills - required)

    # Check age
    if age < 21 or age > 35:
        print(f"{name}: rejected (age {age})")
        continue

    # Find matching and missing skills
    matched = skills & required
    missing = required - skills

    # Calculate matching percentage
    match_percentage = len(matched) / len(required) * 100

    # Check shortlisting conditions
    if match_percentage >= 75 and cgpa >= 2.5:
        status = "shortlisted"
        shortlisted.append((name, match_percentage, cgpa))
    else:
        status = "not shortlisted"

    print(
        f"{name}: {match_percentage:.0f}% match, "
        f"{status}, missing {sorted(missing)}"
    )

# Sort by match percentage and CGPA
shortlisted.sort(key=lambda x: (x[1], x[2]), reverse=True)

# Get names in interview order
interview_order = [candidate[0] for candidate in shortlisted]

print("Interview order:", interview_order)
print("Extra skills seen (not required):", sorted(extra_skills))
