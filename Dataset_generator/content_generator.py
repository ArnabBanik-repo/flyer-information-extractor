import random
from nltk.corpus import brown, reuters, gutenberg
import os
speaker_folder_path = 'dataset/speakers'
speaker_images = os.listdir(speaker_folder_path)

# Sample data for each category
type_of_lecture = ["6th Module Workshop", "3rd Module Seminar", "10th Module Conference", "4th Module Webinar", "2nd Module Symposium",
                   "5th Module Panel Discussion", "7th Module Colloquium", "9th Module Roundtable", "1st Module Keynote Address", "8th Module Lecture Series"]
lecture_titles = ["Introduction to Data Science", "Machine Learning Applications in Finance", "Advancements in Computer Vision", "Deep Learning in Healthcare",
                  "Natural Language Processing Techniques", "Robotics and Automation", "Big Data Analytics", "Cybersecurity and Threat Intelligence",
                  "Blockchain Technology Overview", "Cloud Computing Fundamentals", "Artificial Intelligence in Robotics", "Data Mining Techniques",
                  "Computer Networks and Security", "Software Engineering Principles", "Operating Systems Fundamentals"]
resource_person_names = ["Alisha Gupta", "Rahul Sharma", "Priya Singh", "Sandeep Patel",
                         "Neha Shah", "Ankit Joshi", "Shreya Mehta", "Vivek Kumar", "Kavita Singh", "Ravi Sharma"]
designations = ["Data Scientist", "Research Scientist", "AI Engineer", "Software Developer", "Data Analyst", "Machine Learning Specialist", "Cybersecurity Analyst",
                "Cloud Architect", "Blockchain Developer", "Full Stack Developer"]
company_names = ["Google", "Microsoft", "Amazon", "IBM",
                 "Facebook", "Apple", "Intel", "Oracle", "Cisco", "Adobe"]
cities = ["New York, USA", "Tokyo, Japan", "Berlin, Germany", "London, UK", "Paris, France", "Seoul, South Korea", "Sydney, Australia",
          "Toronto, Canada", "Mumbai, India", "Dubai, UAE", "Bengaluru, India", "Delhi, India", "Chennai, India", "Hyderabad, India"]
course_codes = ["BCD" + str(random.randint(1000, 9999)) for _ in range(10)] + [
    "CSE" + str(random.randint(1000, 9999)) for _ in range(10)]
course_titles = ["Introduction to Python Programming", "Advanced Data Analysis", "Deep Learning Fundamentals", "Data Visualization Techniques",
                 "Natural Language Processing Fundamentals", "Database Management Systems", "Information Security Principles", "Software Engineering Principles",
                 "Internet of Things Applications", "Parallel and Distributed Computing", "Cloud Computing Technologies", "Machine Learning Fundamentals",
                 "Computer Vision and Image Processing", "Cybersecurity Fundamentals", "Web Development Principles"]
dates = ["15th November, 2023", "3rd December, 2023", "21st January, 2024", "9th March, 2024", "6th May, 2024", "18th June, 2024", "27th August, 2024",
         "12th October, 2024", "8th December, 2024", "25th January, 2025"]
times = ["4:00 PM to 6:00 PM", "10:00 AM to 12:00 PM", "2:00 PM to 4:00 PM", "8:00 AM to 10:00 AM", "1:00 PM to 3:00 PM", "6:00 PM to 8:00 PM", "11:00 AM to 1:00 PM",
         "3:00 PM to 5:00 PM", "9:00 AM to 11:00 AM", "5:00 PM to 7:00 PM"]

modes = []
online_platforms = ["MS Teams", "Zoom", "Google Meet", "Skype", "Cisco Webex"]
codes = [chr(random.randint(97, 123))*2+chr(random.randint(65, 91))
         * 2+chr(random.randint(48, 58))] * 10
venues = []
for i in range(101, 127):
    venues.append(f"SJT{i}")
    venues.append(f"SJT{i + 100}")
    venues.append(f"SJT{i + 200}")
    venues.append(f"SJT{i + 300}")
    venues.append(f"SJT{i + 400}")
    venues.append(f"SJT{i + 500}")

for i in range(6):
    modes.append("Mode: Online (" + random.choice(online_platforms) +
                 ") - https://shorturl.at/"+random.choice(codes))
for i in range(6):
    modes.append("Venue: "+random.choice(venues))

# Variable size array for coordinators
coordinators = [
    ["Dr. Anjali M.", "Dr. Amit Kumar", "Dr. Priya Singh"],
    ["Dr. Rajesh Sharma", "Dr. Smita Patel", "Dr. Ravi Kapoor", "Dr. Seema Gupta"],
    ["Dr. Sanjay Singh", "Dr. Reena Gupta", "Dr. Meera Sharma",
        "Dr. Vikas Verma", "Dr. Nidhi Patel"],
    ["Dr. Ankit Mehta", "Dr. Aruna Saxena"],
    ["Dr. Ajay Kumar", "Dr. Neha Sharma", "Dr. Rahul Singh", "Dr. Ananya Roy"],
    ["Dr. Vikram Singh", "Dr. Komal Gupta", "Dr. Ritu Sharma",
        "Dr. Manish Kumar", "Dr. Neeraj Jain"],
    ["Dr. Suresh Mehta", "Dr. Raghav Kapoor", "Dr. Tanvi Sharma"],
    ["Dr. Anamika Singh", "Dr. Sanjeev Kumar",
        "Dr. Nisha Gupta", "Dr. Rajat Mehta"],
    ["Dr. Vivek Gupta", "Dr. Aarti Kapoor", "Dr. Rakesh Sharma"],
    ["Dr. Preeti Singh", "Dr. Karan Mehta", "Dr. Puja Sharma", "Dr. Mohan Kapoor"]
]

# common content
logo = "Logo-vit_logo.jpg"
l1 = "School of Computer Science and Engineering (SCOPE)"
l2 = "Cordially invites you all for"
l3 = "on"
l4 = "by"
l5 = "All are invited"
l6 = " Dr. Umadevi K S      Dr. Ananda Kumar S     Dr. K. Ramesh Babu"
l7 = "HOD – Dept of SS       HOD – Dept of CI         Dean – SCOPE"

# Generate new description
def get_random_sentence_with_name(corpus):
    sentence_set = corpus.sents()
    sentences = [' '.join(sentence) for sentence in sentence_set]
    relevant_sentences = [sent for sent in sentences if ((len(sent.split()) >= 8 and len(sent.split()) < 15) and sent[len(sent)-1]=='.' and sent[0].isupper())]
    return random.choice(relevant_sentences) if relevant_sentences else None

def create_new_description():
    random_paragraph = ""
    random_word_limit = [80,85,90,95,100]
    while len(random_paragraph.split()) < random.choice(random_word_limit):
        random_corpus = random.choice([brown, reuters, gutenberg])
        random_sentence = get_random_sentence_with_name(random_corpus)
        if random_sentence:
            # print(random_sentence)
            random_paragraph += random_sentence + " "
    return random_paragraph

# Generate random content for each category
def random_data():
    random_type_of_lecture = random.choice(type_of_lecture)
    random_lecture_title = random.choice(lecture_titles)
    random_resource_person_name = random.choice(resource_person_names)
    random_designation = random.choice(designations)
    random_company_name = random.choice(company_names)
    random_city = random.choice(cities)
    random_course_code = random.choice(course_codes)
    random_course_title = random.choice(course_titles)
    random_date = random.choice(dates)
    random_time = random.choice(times)
    random_mode = random.choice(modes)
    random_coordinators = random.choice(coordinators)
    speaker = "Speaker-dataset/speakers/"+random.choice(speaker_images)
    # print(speaker)
    description = create_new_description()
    new_data = [logo, l1, l2, random_type_of_lecture, l3, "\""+random_lecture_title+"\"",
                l4, random_resource_person_name, random_designation, random_company_name, random_city, speaker, description, random_course_code +
                " - "+random_course_title, "Date: "+random_date, "Time: "+random_time, random_mode, l5, "Faculty Coordinators: "+", ".join(random_coordinators[:len(
                    random_coordinators)-1])+" and ", random_coordinators[-1:][0], l6, l7]
    for i in range(len(new_data)):
        new_data[i] = new_data[i]+"\n"
    return new_data



# description = "Utkarsh is an ML engineer working in the Research and Development team of Qualcomm. He is an M.Tech graduate and gold medalist from the prestigious Indian Institute of Science, Bengaluru. Utkarsh has worked on several projects in the area of AI/ML and published high quality publications based on research carried out. At Qualcomm, he has been working on state of the art computer vision and NLP models, analyzing the architecture of these models for optimising them to give better performance on Qualcomm products."