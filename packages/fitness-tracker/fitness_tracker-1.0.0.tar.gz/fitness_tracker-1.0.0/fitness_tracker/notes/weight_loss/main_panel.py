import json
import matplotlib
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel, QHBoxLayout, QComboBox, QFrame, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
from fitness_tracker.database_wrapper import DatabaseWrapper
from fitness_tracker.common.units_conversion import kg_to_pounds, pounds_to_kg
from .weight_loss_edit_dialog import WeightLossEditDialog
from .weight_loss_history import WeightLossHistory
from .calories_burnt_dialog import CaloriesBurntDialog
from .cardio_history import CardioHistory
from fitness_tracker.notes.weight_loss.weight_loss_graph import WeightLossGraphCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

matplotlib.use("Qt5Agg")

class MainPanel(QWidget):
  def __init__(self, parent):
    super().__init__(parent)
    self.db_wrapper = DatabaseWrapper()
    self.table_name = "Weight Loss"
    self.setStyleSheet("""
    QWidget{
      color:#c7c7c7;
      font-weight: bold;
    }
    QPushButton{
      background-color: rgba(0, 0, 0, 0);
      border: 1px solid;
      font-size: 18px;
      font-weight: bold;
      border-color: #808080;
      min-height: 28px;
      white-space:nowrap;
      text-align: left;
      padding-left: 5%;
      font-family: Montserrat;
    }
    QPushButton:hover:!pressed{
      border: 2px solid;
      border-color: #747474;
    }
    QPushButton:pressed{
      border: 2px solid;
      background-color: #323232;
      border-color: #6C6C6C;
    }
    QComboBox{
      border-radius: 4px;
      font-size: 18px;
      font-weight: bold;
      white-space:nowrap;
      text-align: left;
      padding-left: 5%;
      font-family: Montserrat;
      min-height: 28px;
      background-color: #440D0F;
    }
    QComboBox:down-arrow{
      width: 0px;
      height: 0px;
      background: #d3d3d3; 
      opacity:0
    }
    QComboBox:drop-down{
      background-color: #440D0F;
      border: 0px;
      opacity:0;
      border-radius: 0px;
      width: 0px;
      height: 0px;
    }
    QComboBox:hover:!pressed{
      background-color: #5D1A1D;
    }
    QComboBox:pressed{
      background-color: #551812;
    }
    """) 
    
    self.db_wrapper.create_local_table(self.table_name)
    self.db_wrapper.create_local_table("Nutrition")
   
    if self.db_wrapper.local_table_is_empty("Nutrition"):
      self.db_wrapper.insert_default_values("Nutrition") 
    
    if self.db_wrapper.local_table_is_empty(self.table_name):
      self.db_wrapper.insert_default_values(self.table_name)
    
    self.fetch_user_data()
    self.date = datetime.today().strftime("%d/%m/%Y")
    self.current_year = datetime.today().year
    self.calorie_goal = self.db_wrapper.fetch_local_column("Nutrition", "calorie_goal")
    
    self.units = "kg" if self.db_wrapper.fetch_local_column("Users", "units") == "metric" else "lb"
    weight_loss_units = "kg" if self.db_wrapper.fetch_local_column(self.table_name, "units") == "metric" else "lb"
    self.weight_history = json.loads(self.db_wrapper.fetch_local_column(self.table_name, "weight_history"))
    
    if self.units != weight_loss_units:
      units_name = "metric" if self.units == "kg" else "imperial"
      self.db_wrapper.update_table_column(self.table_name, "units", units_name)
      if units_name == "metric":
        for date in self.weight_history:
          self.weight_history[date] = str(pounds_to_kg(self.weight_history[date]))
      
      elif units_name == "imperial":
        for date in self.weight_history:
          self.weight_history[date] = str(kg_to_pounds(self.weight_history[date]))

      self.db_wrapper.update_table_column(self.table_name, "weight_history", json.dumps(self.weight_history))

    self.preferred_activity = self.db_wrapper.fetch_local_column(self.table_name, "preferred_activity")
    self.cardio_history = json.loads(self.db_wrapper.fetch_local_column(self.table_name, "cardio_history"))
    if not self.date in self.cardio_history: self.add_date_to_cardio_history()
    if not self.date in self.weight_history: self.add_date_to_weight_history()
    
    self.init_cardio_labels()
    self.create_panel()

  def create_panel(self):
    grid = QGridLayout()
    grid.addLayout(self.create_description(), 0, 0, 1, 1)
    grid.addWidget(self.create_graph(), 1, 0, 4, 1)
    grid.addLayout(self.create_bottom_layout(), 5, 0, 3, 1)
    self.setLayout(grid)

  def create_description(self):
    description = QVBoxLayout()
    description_font = QFont("Montserrat", 12)
    description_label = QLabel("Keep notes and track your weight loss journey.", self)
    description_label.setFont(description_font)
    description_label.setFixedHeight(20)
    description.addWidget(description_label)
    return description

  def create_graph(self):
    self.graph_layout = QVBoxLayout()
    
    graph = WeightLossGraphCanvas(self.db_wrapper.months[datetime.today().month-1], self.current_year, self)
    toolbar = NavigationToolbar(graph, self)
    toolbar.setStyleSheet("background-color: white;") 
    
    combobox_layout = QHBoxLayout()
    self.months_combobox = QComboBox()

    months = []
    for entry in self.weight_history:
      month = entry.split("/")[1]
      for month_name, code in self.db_wrapper.months_mappings.items():
        if code == month: month = month_name
      if not month in months:
        months.append(month)
    if len(months) == 0: months.append(self.db_wrapper.months[datetime.today().month-1])
    self.months_combobox.addItems(months)
    self.months_combobox.setCurrentText(self.db_wrapper.months[datetime.today().month-1])
    self.months_combobox.currentTextChanged.connect(lambda month: self.change_month_graph(month))
    
    self.change_year_combobox = QComboBox()
    
    years = []
    for entry in self.weight_history:
      if not entry.split("/")[-1] in years: years.append(entry.split("/")[-1])
    if len(years) == 0: years.append(str(self.current_year))
    self.change_year_combobox.addItems(list(reversed(years)))
    self.change_year_combobox.currentTextChanged.connect(lambda year: self.change_year_graph(year))

    combobox_layout.addWidget(self.months_combobox)
    combobox_layout.addWidget(self.change_year_combobox)

    self.graph_layout.addWidget(toolbar)
    self.graph_layout.addWidget(graph)
    self.graph_layout.addLayout(combobox_layout)

    framed_graph = QFrame(self)
    framed_graph.setFrameStyle(QFrame.Box)
    framed_graph.setLineWidth(3)
    framed_graph.setLayout(self.graph_layout)

    return framed_graph

  def create_bottom_layout(self):
    bottom_layout = QHBoxLayout()
    bottom_layout.addWidget(self.create_weight_loss())
    bottom_layout.addWidget(self.create_cardio_notes())
    return bottom_layout
  
  def create_weight_loss(self):
    weight_loss = QVBoxLayout()
    main_label = QLabel("Weight Loss")
    main_label.setFont(QFont("Ariel", 18, weight=QFont.Bold))

    current_weight_layout = QHBoxLayout()
    self.current_weight_label = QLabel(" ".join(["Current Weight:", self.current_weight, self.units]))
    update_current_weight_button = QPushButton("Update")
    update_current_weight_button.clicked.connect(lambda: self.update_value("Current Weight", self.current_weight))
    current_weight_layout.addWidget(self.current_weight_label)
    current_weight_layout.addWidget(update_current_weight_button)

    weight_goal_layout = QHBoxLayout()
    self.weight_goal_label = QLabel(" ".join(["Weight Goal:",  self.goal_weight, self.units]))
    update_weight_goal_label = QPushButton("Update")
    update_weight_goal_label.clicked.connect(lambda: self.update_value("Weight Goal", self.goal_weight))
    weight_goal_layout.addWidget(self.weight_goal_label)
    weight_goal_layout.addWidget(update_weight_goal_label)
   
    loss_per_week_layout = QHBoxLayout()
    self.loss_per_week_label = QLabel(" ".join(["Loss Per Week:", str(self.loss_per_week), self.units])) 
    update_loss_per_week_label = QPushButton("Update")
    update_loss_per_week_label.clicked.connect(lambda: self.update_value("Loss Per Week", self.loss_per_week))
    loss_per_week_layout.addWidget(self.loss_per_week_label)
    loss_per_week_layout.addWidget(update_loss_per_week_label)

    calorie_intake_layout = QHBoxLayout()
    calorie_intake_label = QLabel(" ".join(["Calorie Intake:", str(self.calorie_goal), "kcal"]))
    calorie_intake_layout.addWidget(calorie_intake_label)
    
    history_layout = QHBoxLayout()
    weight_loss_history_button = QPushButton("History")
    weight_loss_history_button.clicked.connect(lambda: self.show_weight_history())
    history_layout.addWidget(weight_loss_history_button)   
    
    weight_loss.addWidget(main_label)
    weight_loss.addLayout(calorie_intake_layout)
    weight_loss.addLayout(current_weight_layout)
    weight_loss.addLayout(weight_goal_layout)
    weight_loss.addLayout(loss_per_week_layout)
    weight_loss.addLayout(history_layout)

    weight_loss.setSpacing(5)
    framed_layout = QFrame()
    framed_layout.setObjectName("graphObj")
    framed_layout.setFrameStyle(QFrame.Box)
    framed_layout.setLineWidth(3)
    framed_layout.setStyleSheet("""#graphObj {color: #322d2d;}""")
    
    framed_layout.setLayout(weight_loss)
    
    return framed_layout

  def create_cardio_notes(self):
    cardio_notes = QVBoxLayout()
    main_label = QLabel("Cardio Notes")
    main_label.setFont(QFont("Ariel", 18, weight=QFont.Bold))
    
    preferred_activity_layout = QHBoxLayout()
    self.preferred_activity_label = QLabel(" ".join(["Preferred Activity:", self.preferred_activity]))
    self.preferred_activity_dropdown = QComboBox()
    self.preferred_activity_dropdown.addItems(["Running", "Walking", "Cycling", "Swimming"])
    self.preferred_activity_dropdown.setCurrentText(self.preferred_activity)
    self.preferred_activity_dropdown.currentTextChanged.connect(lambda activity: self.set_new_preferred_activity(activity))

    preferred_activity_layout.addWidget(self.preferred_activity_label)
    preferred_activity_layout.addWidget(self.preferred_activity_dropdown)

    time_spent_layout = QHBoxLayout()
    self.time_spent_label = QLabel(" ".join(["Time Spent:", self.time_spent, "min"]))
    update_time_spent_label = QPushButton("Update")
    update_time_spent_label.clicked.connect(lambda: self.update_value("Time Spent", self.time_spent))
    time_spent_layout.addWidget(self.time_spent_label)
    time_spent_layout.addWidget(update_time_spent_label)

    calories_burnt_layout = QHBoxLayout()
    self.calories_burnt_label = QLabel(" ".join(["Calories Burnt:", self.calories_burnt, "kcal"]))
    update_calories_burnt_label = QPushButton("Update")
    update_calories_burnt_label.clicked.connect(lambda: self.update_value("Calories Burnt", self.calories_burnt))
    calories_burnt_layout.addWidget(self.calories_burnt_label)
    calories_burnt_layout.addWidget(update_calories_burnt_label)

    distance_travelled_layout = QHBoxLayout()
    self.distance_travelled_label = QLabel(" ".join(["Distance Travelled:", self.distance_travelled, "m"]))
    update_distance_travelled_label = QPushButton("Update")
    update_distance_travelled_label.clicked.connect(lambda: self.update_value("Distance Travelled", self.distance_travelled))
    distance_travelled_layout.addWidget(self.distance_travelled_label)
    distance_travelled_layout.addWidget(update_distance_travelled_label)
    
    history_layout = QHBoxLayout()
    cardio_history_button = QPushButton("History")
    cardio_history_button.clicked.connect(lambda: self.show_cardio_history())
    self.save_changes_cardio_button = QPushButton("Save Changes")
    self.save_changes_cardio_button.clicked.connect(lambda: self.add_cardio_entry_to_cardio_history())
    history_layout.addWidget(cardio_history_button)
    history_layout.addWidget(self.save_changes_cardio_button)
    
    cardio_notes.addWidget(main_label)
    cardio_notes.addLayout(preferred_activity_layout)
    cardio_notes.addLayout(time_spent_layout)
    cardio_notes.addLayout(distance_travelled_layout)
    cardio_notes.addLayout(calories_burnt_layout)
    cardio_notes.addLayout(history_layout)

    cardio_notes.setSpacing(5)
    framed_layout = QFrame()
    framed_layout.setObjectName("graphObj")
    framed_layout.setFrameStyle(QFrame.Box)
    framed_layout.setLineWidth(3)
    framed_layout.setStyleSheet("""#graphObj {color: #322d2d;}""")
    
    framed_layout.setLayout(cardio_notes)
    
    return framed_layout

  def update_value(self, to_edit, old_value):
    fitness_goal = None
    date = None
    if not to_edit == "Calories Burnt":
      if to_edit == "Loss Per Week": fitness_goal = self.user_data["Goal Params"][0]
      elif to_edit == "Current Weight": date = self.date
      self.dialog = WeightLossEditDialog(to_edit, old_value, fitness_goal, date)
      self.dialog.update_label_signal.connect(lambda label_to_update: self.update_weight_loss_label(label_to_update))
      self.dialog.update_cardio_notes_signal.connect(lambda value_to_update: self.update_cardio_notes_label(to_edit, value_to_update))
      self.dialog.update_graph_signal.connect(lambda signal: self.refresh_graph(signal))
    else:
      self.dialog = CaloriesBurntDialog(to_edit, old_value, self.time_spent, self.distance_travelled, self.preferred_activity, self.current_weight)
      self.dialog.update_calories_label_signal.connect(lambda value_to_update: self.update_cardio_notes_label(to_edit, value_to_update))
    self.dialog.show()
  
  @pyqtSlot(bool)
  def update_weight_loss_label(self, signal):
    if signal:
      self.fetch_user_data()
      self.current_weight_label.setText(" ".join(["Current Weight:", str(self.current_weight), self.units]))
      self.weight_goal_label.setText(" ".join(["Weight Goal:", str(self.goal_weight), self.units]))
      self.loss_per_week_label.setText(" ".join(["Loss Per Week:", str(self.loss_per_week), self.units]))
  
  @pyqtSlot(str)
  def update_cardio_notes_label(self, to_edit, value_to_update):
    if to_edit == "Time Spent":
      self.time_spent = value_to_update
      self.time_spent_label.setText(" ".join(["Time Spent:", str(value_to_update), "min"]))
    elif to_edit == "Distance Travelled":
      self.distance_travelled = value_to_update
      self.distance_travelled_label.setText(" ".join(["Distance Travelled:", str(value_to_update), "m"]))
    elif to_edit == "Calories Burnt":
      self.calories_burnt = value_to_update
      self.calories_burnt_label.setText(" ".join(["Calories Burnt", str(value_to_update), "kcal"]))

  def fetch_user_data(self):
    self.user_data = self.db_wrapper.fetch_local_user_info()
    self.current_weight = self.user_data["Weight"]
    self.goal_weight = self.user_data["Weight Goal"]
    self.loss_per_week = self.user_data["Goal Params"][1]

  def show_weight_history(self):
    self.history = WeightLossHistory()
    self.history.update_weight_loss_label_signal.connect(lambda signal: self.update_weight_loss_label(signal))
    self.history.setGeometry(100, 200, 300, 300) 
    self.history.show()
  
  def show_cardio_history(self):
    self.cardio_history_dialog = CardioHistory()
    self.cardio_history_dialog.refresh_cardio_labels_signal.connect(lambda signal: self.refresh_cardio_notes(signal))
    self.cardio_history_dialog.setGeometry(100, 200, 300, 300)
    self.cardio_history_dialog.show()
  
  @pyqtSlot(bool)
  def refresh_cardio_notes(self, signal):
    if signal:
      self.cardio_history = json.loads(self.db_wrapper.fetch_local_column(self.table_name, "cardio_history"))
      self.init_cardio_labels()
      self.time_spent_label.setText(" ".join(["Time Spent:", self.time_spent, "min"]))
      self.distance_travelled_label.setText(" ".join(["Distance Travelled:", self.distance_travelled, "m"]))
      self.calories_burnt_label.setText(" ".join(["Calories Burnt:", self.calories_burnt, "kcal"]))

  def set_new_preferred_activity(self, activity):
    self.preferred_activity = activity
    self.preferred_activity_label.setText(" ".join(["Preferred Activity:", activity]))
    self.preferred_activity_dropdown.setCurrentText(activity)
    self.db_wrapper.update_table_column(self.table_name, "preferred_activity", self.preferred_activity)
    self.init_cardio_labels()
    self.time_spent_label.setText(" ".join(["Time Spent:", self.time_spent, "min"]))
    self.distance_travelled_label.setText(" ".join(["Distance Travelled:", self.distance_travelled, "m"]))
    self.calories_burnt_label.setText(" ".join(["Calories Burnt:", self.calories_burnt, "kcal"]))

  def init_cardio_labels(self):
    if len(self.cardio_history[self.date][self.preferred_activity]) > 0:
      self.today_exercise = self.cardio_history[self.date][self.preferred_activity][-1]
      self.time_spent = self.today_exercise["Time Spent"]
      self.distance_travelled = self.today_exercise["Distance Travelled"]
      self.calories_burnt = self.today_exercise["Calories Burnt"]
    else:
      self.time_spent = "0"
      self.distance_travelled = "0"
      self.calories_burnt = "0"
  
  def add_date_to_cardio_history(self):
    activities = ["Running", "Walking", "Cycling", "Swimming"]
    self.cardio_history[self.date] = {}
    for activity in activities:
      self.cardio_history[self.date][activity] = []
  
    cardio_history = json.dumps(self.cardio_history) 
    self.db_wrapper.update_table_column(self.table_name, "cardio_history", cardio_history)

  def add_cardio_entry_to_cardio_history(self):
    date = datetime.today().strftime("%d/%m/%Y")
    new_entry = {"Time Spent": str(self.time_spent), "Distance Travelled": str(self.distance_travelled),
                 "Calories Burnt": str(self.calories_burnt)}
    self.cardio_history[date][self.preferred_activity].append(new_entry)
    current_cardio_history = json.dumps(self.cardio_history) 
    self.db_wrapper.update_table_column(self.table_name, "cardio_history", current_cardio_history)

  def add_date_to_weight_history(self):
    try:
      last_entry = list(self.weight_history.values())[-1]
      self.weight_history[self.date] = last_entry
      self.db_wrapper.update_table_column(self.table_name, "weight_history", json.dumps(self.weight_history))
    except IndexError: # no records
      pass
  
  @pyqtSlot(bool)
  def refresh_graph(self, signal):
    if signal:
      self.weight_history = self.db_wrapper.fetch_local_column(self.table_name, "weight_history")
      self.replace_graph(str(self.months_combobox.currentText()))

  def replace_graph(self, month):
    new_graph = WeightLossGraphCanvas(month, self.current_year, self)
    new_toolbar = NavigationToolbar(new_graph, self)
    
    old_toolbar_reference = self.graph_layout.itemAt(0).widget()
    old_graph_reference = self.graph_layout.itemAt(1).widget()

    self.graph_layout.replaceWidget(old_toolbar_reference, new_toolbar)
    self.graph_layout.replaceWidget(old_graph_reference, new_graph)
  
  def change_year_graph(self, year):
    self.current_year = year
    self.replace_graph(str(self.months_combobox.currentText()))

  def change_month_graph(self, month):
    self.replace_graph(str(month))
