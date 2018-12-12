#! python3
# 随机顺序创建带有问题和答案的测验以及答案键。

import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'北京': '北京', '上海': '上海', '天津': '天津',
   '重庆': '重庆', '黑龙江': '哈尔滨', '吉林': '长春',
   '辽宁': '沈阳', '内蒙古': '呼和浩特', '河北': '石家庄',
   '新疆': '乌鲁木齐', '甘肃': '兰州', '青海': '西宁', '陕西':
   '西安', '宁夏': '银川', '河南': '郑州', '山东':
   '济南', '山西': '太原', '安徽': '合肥', '湖北':
   '武汉', '湖南': '长沙', '江苏': '南京', '四川':
   '成都', '贵州': '贵阳', '云南': '昆明', '广西':
   '南宁', '西藏': '拉萨', '浙江': '杭州', '江西':
   '南昌', '广东': '广州', '福建': '福州', '台湾': '台北', '海南': '海口', '香港': '香港',
   '澳门': '澳门'}


# 生成10个测验文件。

for quizNum in range(10):
    # Create the quiz and answer key files.#创建测验和回答密钥文件。
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quizFile.write('姓名:\n\n日期:\n\n年级:\n\n')
    quizFile.write((' ' * 20) + '全国省会测试 (试卷 %s)' % (quizNum + 1))
    quizFile.write('\n\n')


    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 34 states, making a question for each.循环遍历34个州，为每个州提出问题。
    for questionNum in range(34):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. %s的省会是 ?\n' % (questionNum + 1,
                   states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')


        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
                  answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
