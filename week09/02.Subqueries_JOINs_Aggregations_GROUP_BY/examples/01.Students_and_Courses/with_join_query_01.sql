SELECT student.name, course.language, course.year
	FROM student
	LEFT OUTER JOIN student_to_course
		ON student.id == student_to_course.student_id
	LEFT OUTER JOIN course
		ON course.id == student_to_course.course_id;

/*
    Взима ВСИЧКИ редове от таблицата `student` (`SELECT ... FROM student`)
    обединена с `student_to_course`, на база на колоната `id` от таблицата `student` и колоната `student_id` от таблицата `student_to_course` (LEFT OUTER JOIN ... ON ...)
    обединена с course, на база на колоната `course.id` от таблицата `student_to_course` и колоната `id` от таблицата `course` (LEFT OUTER JOIN ... ON ...)
*/
