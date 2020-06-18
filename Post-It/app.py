from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QPushButton,
    QGridLayout,
    QWidget,
    QLabel,
)
import sys


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Post-It")
        self.resize(800, 600)
        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_widget.setObjectName("main_widget")  # 对象命名
        self.main_layout = QGridLayout()  # 创建网格布局的对象
        self.main_widget.setLayout(self.main_layout)  # 将主部件设置为网格布局

        # 初始化导航栏和导航栏界面
        self.init_navigaton_bar()
        self.init_navigaton_interface()
        self.clicked_1()  # 默认显示界面1

        # 将初始化完成的左侧、右侧空间加入整体空间的网格布局
        self.main_layout.addWidget(self.left_widget, 0, 0, 1, 1)
        self.main_layout.addWidget(self.right_widget1, 0, 1, 1, 6)
        self.main_layout.addWidget(self.right_widget2, 0, 1, 1, 6)
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

    def init_navigaton_bar(self):
        self.left_widget = QWidget()  # 创建左侧部件
        self.left_widget.setObjectName("navigaton_bar")  # 左侧部件对象命名
        self.left_layout = QGridLayout()  # 创建网格布局对象
        self.left_widget.setLayout(self.left_layout)  # 将左侧部件设置为网格布局
        self.button1 = QPushButton()
        self.button1.setText("build")
        self.button2 = QPushButton()
        self.button2.setText("flash")
        self.left_layout.addWidget(self.button1)
        self.left_layout.addWidget(self.button2)

    def init_navigaton_interface(self):
        self.right_widget1 = QWidget()  # 创建右侧界面1
        self.right_widget1.setStyleSheet("QWidget { background-color: Red}")
        self.right_layout1 = QGridLayout()  # 创建网格布局对象1
        self.right_widget1.setLayout(self.right_layout1)  # 设置右侧界面1的布局为网格布局
        self.label1 = QLabel()
        self.label1.setText("111111")
        self.right_layout1.addWidget(self.label1)

        self.right_widget2 = QWidget()  # 创建右侧界面2
        self.right_widget2.setStyleSheet("QWidget { background-color: Blue}")
        self.right_layout2 = QGridLayout()  # 创建网格布局对象2
        self.right_widget2.setLayout(self.right_layout2)  # 设置右侧界面2的布局为网格布局
        self.label2 = QLabel()
        self.label2.setText("222222")
        self.right_layout2.addWidget(self.label2)

        # 把切换界面的button和两个跳转函数绑定
        self.button1.clicked.connect(self.clicked_1)
        self.button2.clicked.connect(self.clicked_2)

    def clicked_1(self):
        self.right_widget1.show()
        self.right_widget2.hide()

    def clicked_2(self):
        self.right_widget1.hide()
        self.right_widget2.show()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    gallery = MyWindow()
    gallery.show()
    sys.exit(myapp.exec_())
