import logging

logging.basicConfig(level=logging.ERROR, format=f'you got an ERROR %(message)s at %(asctime)s please check the values', filename='log.log')

def check(checking):
    try:
        print(eval(checking))
    except BaseException as err:
        logging.error(err)
    else:
        print("ok")

check("1+1")
check("1/0")
check("1/None")
check('"a"*"a"')
check('"a"*2')
