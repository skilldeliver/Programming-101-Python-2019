SELECT student.name, course.language, course.year
	FROM student
	INNER JOIN student_to_course
		ON student.id == student_to_course.student_id
	INNER JOIN course
		ON course.id == student_to_course.course_id;

/*
    Взима редовете от таблицата `student` (`SELECT ... FROM student`) - само редовете, за които са изпълнени условията (и никое от полетата в JOIN-овете не е null)
    обединена с `student_to_course`, на база на колоната `id` от таблицата `student` и колоната `student_id` от таблицата `student_to_course` (INNER JOIN ... ON ...)
    обединена с course, на база на колоната `course.id` от таблицата `student_to_course` и колоната `id` от таблицата `course` (INNER JOIN ... ON ...)
*/
