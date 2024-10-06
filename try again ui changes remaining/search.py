import sys
from PyQt5 import QtWidgets, QtCore

class YourWindowClass(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Filter & Search")

        # Central Widget
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)

        # Create table widget for displaying data
        self.table_widget = QtWidgets.QTableWidget(0, 3)  # 3 columns for example
        self.table_widget.setHorizontalHeaderLabels(["Title", "Author", "Year"])
        layout.addWidget(self.table_widget)

        # Search fields and filter dropdowns for each column
        self.title_search = QtWidgets.QLineEdit(self)
        self.title_search.setPlaceholderText("Search Title")
        self.title_filter_type = QtWidgets.QComboBox(self)
        self.title_filter_type.addItems(["Contains", "Starts With", "Ends With"])

        self.author_search = QtWidgets.QLineEdit(self)
        self.author_search.setPlaceholderText("Search Author")
        self.author_filter_type = QtWidgets.QComboBox(self)
        self.author_filter_type.addItems(["Contains", "Starts With", "Ends With"])

        self.year_search = QtWidgets.QLineEdit(self)
        self.year_search.setPlaceholderText("Search Year")
        
        # Add search fields and filter dropdowns to the layout
        search_layout = QtWidgets.QHBoxLayout()
        search_layout.addWidget(self.title_search)
        search_layout.addWidget(self.title_filter_type)
        search_layout.addWidget(self.author_search)
        search_layout.addWidget(self.author_filter_type)
        search_layout.addWidget(self.year_search)
        layout.addLayout(search_layout)

        # Connect search fields to their respective functions
        self.title_search.textChanged.connect(lambda: self.filter_data('title', self.title_search.text(), self.title_filter_type.currentText()))
        self.author_search.textChanged.connect(lambda: self.filter_data('author', self.author_search.text(), self.author_filter_type.currentText()))
        self.year_search.textChanged.connect(lambda: self.filter_data('year', self.year_search.text()))

        # Example data
        self.data = [
            {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": "1951"},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": "1960"},
            {"title": "1984", "author": "George Orwell", "year": "1949"},
            {"title": "Moby-Dick", "author": "Herman Melville", "year": "1851"},
        ]

        self.populate_table(self.data)

    def populate_table(self, data):
        """ Populate the table widget with data """
        self.table_widget.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            self.table_widget.setItem(row_num, 0, QtWidgets.QTableWidgetItem(row_data["title"]))
            self.table_widget.setItem(row_num, 1, QtWidgets.QTableWidgetItem(row_data["author"]))
            self.table_widget.setItem(row_num, 2, QtWidgets.QTableWidgetItem(row_data["year"]))

    def filter_data(self, column, text, filter_type="Contains"):
        """ Filter data based on input text and filter type """
        if column == 'title':
            col = 0
        elif column == 'author':
            col = 1
        elif column == 'year':
            col = 2
        else:
            return

        filtered_data = []
        for row in self.data:
            if col == 0:
                value = row["title"].lower()
            elif col == 1:
                value = row["author"].lower()
            else:
                value = row["year"].lower()

            if filter_type == "Contains" and text.lower() in value:
                filtered_data.append(row)
            elif filter_type == "Starts With" and value.startswith(text.lower()):
                filtered_data.append(row)
            elif filter_type == "Ends With" and value.endswith(text.lower()):
                filtered_data.append(row)

        self.populate_table(filtered_data)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = YourWindowClass()
    window.show()
    sys.exit(app.exec_())
