import re
from collections import Counter

# --- Sample Resume Text ---
resume_text = """
Name: Amit Kumar
Email: amit.kumar2026@email.com, amit.work@gmail.com
Phone: +91-98765-43210, 555-019-2834
Education: B.Tech in Computer Science
Skills: Python, Java, SQL, Python, JavaScript, HTML, SQL, Git
Projects: Developed an AI Chatbot using Python and SQL. Built a Web App with HTML and JavaScript.
Achievements: Coding Competition Winner, Certified in Java.
"""

# Pre-processing text for keyword analysis
# Removes punctuation and converts to lowercase to get accurate word counts
clean_text = re.sub(r'[^\w\s,]', '', resume_text)
words_list = clean_text.lower().split()

# --- Task 1 & 2: Count total words and characters ---
total_words = len(resume_text.split())
total_characters = len(resume_text)

# --- Task 3 & 4: Extract email IDs and phone numbers using regex ---
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'[\d\s+-]{10,}'

emails = re.findall(email_pattern, resume_text)
# Clean up extracted phone strings to filter out empty spaces/formatting noise
phones = [p.strip() for p in re.findall(phone_pattern, resume_text) if len(p.strip()) >= 10]

# --- Task 5, 8 & 9: Skill processing from the Skills section ---
# Isolate the skills line to process accurately
skills_line = ""
for line in resume_text.strip().split('\n'):
    if line.startswith("Skills:"):
        skills_line = line.replace("Skills:", "")

# Clean and split skills into a list
all_skills = [skill.strip() for skill in skills_line.split(',') if skill.strip()]
total_skills_count = len(all_skills)

# Generate skill frequency report
skill_report = dict(Counter(all_skills))

# Detect duplicate skills
duplicate_skills = list(set([skill for skill in all_skills if all_skills.count(skill) > 1]))

# --- Task 6 & 7: Keyword repetition analysis ---
word_counts = Counter(words_list)
# Filtering out common short filler words for meaningful keyword analysis
filler_words = {'in', 'an', 'using', 'and', 'with', 'a', 'to', 'of', 'for', 'at'}
meaningful_word_counts = {w: c for w, c in word_counts.items() if w not in filler_words and len(w) > 1}

# Find repeated keywords (appearing more than once)
repeated_keywords = {w: c for w, c in meaningful_word_counts.items() if c > 1}

# Identify the most frequently used word
most_frequent_word = max(meaningful_word_counts, key=meaningful_word_counts.get) if meaningful_word_counts else "None"
most_frequent_count = meaningful_word_counts.get(most_frequent_word, 0)

# --- Task 10: Summary Dashboard Display ---
print("==================================================")
print("           RESUME PARSER DASHBOARD                ")
print("==================================================")
print(f"1. Total Words:             {total_words}")
print(f"2. Total Characters:        {total_characters}")
print(f"3. Extracted Email IDs:     {emails}")
print(f"4. Extracted Phone Numbers: {phones}")
print(f"5. Total Skills Mentioned:  {total_skills_count}")
print(f"6. Repeated Keywords:       {repeated_keywords}")
print(f"7. Most Frequent Word:      '{most_frequent_word}' ({most_frequent_count} times)")
print(f"8. Skill Frequency Report:  {skill_report}")
print(f"9. Duplicate Skills Found:  {duplicate_skills}")
print("==================================================")