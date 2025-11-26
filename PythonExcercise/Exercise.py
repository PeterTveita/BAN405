import time
from idlelib.configdialog import changes


def convert_and_print_time():
    total_seconds = time.time()
    days = total_seconds // (24 * 3600)
    seconds_remaining = total_seconds % (24 * 3600)
    hours = seconds_remaining // 3600
    seconds_remaining %= 3600
    minutes = seconds_remaining // 60
    seconds = seconds_remaining % 60
    print(f"Total seconds since the epoch: {total_seconds}")
    print(f"Days since the epoch: {int(days)}")
    print(f"Hours since the epoch: {int(hours)}")
    print(f"Current time of day: {int(hours)}:{int(minutes)}:{seconds:.2f}")

def round_scores(student_scores):
    return [round(score) for score in student_scores]
student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
rounded_scores = round_scores(student_scores)


def count_failed_students(student_scores1):
    count = 0
    for score in student_scores1:
        if score <= 40:
            count += 1
    return count
    # To run code:
    # print(f"{count_failed_students(student_scores)} students failed the test")
student_scores1 = [90,40,55,70,30,25,80,95,38,40]

def above_threshold(student_scores2, threshold):
    count = 0
    for score in student_scores2:
        if score >= threshold:
            count += 1
    return count

student_scores2 = [90,40,55,70,30,68,70,75,83,96]
best_students = above_threshold(student_scores2, 75)
    # To run code:
    # print(f"{best_students} students are above the threshold")
    # Or:
    # print(f"{above_threshold(student_scores2, 75)} students are above the threshold")

def letter_grades(highest):
    points_to_distribute = highest - 40
    interval_size = points_to_distribute // 4

    d_threshold = 41
    c_threshold = 41 + interval_size
    b_threshold = 41 + 2 * interval_size
    a_threshold = 41 + 3 * interval_size

    return [d_threshold, c_threshold, b_threshold, a_threshold]

print(letter_grades(highest=100))