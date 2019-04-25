SELECT student.name,
  (SELECT course.language
   FROM course
   WHERE course.id =
       (SELECT student_to_course.course_id
        FROM student_to_course
        WHERE student_to_course.student_id == student.id
        LIMIT 1) )
FROM student;

/*
1. Най-външната заявка:
	```
	SELECT student.name, <subquery>
		FROM student;
	```
    => Взима "име на студента" + резултата от subquery-то

2. Първата подзаявка:
	```
	SELECT course.language
	FROM course
	WHERE course.id = <subquery>
	```
	=> Взима името на езика, на реда, където id-то на курса е равно на резултата от най-вътрешната заявка
	
3. Най-вътрешната заявка:
	```
	SELECT student_to_course.course_id
		FROM student_to_course
		WHERE student_to_course.student_id == student.id
		LIMIT 1
	```
	=> Взима id-тата на курса от student_to_course таблицата, там където id-то на студента е същото като id-то на студента от най-външната заявка като ще вземе максимум 1 резултат (LIMIT 1).
		С други думи взимаме id-то на курса първият срещнат student_to_course запис за този студент.
*/
