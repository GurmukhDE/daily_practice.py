from loguru import logger
l = [2,4,5,6,8,9]

l2  = ['a', 'b']

list_inside_list_append = (logger.info(l.append(l2)))
logger.info(f'list_inside_list_appended {l}')
logger.info(l.append(3))
logger.info(l)

l2 = [1,3,7]
logger.info(l.extend(l2))
logger.info(l)

logger.info(l.insert(4,2))
logger.info(l)
#
md_list = [['gurmukh', "data_engineer"],['company', 'EPAM']] #multidimensional List

print(md_list[1][0])

lis = [1,2,3]

l = [4,6,7]
logger.info(lis.extend(l))

logger.info(lis)
