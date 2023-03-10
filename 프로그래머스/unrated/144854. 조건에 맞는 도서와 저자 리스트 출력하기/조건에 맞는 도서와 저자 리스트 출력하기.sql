-- 조건에 맞는 도서와 저자 리스트 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/144854
SELECT L.BOOK_ID, R.AUTHOR_NAME, DATE_FORMAT(L.PUBLISHED_DATE, '%Y-%m-%d') PUBLISHED_DATE
FROM BOOK L
INNER JOIN AUTHOR R
    ON L.AUTHOR_ID = R.AUTHOR_ID
WHERE CATEGORY = '경제'
ORDER BY PUBLISHED_DATE;