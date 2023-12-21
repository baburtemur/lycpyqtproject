import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt, QDate, pyqtSignal, QRect
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QDialog, QInputDialog, QComboBox,\
     QDialogButtonBox, QVBoxLayout, QTableWidgetItem, QCalendarWidget
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtGui import *
import csv


#-*-coding utf-8-*-

astronomy = [
    "Московская олимпиада школьников",
    "Санкт-Петербургская астрономическая олимпиада"
]
biology = [
    "Олимпиада школьников «Ломоносов»", "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Всесибирская открытая олимпиада школьников",
    "Межрегиональная олимпиада школьников «Будущие исследователи - будущее науки»",
    "Олимпиада школьников «Физтех»"
]
genetic = [
    "Московская олимпиада школьников",
    "Олимпиада школьников «Ломоносов»"
]
geography = [
    "Многопредметная олимпиада «Юные таланты»",
    "Московская олимпиада школьников",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Герценовская олимпиада школьников",
    "Олимпиада школьников «Покори Воробьевы горы!»"
]
geology = [
    "Олимпиада школьников «Ломоносов»",
    "Многопредметная олимпиада «Юные таланты»"
]
gumanitary = [
    "Междисциплинарная олимпиада школьников имени В.И. Вернадского",
    "Телевизионная гуманитарная олимпиада школьников «Умницы и умники»",
    "Олимпиада МГИМО МИД России для школьников"
]
design = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Межрегиональные предметные олимпиады федерального государственного автономного образовательного учреждения высшег"
    "о образования «Казанский (Приволжский) федеральный университет»",
]
natural = [
    "Всероссийский конкурс научных работ школьников «Юниор»",
    "Многопрофильная инженерная олимпиада «Звезда»"
]
journalism = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников «Покори Воробьевы горы!»",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Олимпиада школьников Российской академии народного хозяйства и государственной службы при Президенте Российской Федерации"
]
engineering = [
    'Всероссийская олимпиада школьников «Высшая проба»',
    "Всероссийский конкурс научных работ школьников «Юниор»",
    "Олимпиада школьников «Ломоносов»"
]
foreign = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников «Покори Воробьевы горы!»",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Межрегиональная олимпиада школьников «Евразийская лингвистическая олимпиада»",
    "Олимпиада РГГУ для школьников",
    "лимпиада школьников Российской академии народного хозяйства и государственной службы при Президенте Российской Федерации",
    "Учитель школы будущего",
    "Всероссийская олимпиада школьников «Миссия выполнима. Твое призвание - финансист!»",
    "Межрегиональная олимпиада школьников на базе ведомственных образовательных организаций",
    "Плехановская олимпиада школьников",
    "Региональный конкурс школьников Челябинского университетского образовательного округа"
]
computer = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Вузовско-академическая олимпиада по информатике",
    "Московская олимпиада школьников",
    "Олимпиада школьников по информатике и программированию",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Открытая олимпиада школьников",
    "Открытая олимпиада школьников по программированию",
    "Всесибирская открытая олимпиада школьников",
    "Международная олимпиада «Innopolis Open»",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников по программированию «ТехноКубок»",
    "Открытая олимпиада школьников по программированию «Когнитивные технологии»",
    "Отраслевая олимпиада школьников «Газпром»",
    "Международная олимпиада школьников Уральского федерального университета «Изумруд»",
    "Олимпиада школьников «Гранит науки»",
    "Университетская олимпиада школьников «Бельчонок»"
]
security = [
    "Всероссийская междисциплинарная олимпиада школьников «Национальная технологическая олимпиада»",
    "Международная олимпиада «Innopolis Open»"
]
history = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Межрегиональная олимпиада школьников «Будущие исследователи - будущее науки»",
    "Московская олимпиада школьников",
    "Олимпиада РГГУ для школьников",
    "Олимпиада школьников «Покори Воробьевы горы!»",
    "Олимпиада школьников Российской академии народного хозяйства и государственной службы при Президенте Российской Федерации",
    "Турнир имени М.В. Ломоносова",
    "Всероссийская олимпиада школьников «Миссия выполнима. Твое призвание - финансист!»",
    "Всероссийская Толстовская олимпиада школьников",
    "Международная олимпиада школьников Уральского федерального университета «Изумруд»",
    "Олимпиада школьников федерального государственного бюджетного образовательного учреждения высшего образования «Всероссийский государственный университет юстиции (РПА Минюста России)» «В мир права»",
    "Открытая региональная межвузовская олимпиада вузов Томской области (ОРМО)"
]
linguist = [
    "Московская олимпиада школьников",
    "Турнир имени М.В. Ломоносова"
]
literature = [
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников «Покори Воробьевы горы!»",
    "Всероссийская Толстовская олимпиада школьников",
    "Олимпиада РГГУ для школьников",
    "Турнир имени М.В. Ломоносова"
]
math = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Московская олимпиада школьников",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников «Покори Воробьевы горы!»",
    "Олимпиада школьников «Физтех»",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Санкт-Петербургская олимпиада школьников",
    "Турнир городов",
    "«Формула Единства» / «Третье тысячелетие»",
    "Всесибирская открытая олимпиада школьников",
    "Межрегиональная олимпиада школьников имени И.Я. Верченко",
    "Межрегиональная олимпиада школьников на базе ведомственных образовательных организаций",
    "Объединенная межвузовская математическая олимпиада школьников",
    "Олимпиада Курчатов",
    "Отраслевая физико-математическая олимпиада школьников «Росатом»",
    "Турнир имени М.В. Ломоносова",
    "Всероссийская олимпиада школьников «Миссия выполнима. Твое призвание - финансист!»Международная олимпиада «Innopolis Open»",
    "Межрегиональная олимпиада школьников «Будущие исследователи - будущее науки»"
    "Межрегиональные предметные олимпиады федерального государственного автономного образовательного учреждения высшего образования «Казанский (Приволжский) федеральный университет»",
    "Олимпиада школьников «Шаг в будущее»",
    "Олимпиада Юношеской математической школы",
    "Открытая олимпиада школьников",
    "Университетская олимпиада школьников «Бельчонок»"
]
society = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников «Покори Воробьевы горы!»",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Государственный аудит",
    "Московская олимпиада школьников",
    "Олимпиада школьников Российской академии народного хозяйства и государственной службы при Президенте Российской Федерации",
    "Всероссийская олимпиада школьников «Миссия выполнима. Твое призвание - финансист!»",
    "Всероссийская Толстовская олимпиада школьников",
    "Международная олимпиада школьников Уральского федерального университета «Изумруд»",
    "Межрегиональная олимпиада школьников на базе ведомственных образовательных организаций",
    "Океан знаний",
    "Олимпиада РГГУ для школьников"
]
politology = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников Российской академии народного хозяйства и государственной службы при Президенте Российской Федерации"
]
law = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Кутафинская олимпиада школьников по праву",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Межрегиональная олимпиада по праву «ФЕМИДА»",
    "Московская олимпиада школьников",
    "Всероссийская Толстовская олимпиада школьников",
    "Олимпиада школьников федерального государственного бюджетного образовательного учреждения высшего образования «Всероссийский государственный университет юстиции (РПА Минюста России)» «В мир права»"
]
psychology = [
    "Олимпиада школьников «Ломоносов»",
    "Всероссийская олимпиада школьников «Высшая проба»"
]
painting = [
    "Международная олимпиада школьников «Искусство графики»",
    "Межрегиональная олимпиада школьников имени В.Е. Татлина"
]
robots = [
    "Московская олимпиада школьников",
    "Олимпиада школьников «Ломоносов»"
]
russian = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада РГГУ для школьников",
    "Открытая региональная межвузовская олимпиада вузов Томской области (ОРМО)",
    "Плехановская олимпиада школьников",
    "Межрегиональная олимпиада школьников «Будущие исследователи - будущее науки»",
    "Межрегиональные предметные олимпиады федерального государственного автономного образовательного учреждения высшего образования «Казанский (Приволжский) федеральный университет»",
    "Океан знаний"
]
sociology = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Олимпиада школьников Санкт-Петербургского государственного университета"
]
music = [
    "Всероссийская (с международным участием) олимпиада учащихся музыкальных колледжей",
    "Всероссийская олимпиада по музыкально-теоретическим дисциплинам для учащихся детских музыкальных школ и детских школ искусств"
]
physics = [
    "Интернет-олимпиада школьников по физике",
    "Московская олимпиада школьников",
    "Олимпиада школьников «Покори Воробьевы горы!»",
    "Олимпиада школьников «Физтех»",
    "Отраслевая физико-математическая олимпиада школьников «Росатом»",
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Всесибирская открытая олимпиада школьников",
    "Городская открытая олимпиада школьников по физике",
    "Инженерная олимпиада школьников",
    "Межрегиональная олимпиада школьников «Будущие исследователи - будущее науки»",
    "Олимпиада Курчатов",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников «Робофест»",
    "Олимпиада школьников «Шаг в будущее»",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "«Наследники Левши»",
    "«Формула Единства» / «Третье тысячелетие»",
    "Межрегиональная олимпиада школьников на базе ведомственных образовательных организаций",
    "Межрегиональные предметные олимпиады федерального государственного автономного образовательного учреждения высшего образования «Казанский (Приволжский) федеральный университет»",
    "Олимпиада школьников «Надежда энергетики»",
    "Открытая региональная межвузовская олимпиада вузов Томской области (ОРМО)",
    "Турнир имени М.В. Ломоносова"
]
philology = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Московская олимпиада школьников"
]
phylosophy = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Олимпиада школьников «Ломоносов»"
]
finlit = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "«Финатлон для старшеклассников» - Всероссийская олимпиада по финансовой грамотности, финансовому рынку и защите прав потребителей финансовых услуг",
    "Московская олимпиада школьников",
    "Олимпиада школьников Российской академии народного хозяйства и государственной службы при Президенте Российской Федерации",
    "Плехановская олимпиада школьников"
]
chemistry = [
    "Всесибирская открытая олимпиада школьников",
    "Многопредметная олимпиада «Юные таланты»",
    "Московская олимпиада школьников",
    "Олимпиада школьников «Ломоносов»",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Межрегиональные предметные олимпиады федерального государственного автономного образовательного учреждения высшего образования «Казанский (Приволжский) федеральный университет»",
    "Открытая межвузовская олимпиада школьников Сибирского федерального округа «Будущее Сибири»",
    "Санкт-Петербургская олимпиада школьников",
    "Всероссийская Сеченовская олимпиада школьников",
    "Межрегиональная олимпиада школьников «Будущие исследователи - будущее науки»",
    "Олимпиада школьников «Гранит науки»",
    "Открытая химическая олимпиада",
    "Открытая химическая олимпиада",
    "Университетская олимпиада школьников «Бельчонок»"
]
ecology = [
    "Олимпиада школьников «Ломоносов»",
    "Московская олимпиада школьников"
]
economy = [
    "Всероссийская олимпиада школьников «Высшая проба»",
    "Всероссийская экономическая олимпиада школьников имени Н.Д. Кондратьева",
    "Московская олимпиада школьников",
    "Олимпиада школьников по экономике в рамках международного экономического фестиваля школьников «Сибириада. Шаг в мечту»",
    "Олимпиада школьников Санкт-Петербургского государственного университета",
    "Всероссийская олимпиада школьников «Миссия выполнима. Твое призвание - финансист!»",
    "Олимпиада школьников Российской академии народного хозяйства и государственной службы при Президенте Российской Федерации",
    "Плехановская олимпиада школьников"
]
status = [
    "Зарегистрирован",
    "Заявка подана",
    "Незарегистрирован",
    "Неоткрыта"
]

stage = [
    "Отборочный",
    "Региональный",
    "Муниципальный",
    "Заключительный"
]
discipline = {"Астрономия": astronomy, "Биология": biology, "Генетика": genetic, "География": geography,
              "Гуманитарные науки": gumanitary, "Дизайн": design, "Естественные науки": natural,
              "Журналистика": journalism, "Инженерные науки": engineering, "Иностранный язык": foreign, "Информатика":
              computer, "Информационная безопасность": security, "История": history, "Лингвистика": linguist,
              "Литература": literature, "Математика": math, "Обществознание": society, "Политология": politology,
              "Право": law, "Психология": psychology, "Рисунок": painting, "Робототехника": robots,
              "Русския язык": russian, "Социология": sociology, "Теория музыки": music, "Физика": physics,
              "Филология": philology, "Философия": phylosophy, "Финансовая грамотность": finlit, "Химия": chemistry,
              "Экология": ecology, "Экономика": economy}

names = ['-']
for elem in discipline.values():
    for item in elem:
        if item not in names:
            names.append(item)

class OlimpSchedule(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.timeButton.clicked.connect(self.time)
        self.findButton.clicked.connect(self.find)
        self.selectall.clicked.connect(self.select)
        self.addButton.clicked.connect(self.add)
        self.add_check0.stateChanged.connect(self.add0)
        self.delbutton.clicked.connect(self.dell)
        self.c0 = 0
        self.c1 = 0
        self.c2 = 0
        self.add_check1.stateChanged.connect(self.add1)
        self.add_check2.stateChanged.connect(self.add2)
        self.v = QComboBox()
        self.searchbox_1.addItems(elem for elem in status)
        for elem in discipline.keys():
            self.searchbox_2.addItem(elem)
        self.searchbox_3.addItems(elem for elem in stage)
        self.search.currentTextChanged.connect(self.replace)
        self.date.setDate(QDate.currentDate())
        self.date.setCalendarPopup(True)
        self.date.setMinimumDate(QDate.currentDate().addDays(-35))
        self.date.hide()
        self.Date.hide()
        self.datecheck.stateChanged.connect(self.showw)
        self.sh = 0
        self.clear_button.clicked.connect(self.clear)
        self.name = ""
        self.item = ""
        with open('results.csv', 'r', encoding='utf-8') as csfile:
            reader = csv.reader(csfile, delimiter=";")
            title = next(reader)
            self.rowPosition = len(list(reader))
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(self.rowPosition)
            for i in range(len(title)):
                self.tableWidget.setColumnWidth(i, 189)
        self.select()

    def select(self):
        with open('results.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            sub = 0
            for i, row in enumerate(reader):
                if len(row) == 0:
                    sub += 1
                    continue
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i - sub, j, QTableWidgetItem(elem))

    def add(self):
        with open('results.csv', 'r', encoding='utf-8') as csfile:
            reader = csv.reader(csfile, delimiter=';')
            self.rowPositionpl = self.rowPosition - 1
            self.tableWidget.insertRow(self.rowPositionpl)
            rr = next(reader)
            if self.search.currentText() == "предмету":
                self.item = self.searchbox_2.currentText()
                name, ok = QInputDialog.getItem(self, "Введите название олимпиады", "Название", (names), 1, True)
                if ok:
                    self.name = name
                else:
                    self.tableWidget.setRowCount(self.tableWidget.rowCount() - 1)
                    return
            else:
                self.name = self.searchbox_2.currentText()
                name, ok = QInputDialog.getItem(self, "Введите предмет", "Предмет", (discipline.keys()), 1, True)
                if ok:
                    self.item = name
                else:
                    self.tableWidget.setRowCount(self.tableWidget.rowCount() - 1)
                    return
            qqq = list(reader)
            for elem in qqq:
                if elem == []:
                    qqq.remove([])
            if len(qqq) > 0:
                id = int(qqq[-1][-1]) + 1
            else:
                id = 0
            if self.date.date() == QDate.currentDate():
                self.dt = "Неизвестно"
            else:
                self.dt = str(self.date.date().toPyDate())
            self.current = [self.searchbox_1.currentText(), self.name, self.item,
                            self.searchbox_3.currentText(), self.dt, str(id)]
            for elem in self.current:
                if elem == '-':
                    dlg = Warning(["Вы не ввели все параметры!"])
                    dlg.setWindowTitle("ошибка!")
                    dlg.exec()
                    self.tableWidget.setRowCount(self.tableWidget.rowCount() - 1)
                    return
            for elem in reader:
                try:
                    if elem[2] == self.current[2] and elem[1] == self.current[1]:
                        dlg = Warning(["Олимпиада уже присутствует в реестре!,"
                                      " нажмите 'удалить' чтобы убрать её из списка"])
                        dlg.setWindowTitle("ошибка!")
                        dlg.exec()
                        self.tableWidget.setRowCount(self.tableWidget.rowCount() - 1)
                        return
                except IndexError:
                    continue
            for i in range(len(self.current)):
                if self.current[i] == "":
                    self.current[i] = "Неизвестно"
                self.tableWidget.setItem(self.rowPositionpl, i, QTableWidgetItem(self.current[i]))
            with open('results.csv', 'a', encoding='utf-8') as csfile:
                print(";".join(self.current), end='\n', file=csfile)
            self.rowPosition += 1

    def find(self):
        try:
            if len(self.tableWidget.selectedIndexes()) == 0:
                name, ok = QInputDialog.getInt(self, "Id", "Введите id", 0, 0, self.rowPosition)
                a = ""
                if ok:
                    with open("results.csv", "r", encoding="utf-8") as vv:
                        vr = csv.reader(vv, delimiter=';')
                        for elem in vr:
                            if len(elem) < 5:
                                continue
                            if elem[5] == str(name):
                                dlg = Warning([', '.join(elem)])
                                dlg.exec()
            else:
                a = []
                with open("results.csv", "r", encoding="utf-8") as vv:
                    vt = list(csv.reader(vv, delimiter=";"))
                for item in self.tableWidget.selectedIndexes():
                    b = ""
                    for i in vt[item.row() + 2]:
                        b += i + ', '
                    a.append(b)
                dlg = Warning(a)
                dlg.exec()
        except IndexError:
            Warning(["Таблица пуста!"]).exec()

    def dell(self):
        try:
            if len(self.tableWidget.selectedIndexes()) == 0:
                name, ok = QInputDialog.getInt(self, "Id", "Введите id", 0, 0, self.rowPosition)
                if ok:
                    with open("results.csv", "r", encoding="utf-8") as vv:
                        vt = list(csv.reader(vv, delimiter=";"))
                        vt.pop(name + 2)
                        self.tableWidget.removeRow(name)
                    with open("results.csv", 'w', encoding="utf-8") as vv:
                        self.rowPosition = len(vt)
                        tt = csv.writer(vv, delimiter=';')
                        for elem in vt:
                            tt.writerow(elem)
            else:
                with open("results.csv", "r", encoding="utf-8") as vv:
                    vt = list(csv.reader(vv, delimiter=";"))
                for item in self.tableWidget.selectedIndexes():
                    vt.pop(item.row() + 2)
                    self.tableWidget.removeRow(item.row())
                with open("results.csv", 'w', encoding="utf-8") as vv:
                    self.rowPosition = len(vt) - 1
                    tt = csv.writer(vv, delimiter=';')
                    filter(lambda x: len(x) > 1, vt)
                    point = 0
                    for elem in vt:
                        if len(elem) > 5:
                            tt.writerow(elem)
                            point += 1
            self.rowPosition = point

        except IndexError:
            Warning(["Таблица пуста!"]).exec()

    def showw(self):
        if self.sh % 2 == 0:
            self.date.show()
            self.Date.show()
        else:
            self.date.hide()
            self.Date.hide()
        self.sh += 1


    def replace(self):
        if self.search.currentText() == "предмету":
            self.Name.setText("Предмет")
            self.searchbox_2.clear()
            self.searchbox_2.addItems(item for item in discipline.keys())
        else:
            self.Name.setText("Название")
            self.searchbox_2.clear()
            self.searchbox_2.addItems(item for item in names)

    def add0(self):
        if self.c0 % 2 == 0:
            self.searchbox_1.hide()
            self.edit0.show()
        else:
            self.searchbox_1.show()
            if self.edit0.text() != "":
                self.searchbox_1.addItem(self.edit0.text())
            self.edit0.hide()
        self.c0 += 1
        self.edit0.clear()

    def add1(self):
        if self.c1 % 2 == 0:
            self.searchbox_2.hide()
            self.edit1.show()
        else:
            self.searchbox_2.show()
            if self.edit1.text() != "":
                self.searchbox_2.addItem(self.edit1.text())
            self.edit1.hide()
        self.c1 += 1
        self.edit1.clear()


    def add2(self):
        if self.c2 % 2 == 0:
            self.searchbox_3.hide()
            self.edit2.show()
        else:
            self.searchbox_3.show()
            if self.edit2.text() != "":
                self.searchbox_3.addItem(self.edit2.text())
            self.edit2.hide()
        self.c2 += 1
        self.edit2.clear()

    def clear(self):
        with open('results.csv', "w", encoding='utf-8') as qq:
            t = csv.writer(qq, delimiter=';')
            t.writerow(['Статус', 'Название', 'Предмет', 'Этап', 'Дата', 'Id'])
        self.tableWidget.setRowCount(0)
        main = ['Статус', 'Название', 'Предмет', 'Этап', 'Дата', 'Id']
        for i in range(len(main)):
            self.tableWidget.setItem(0, i, QTableWidgetItem(main[i]))
        self.rowPosition = 1

    def time(self):
        with open("results.csv", 'r', encoding='utf-8') as cc:
            cv = list(csv.reader(cc, delimiter=';'))
        dlg = getDate(cv)
        dlg.setWindowTitle("Даты")
        dlg.exec()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F1:
            dlg = Manual()
            dlg.setWindowTitle("Руководство")
            dlg.exec()

class Manual(QDialog):
    signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ошибка!")
        self.setFixedSize(600, 120)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout(self)
        message = QLabel(open('readme.txt', 'r', encoding='utf-8'), self)
        message.setFont(QFont('Arial', 10))
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class getDate(QDialog):
    signal = pyqtSignal(int)

    def __init__(self, a):
        super().__init__()
        self.setFixedSize(400, 400)
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(0, 0, 400, 400)
        self.calendar.setSelectionMode(QCalendarWidget.SelectionMode.SingleSelection)
        painter = QPainter(self.calendar)
        painter.setBrush(QColor(0, 255, 0))
        v = ""
        for i in range(2, len(a)):
            if a[i][4] == "Неизвестно":
                continue
            self.calendar.paintCell(painter, QRect(0, 0, 400, 400), QDate.fromString(a[i][4]))
            v = self.calendar.selectedDate()
        self.calendar.clicked.connect(self.info)

    def info(self):
        date = str(self.calendar.selectedDate().toPyDate())
        with open("results.csv", 'r', encoding='utf-8') as cc:
            ct = list(csv.reader(cc, delimiter=';'))
        for i in range(2, len(ct)):
            if ct[i][4].strip() == date.strip():
                vt = list(ct[i][y] for y in range(len(ct[i]) - 2))
                Warning(vt).exec()



class Warning(QDialog):
    signal = pyqtSignal(int)

    def __init__(self, a):
        super().__init__()
        max = 0
        for elem in a:
            if len(elem) > max:
                max = len(elem)
        self.setWindowTitle("")
        self.setFixedSize(40 + max * 7, 120)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout(self)
        message = QLabel('\n'.join(a), self)
        message.setFont(QFont('Arial', 10))
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OlimpSchedule()
    ex.show()
    sys.exit(app.exec())