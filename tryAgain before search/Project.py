# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'naya.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pandas as pd
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QTableView
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import csv
import sortingAlgorithms
import tkinter as tk
from tkinter import messagebox


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1085, 797)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                # self.title_search = QtWidgets.QLineEdit(MainWindow)

                        # Add search boxes and filter options for each column
                # self.search_layout = QtWidgets.QHBoxLayout()

                

                self.label_3 = QtWidgets.QLabel(self.centralwidget)

                self.label_3.setGeometry(QtCore.QRect(50, 140, 91, 41))
                self.label_3.setStyleSheet("font-size:23px;\n"
        "color: rgb(170, 0, 127);")
                self.label_3.setObjectName("label_3")
                self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_4.setGeometry(QtCore.QRect(500, 640, 201, 61))
                font = QtGui.QFont()
                font.setPointSize(-1)
                self.pushButton_4.setFont(font)
                self.pushButton_4.setStyleSheet("QPushButton {\n"
        "    background-color: #aa007f;  /* Matte Yellow */\n"
        "    border-radius: 15px;\n"
        "    border: 2px solid #555;\n"
        "    min-width: 60px;\n"
        "    min-height: 30px;\n"
        "    color: #1E1E1E;  /* Matte Black text */\n"
        "    font-size: 23px;\n"
        "}\n"
        "\n"
        "QPushButton::checked {\n"
        "    background-color: #aa007f;  /* Matte Yellow */\n"
        "}\n"
        "\n"
        "QPushButton::before {\n"
        "    content: \"\";\n"
        "    position: absolute;\n"
        "    top: 5px;\n"
        "    left: 5px;\n"
        "    width: 20px;\n"
        "    height: 20px;\n"
        "    background-color: #FFFFFF;  /* Handle color */\n"
        "    border-radius: 50%;\n"
        "    transition: left 0.3s;\n"
        "    font-size: 23px;\n"
        "}\n"
        "\n"
        "QPushButton::checked::before {\n"
        "    left: 35px;\n"
        "}\n"
        "")
                self.pushButton_4.setObjectName("pushButton_4")
                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_2.setGeometry(QtCore.QRect(800, 220, 201, 51))
                font = QtGui.QFont()
                self.pushButton_2.setFont(font)
                self.pushButton_2.setStyleSheet("QPushButton {\n"
        "    background-color: #aa007f;  /* Matte Yellow */\n"
        "    border-radius: 10px;\n"
        "    border: 2px solid #555;\n"
        "    min-width: 60px;\n"
        "    min-height: 30px;\n"
        "    color: #1E1E1E;  /* Matte Black text */\n"
        "}\n"
        "\n"
        "QPushButton::checked {\n"
        "    background-color: #FFCC00;  /* Matte Yellow */\n"
        "}\n"
        "\n"
        "QPushButton::before {\n"
        "    content: \"\";\n"
        "    position: absolute;\n"
        "    top: 5px;\n"
        "    left: 5px;\n"
        "    width: 20px;\n"
        "    height: 20px;\n"
        "    background-color: #FFFFFF;  /* Handle color */\n"
        "    border-radius: 50%;\n"
        "    transition: left 0.3s;\n"
        "}\n"
        "\n"
        "QPushButton::checked::before {\n"
        "    left: 35px;\n"
        "}\n"
        "")
                self.pushButton_2.setObjectName("pushButton_2")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(550, 140, 91, 41))
                self.label_4.setStyleSheet("font-size:23px;\n"
        "color: rgb(170, 0, 127);")
                self.label_4.setObjectName("label_4")
                self.comboBox = QtWidgets.QComboBox(self.centralwidget)
                self.comboBox.setGeometry(QtCore.QRect(150, 140, 251, 31))
                self.comboBox.setMinimumSize(QtCore.QSize(251, 31))
                self.comboBox.setStyleSheet("background-color:#FFFFFF;\n"
        "border-color:#1E1E1E;\n"
        "")
                self.comboBox.setObjectName("comboBox")
                self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_3.setGeometry(QtCore.QRect(300, 640, 201, 61))
                font = QtGui.QFont()
                font.setPointSize(-1)
                self.pushButton_3.setFont(font)
                self.pushButton_3.setStyleSheet("QPushButton {\n"
        "    background-color:#aa007f; \n"
        "    border-radius: 15px;\n"
        "    border: 2px solid #555;\n"
        "    min-width: 60px;\n"
        "    min-height: 30px;\n"
        "    color: #1E1E1E;  /* Matte Black text */\n"
        "    font-size: 23px;\n"
        "}\n"
        "\n"
        "QPushButton::checked {\n"
        "    background-color: #aa007f; \n"
        "}\n"
        "\n"
        "QPushButton::before {\n"
        "    content: \"\";\n"
        "    position: absolute;\n"
        "    top: 5px;\n"
        "    left: 5px;\n"
        "    width: 20px;\n"
        "    height: 20px;\n"
        "    background-color: #FFFFFF;  /* Handle color */\n"
        "    border-radius: 50%;\n"
        "    transition: left 0.3s;\n"
        "    font-size: 23px;\n"
        "\n"
        "}\n"
        "\n"
        "QPushButton::checked::before {\n"
        "    left: 35px;\n"
        "}\n"
        "")
                self.pushButton_3.setIconSize(QtCore.QSize(16, 16))
                self.pushButton_3.setObjectName("pushButton_3")
                self.label_9 = QtWidgets.QLabel(self.centralwidget)
                self.label_9.setGeometry(QtCore.QRect(380, 20, 51, 51))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(51)
                sizePolicy.setVerticalStretch(51)
                sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
                self.label_9.setSizePolicy(sizePolicy)
                self.label_9.setMinimumSize(QtCore.QSize(51, 51))
                self.label_9.setStyleSheet("image: url(:/Icons/sort.png);")
                self.label_9.setText("")
                self.label_9.setPixmap(QtGui.QPixmap(":/Icons/sort.png"))
                self.label_9.setScaledContents(True)
                self.label_9.setObjectName("label_9")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(500, 360, 201, 51))
                font = QtGui.QFont()
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("QPushButton {\n"
        "    background-color: #aa007f;  /* Matte Yellow */\n"
        "    border-radius: 15px;\n"
        "    border: 2px solid #555;\n"
        "    min-width: 60px;\n"
        "    min-height: 30px;\n"
        "    color: #1E1E1E;  /* Matte Black text */\n"
        "}\n"
        "\n"
        "QPushButton::checked {\n"
        "    background-color: #aa007f;  /* Matte Yellow */\n"
        "}\n"
        "\n"
        "QPushButton::before {\n"
        "    content: \"\";\n"
        "    position: absolute;\n"
        "    top: 5px;\n"
        "    left: 5px;\n"
        "    width: 20px;\n"
        "    height: 20px;\n"
        "    background-color: #FFFFFF;  /* Handle color */\n"
        "    border-radius: 50%;\n"
        "    transition: left 0.3s;\n"
        "}\n"
        "\n"
        "QPushButton::checked::before {\n"
        "    left: 35px;\n"
        "}\n"
        "")
                self.pushButton.setObjectName("pushButton")
                self.tableView = QtWidgets.QTableView(self.centralwidget)
                self.tableView.setGeometry(QtCore.QRect(100, 330, 901, 291))
                self.tableView.setMinimumSize(QtCore.QSize(861, 291))
                self.tableView.setStyleSheet("background-color:#FFFFFF;color : #1E1E1E;")
                self.tableView.setObjectName("tableView")
                self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(470, 10, 199, 69))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(26)
                self.label.setFont(font)
                self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
                self.label.setStyleSheet("color: rgb(170, 0, 127);\n"
        "background-color: rgb(0, 0, 127);")
                self.label.setObjectName("label")
                

                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(730, 650, 300, 41))
                self.label_6.setMinimumSize(QtCore.QSize(111, 41))
                self.label_6.setStyleSheet("color:#aa007f;font-size:20px;")
                self.label_6.setObjectName("label_6")

                
                
                self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
                self.comboBox_2.setGeometry(QtCore.QRect(680, 140, 251, 31))
                self.comboBox_2.setMinimumSize(QtCore.QSize(251, 31))
                self.comboBox_2.setStyleSheet("background-color:#FFFFFF;border-color:#1E1E1E;")
                self.comboBox_2.setObjectName("comboBox_2")
                self.comboBox_2.addItem("")
                self.comboBox_2.addItem("")
                self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_6.setGeometry(QtCore.QRect(100, 640, 201, 61))
                font = QtGui.QFont()
                font.setPointSize(-1)
                self.pushButton_6.setFont(font)
                self.pushButton_6.setStyleSheet("QPushButton {\n"
        "    background-color: #aa007f;\n"
        "  \n"
        "    border-radius: 15px;\n"
        "    border: 2px solid #555;\n"
        "    min-width: 60px;\n"
        "    min-height: 30px;\n"
        "    color: #1E1E1E;  /* Matte Black text */\n"
        "font-size: 23px;\n"
        "}\n"
        "\n"
        "QPushButton::checked {\n"
        "   \n"
        "    background-color: rgb(85, 0, 255);\n"
        "}\n"
        "\n"
        "QPushButton::before {\n"
        "    content: \"\";\n"
        "    position: absolute;\n"
        "    top: 5px;\n"
        "    left: 5px;\n"
        "    width: 20px;\n"
        "    height: 20px;\n"
        "    background-color: #FFFFFF;  /* Handle color */\n"
        "    border-radius: 50%;\n"
        "    transition: left 0.3s;\n"
        "font-size: 23px;\n"
        "}\n"
        "\n"
        "QPushButton::checked::before {\n"
        "    left: 35px;\n"
        "}\n"
        "")
                self.pushButton_6.setObjectName("pushButton_6")
                self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_5.setGeometry(QtCore.QRect(340, 705, 201, 61))
                font = QtGui.QFont()
                font.setPointSize(-1)
                self.pushButton_5.setFont(font)
                self.pushButton_5.setStyleSheet("QPushButton {\n"
        "    background-color: #aa007f;  /* Matte Yellow */\n"
        "    border-radius: 15px;\n"
        "    border: 2px solid #555;\n"
        "    min-width: 60px;\n"
        "    min-height: 30px;\n"
        "    color: #1E1E1E;  /* Matte Black text */\n"
        "font-size: 23px;\n"
        "}\n"
        "\n"
        "QPushButton::checked {\n"
        "    background-color: #aa007f;  /* Matte Yellow */\n"
        "}\n"
        "\n"
        "QPushButton::before {\n"
        "    content: \"\";\n"
        "    position: absolute;\n"
        "    top: 5px;\n"
        "    left: 5px;\n"
        "    width: 20px;\n"
        "    height: 20px;\n"
        "    background-color: #FFFFFF;  /* Handle color */\n"
        "    border-radius: 50%;\n"
        "    transition: left 0.3s;\n"
        "font-size: 23px;\n"
        "}\n"
        "\n"
        "QPushButton::checked::before {\n"
        "    left: 35px;\n"
        "}\n"
        "")
                self.pushButton_5.setObjectName("pushButton_5")
                self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
                self.progressBar.setGeometry(QtCore.QRect(110, 260, 651, 41))
                self.progressBar.setProperty("value", 0)
                self.progressBar.setObjectName("progressBar")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_3.setText(_translate("MainWindow", "Sort"))
                self.pushButton_4.setText(_translate("MainWindow", "Pause"))
                self.pushButton_2.setText(_translate("MainWindow", "Sort"))
                self.label_4.setText(_translate("MainWindow", "Order"))
                # self.comboBox.setItemText(0, _translate("MainWindow", "BubbleSort"))
                # self.comboBox.setItemText(1, _translate("MainWindow", "MergeSort"))
                self.comboBox.addItems(["Select Algorithm","Merge Sort", "Bubble Sort", "Selection Sort", "Insertion Sort", 
                                    "Hybrid Merge Sort", "Quick Sort", "Counting Sort", 
                                    "Radix Sort", "Bucket Sort", "Genome Sort", 
                                    "Cycle Sort", "Brick Sort"])
                self.pushButton_3.setText(_translate("MainWindow", "Play"))
                self.pushButton.setText(_translate("MainWindow", "Go to Sort"))
                self.label.setText(_translate("MainWindow", "SortScraper"))
                self.label_6.setText(_translate("MainWindow", ""))
                self.comboBox_2.setItemText(0, _translate("MainWindow", "Ascending"))
                self.comboBox_2.setItemText(1, _translate("MainWindow", "Descending"))
                self.pushButton_6.setText(_translate("MainWindow", "Clear"))
                self.pushButton_5.setText(_translate("MainWindow", "Load From Csv"))

        
class ScraperThread(QtCore.QThread):
    progress_update = QtCore.pyqtSignal(int)  # Signal to update progress bar
    data_ready = QtCore.pyqtSignal(list)  # Signal to emit new rows of data

    def __init__(self):
        super(ScraperThread, self).__init__()
        self._is_paused = False
        self._mutex = QtCore.QMutex()
        self._wait_condition = QtCore.QWaitCondition()
        self.total_movies = 0  # Total number of movies to be scraped for progress calculation
        self.movies_scraped = 0  # Count of movies scraped so far

    def pause(self):
        """Pause the thread."""
        self._is_paused = True

    def resume(self):
        """Resume the thread."""
        self._is_paused = False
        self._wait_condition.wakeAll()  # Wake the thread if it's paused

    def run(self):
        # Web scraping logic
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        chrome_service = Service('C:\\Users\\musno\\OneDrive\\Desktop\\SEMESTER 3\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')  # Replace with your chromedriver path
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        number_of_pages = 10  # You can adjust this
        moviesOnOnePage = 0
        checkedMoviesCount = False

        for page in range(1, number_of_pages + 1):
            try:
                url = f'https://www.flickchart.com/charts.aspx?perpage=50000&page={page}'
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                movies = soup.find_all('div', class_='movieDetails')
                if not checkedMoviesCount:
                    moviesOnOnePage = len(movies)
                    checkedMoviesCount = True
                    self.total_movies = moviesOnOnePage * number_of_pages

                # Loop through each movie in the page
                for movie in movies:
                    # Pause mechanism before processing each movie
                    self._mutex.lock()
                    if self._is_paused:
                        self._wait_condition.wait(self._mutex)
                    self._mutex.unlock()

                    try:
                        title = movie.find('span', itemprop='name').get_text(strip=True)
                        release_year = movie.find('a', class_='chartsYear').get_text(strip=True)
                        duration = movie.find('span', class_='minutes').get_text(strip=True).replace(',', '').strip()
                        director = movie.find('a', href=lambda x: x and 'director=' in x).get_text(strip=True)
                        main_cast = movie.find_all('a', href=lambda x: x and 'actor=' in x)
                        actor_1 = main_cast[0].get_text(strip=True) if len(main_cast) > 0 else ''
                        actor_2 = main_cast[1].get_text(strip=True) if len(main_cast) > 1 else ''
                        genres = [genre.get_text(strip=True) for genre in movie.find('p', class_='genre').find_all('a', class_='filterLink')]
                        genre = genres[0] if genres else ''
                        movie_data = [[title, release_year, duration, director, actor_1, actor_2, genre]]

                        # Emit data for this movie immediately
                        self.data_ready.emit(movie_data)
                        # Append the data to the CSV file
                        # with open('new.csv', mode='a', newline='', encoding='utf-8') as file:
                        #     writer = csv.writer(file)
                        #     writer.writerow(movie_data)

                        # Increment the count of movies scraped
                        self.movies_scraped += 1

                        # Update progress based on movies processed
                        self.progress_update.emit(int((self.movies_scraped / self.total_movies) * 100))

                    except Exception as e:
                        print(f"Error processing movie: {e}")

            except Exception as e:
                print(f"Error on page {page}: {e}")
                continue

        driver.quit()


class MainApp(QtWidgets.QMainWindow):
        def __init__(self):
                super().__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                self.ui.pushButton_6.clicked.connect(self.clear)
                self.ui.pushButton_4.setText("Pause Scraping")
                self.ui.pushButton_4.clicked.connect(self.toggle_pause_resume)
                self.ui.pushButton_3.clicked.connect(self.start_scraping)
                self.ui.pushButton_5.clicked.connect(self.load_csv)
                self.ui.pushButton_2.clicked.connect(self.sort_data)
                # self.ui.title_search.textChanged.connect(lambda: self.filter_data('title', self.ui.title_search.text()))

                
                # Thread to handle scraping
                self.scraper_thread = ScraperThread()
                self.scraper_thread.progress_update.connect(self.update_progress)
                self.scraper_thread.data_ready.connect(self.append_rows_to_table)

                # Set up the model for the table
                self.model = QStandardItemModel()
                self.model.setHorizontalHeaderLabels(['Title', 'Release Year', 'Duration', 'Director', 'Actor 1', 'Actor 2', 'Genre'])
                self.ui.tableView.setModel(self.model)

                # State for pause and resume
                self.is_paused = False

        def update_table(self, sorted_data):
                self.model.clear()  # Clear the current model
                self.model.setHorizontalHeaderLabels(['Title', 'Release Year', 'Duration', 'Director', 'Actor 1', 'Actor 2', 'Genre'])
                for row_data in sorted_data:
                        items = [QStandardItem(str(field)) for field in row_data]
                        self.model.appendRow(items)
                        

        def clear(self):
                try:
                # Reset the table view by setting an empty model
                        self.model.clear()  # Clear the existing data in the model
                        self.model.setHorizontalHeaderLabels(['Title', 'Release Year', 'Duration', 'Director', 'Actor 1', 'Actor 2', 'Genre'])
                        self.ui.tableView.setModel(self.model)# Set the empty model to the table view
                        print("Table cleared successfully")
                except Exception as e:
                        print(f"Error clearing table: {e}")


        def filter_data(self, column_name, search_text):
                """Filters the table data based on search input for a given column."""
                filtered_data = []
                
                column_index = self.get_column_index(column_name)
                
                for row in self.table_data:  # Assuming self.table_data is the original full dataset
                        # Apply filtering logic
                        if column_name in ['title', 'director', 'actor_1', 'actor_2', 'genre']:  # For string columns
                                if self.ui.filter_type.currentText() == "Contains" and search_text.lower() in row[column_index].lower():
                                        filtered_data.append(row)
                                elif self.ui.filter_type.currentText() == "Starts With" and row[column_index].lower().startswith(search_text.lower()):
                                        filtered_data.append(row)
                                elif self.ui.filter_type.currentText() == "Ends With" and row[column_index].lower().endswith(search_text.lower()):
                                        filtered_data.append(row)
                        else:  # For numeric columns like "Release Year", "Duration"
                                try:
                                        value = int(search_text)
                                        if int(row[column_index]) == value:
                                                filtered_data.append(row)
                                except ValueError:
                                        pass  # If the search input isn't valid, ignore the filtering

                self.update_table(filtered_data)

        def load_csv(self):
        # Load the CSV file automatically
                fileName = "hahah.csv"  # Specify the path to your CSV file here
        
                try:
                        # Load the CSV file using pandas
                        data = pd.read_csv(fileName)
                        
                        # Create a model and set it to the table view
                        model = QtGui.QStandardItemModel()
                        model.setHorizontalHeaderLabels(data.columns)

                        for row in data.values:
                                items = [QtGui.QStandardItem(str(item)) for item in row]
                                model.appendRow(items)
                                self.model = model

                        self.ui.tableView.setModel(self.model)

                except Exception as e:
                        print(f"Error loading CSV: {e}")


        def sort_data(self):

                checkOrder = self.ui.comboBox_2.currentText()
                reverse = False
                if(checkOrder == "Descending"):
                        reverse = True

                # Retrieve the selection model from the table view
                selected_algorithm = self.ui.comboBox.currentText()
                selection_model = self.ui.tableView.selectionModel()
                
                # Get the selected indexes
                selected_indexes = selection_model.selectedIndexes()
                
                if not selected_indexes:
                        print("No column selected for sorting.")
                        return  # Exit if no column is selected

                # Get the first selected index (assuming you select only one column)
                selected_index = selected_indexes[0]

                # Get the column index of the selected header
                column_index = selected_index.column()

                print(f"Selected Column Index: {column_index}")

                if column_index < 0:  # If no valid column is selected
                        return

               

                # Retrieve the table data once
                table_data = self.get_table_data()
                print(f"Table Data Before Sorting: {table_data}")


                if selected_algorithm in ["Counting Sort", "Radix Sort", "Bucket Sort"]:
                        # Ensure Counting Sort is only used for valid numeric columns
                        if column_index == 1:  # Assuming column 1 is Release Year, 2 is Duration
                                table_data = self.preprocess_release_years(table_data, column_index)
                        elif column_index == 2:
                                table_data = self.preprocess_durations(table_data, column_index)
                        else:
                                messagebox.showerror("Invalid Column", "This Sort can only be applied to numeric columns.")
                                return
                elif column_index == 2:
                                table_data = self.preprocess_durations(table_data, column_index)
                

                start_time = time.time()

                # Choose the sorting algorithm based on user selection
                if selected_algorithm == "Bubble Sort":
                        sorted_data = sortingAlgorithms.bubble_sort(table_data, column_index, reverse)
                elif selected_algorithm == "Quick Sort":
                        sorted_data = sortingAlgorithms.quick_sort(table_data, column_index, reverse)
                elif selected_algorithm == "Selection Sort":
                        sorted_data = sortingAlgorithms.selection_sort(table_data, column_index, reverse)
                elif selected_algorithm == "Insertion Sort":
                        sorted_data = sortingAlgorithms.insertion_sort(table_data, column_index, reverse)
                elif selected_algorithm == "Merge Sort":
                        sorted_data = sortingAlgorithms.merge_sort(table_data, column_index, reverse)
                elif selected_algorithm == "Hybrid Merge Sort":
                        sorted_data = sortingAlgorithms.hybrid_merge_sort(table_data, column_index, reverse)
                elif selected_algorithm == "Counting Sort":
                        sorted_data = sortingAlgorithms.counting_sort(table_data, column_index, reverse)
                elif selected_algorithm == "Radix Sort":
                        sorted_data = sortingAlgorithms.radix_sort(table_data, column_index, reverse)
                elif selected_algorithm == "Bucket Sort":
                        sorted_data = sortingAlgorithms.bucket_sort(table_data, column_index, reverse)
                elif selected_algorithm == "Genome Sort":
                        sorted_data = sortingAlgorithms.gnome_sort(table_data, column_index, reverse)
                elif selected_algorithm == "Cycle Sort":
                        sorted_data = sortingAlgorithms.cycle_sort(table_data, column_index, reverse)
                elif selected_algorithm == "Brick Sort":
                        sorted_data = sortingAlgorithms.brick_sort(table_data, column_index, reverse)
                else:
                        return  # If no valid algorithm is selected, exit


                # End timing the sorting process
                end_time = time.time()

                # Calculate runtime
                runtime = (end_time - start_time) * 1000 

                # Update the label to display the runtime in seconds
                self.ui.label_6.setText(f"Sorting Time: {runtime:.6f} ms")
                # Update the table with the sorted data
                print(len(sorted_data))
                
                print(f"Sorted Data: {sorted_data}")
                messagebox.showinfo("Sorted", "Selected is sorted")
                self.update_table(sorted_data)

        def preprocess_release_years(self, table_data, column_index):
                # Create a new list to hold the processed data
                processed_data = []

                # Convert the release year column from strings to integers
                for row in table_data:
                        new_row = row[:]  # Make a copy of the row
                        try:
                                new_row[column_index] = int(row[column_index])
                        except ValueError:
                                print(f"Error converting {row[column_index]} to int")
                        processed_data.append(new_row)

                return processed_data

        def preprocess_durations(self, table_data, column_index):
                # Create a new list to hold the processed data
                processed_data = []

                for row in table_data:
                        new_row = row[:]  # Make a copy of the row
                        try:
                        # Extract the integer part from the string duration (e.g., "121 min")
                                duration_str = row[column_index]
                                new_row[column_index] = int(duration_str.split()[0])  # Extract the number and convert to int
                        except (ValueError, IndexError) as e:
                                print(f"Error converting {row[column_index]} to int: {e}")
                        # Append the processed row (either modified or unmodified) to the processed data
                        processed_data.append(new_row)

                return processed_data


        def get_table_data(self):
                """Retrieves data from the model to be sorted."""
                data = []
                for row in range(self.model.rowCount()):
                        row_data = []
                        for column in range(self.model.columnCount()):
                                item = self.model.item(row, column)
                                value = item.text() if item else ""
                                row_data.append(value)
                        data.append(row_data)
                return data


        def start_scraping(self):
                self.scraper_thread.start()

        def update_progress(self, value):
                self.ui.progressBar.setValue(value)

        def append_rows_to_table(self, movie_data):
                """Appends rows of movie data to the table model."""
                for row_data in movie_data:
                        items = [QStandardItem(str(field)) for field in row_data]
                        self.model.appendRow(items)

        def toggle_pause_resume(self):
                """Toggles between pausing and resuming the scraping."""
                if self.is_paused:
                        self.scraper_thread.resume()
                        self.ui.pushButton_4.setText("Pause Scraping")
                else:
                        self.scraper_thread.pause()
                        self.ui.pushButton_4.setText("Resume Scraping")
                        self.is_paused = not self.is_paused


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainApp()
    mainWindow.show()
    sys.exit(app.exec_())
