# https://stackoverflow.com/questions/9122/select-all-columns-except-one-in-mysql
# SET @sql = CONCAT(
#     'SELECT ', (
#         SELECT REPLACE(
#             GROUP_CONCAT(
#                 COLUMN_NAME
#             ), 'TLNO,', '') 
#         FROM INFORMATION_SCHEMA.COLUMNS 
#         WHERE TABLE_NAME = 'FOOD_WAREHOUSE'
#     ), ' FROM FOOD_WAREHOUSE'
# );
# PREPARE stmt1 FROM @sql;
# EXECUTE stmt1;

SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS,
    CASE
        WHEN FREEZER_YN IS NULL THEN 'N'
        ELSE FREEZER_YN
    END AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE WAREHOUSE_NAME LIKE '%경기%'
ORDER BY 1;