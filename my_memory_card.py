from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Португалии', 'Португальский', 'Английский', 'Испанский', 'Французский'))
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('В каком году был выпущен первый телефон компании Apple(Iphone)?', '2007', '2008', '2005', '2010'))
questions_list.append(Question('Какой национальности не существует?', 'Энцы', 'Смурфы', 'Чульмцы', 'Алеуты'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'жёлтый', 'белый', 'синий', 'красный'))

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
            print('Рейтинг:', window.score/window.total*100)

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def next_question():
    cur_question= randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
    window.total += 1

def ask(q: Question):
    shuffle = (answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Correct.setText(q.right_answer)
    lb_Question.setText(q.quest)
    show_question()

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

app = QApplication([])

window = QWidget()
window.resize(600, 400)
window.setWindowTitle('Не забывай про скобки')

'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Какой национальности не существует?') # текст вопроса

RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чульмцы')
rbtn_4 = QRadioButton('Алеуты')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 

AnsGroupBox = QGroupBox('Результаты теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ тут!')
AnsGroupBox.hide()

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment= Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
#RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)

# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

window.cur_question = -1

btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()

window.setLayout(layout_card)
window.show()
app.exec()