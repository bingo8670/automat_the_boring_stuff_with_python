import logging
# 打印日志信息时，使用 logging.debug() 函数。这个 debug() 函数 将调用 basicConfig()，打印一行信息。这行信息的格式是我们在 basicConfig()函数 中指定的，并且包括我们传递给 debug() 的消息。
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
