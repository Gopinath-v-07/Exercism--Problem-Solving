def round_scores(student_scores):
    output=[]
    for i in student_scores:
     if i :
        output.append(round(i))
    return output

    


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    count=0
    for i in student_scores:
        if i <=40:
            count+=1
    return count

    pass


def above_threshold(student_scores, threshold):

    return [score for score in student_scores if score >= threshold]
       
        

    pass


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - letter grade intervaof lower threshold scores for each D-A l.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    step = (highest - 40) // 4
    
    d = 41
    c = d + step
    b = c + step
    a = b + step
    
    return [d, c, b, a]


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    result=[]
    for i in range(len(student_scores)):
        rank=i+1
        result.append(f"{rank}. {student_names[i]}: {student_scores[i]}")
    return result
        
        
              

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    
    for student in student_info:
        if student[1] == 100:
            return student
    return []

    pass
