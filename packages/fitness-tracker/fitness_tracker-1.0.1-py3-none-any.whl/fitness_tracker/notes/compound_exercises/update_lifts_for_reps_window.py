import json
import os
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QFormLayout, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import pyqtSignal, Qt
from fitness_tracker.database_wrapper import DatabaseWrapper

class UpdateLiftsForRepsWindow(QWidget):
  change_lifts_for_reps_signal = pyqtSignal(bool)
  history_signal = pyqtSignal(bool)

  def __init__(self):
    super().__init__()
    self.db_wrapper = DatabaseWrapper()
    self.table_name = "Compound Exercises"
    self.setStyleSheet("""
    QWidget{
      background-color: #232120;
      font-weight: bold;
      color:#c7c7c7;
    }
    QPushButton{
      background-color: rgba(0, 0, 0, 0);
      border: 1px solid;
      font-size: 18px;
      font-weight: bold;
      border-color: #808080;
      min-height: 28px;
      white-space:nowrap;
      text-align: center;
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
    }
    """) 
    self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
    self.setWindowModality(Qt.ApplicationModal)
    self.units = "kg" if self.db_wrapper.fetch_local_column("Users", "units") == "metric" else "lb"
    self.preferred_lifts = json.loads(self.db_wrapper.fetch_local_column(self.table_name, "preferred_lifts"))
    self.setWindowTitle("Update Lifts For Reps")
    self.setLayout(self.create_panel())
    self.set_line_edit_values()

  def create_panel(self):
    form_layout = QFormLayout()
    
    exercise_label = QLabel("Exercise")
    header_layout = QHBoxLayout()
    reps_label = QLabel("Reps")
    weight_label = QLabel("Weight")
    header_layout.addWidget(reps_label)
    header_layout.addWidget(weight_label)

    horizontal_press_label = QLabel(self.preferred_lifts["Horizontal Press"])
    self.horizontal_press_reps_edit = QLineEdit()
    self.horizontal_press_reps_edit.setValidator(QIntValidator())
    x_label = QLabel("x")
    self.horizontal_press_edit = QLineEdit() 
    self.horizontal_press_edit.setValidator(QIntValidator())
    units_label = QLabel(self.units)
    hbox = QHBoxLayout()
    hbox.addWidget(self.horizontal_press_reps_edit)
    hbox.addWidget(x_label)
    hbox.addWidget(self.horizontal_press_edit)
    hbox.addWidget(units_label)

    floor_pull_label = QLabel(self.preferred_lifts["Floor Pull"])
    self.floor_pull_reps_edit = QLineEdit()
    self.floor_pull_reps_edit.setValidator(QIntValidator())
    x_label1 = QLabel("x")
    self.floor_pull_edit = QLineEdit()
    self.floor_pull_edit.setValidator(QIntValidator())
    units_label1 = QLabel(self.units)
    hbox1 = QHBoxLayout()
    hbox1.addWidget(self.floor_pull_reps_edit)
    hbox1.addWidget(x_label1)
    hbox1.addWidget(self.floor_pull_edit)
    hbox1.addWidget(units_label1)

    squat_label = QLabel(self.preferred_lifts["Squat"])
    self.squat_reps_edit = QLineEdit()
    self.squat_reps_edit.setValidator(QIntValidator())
    x_label2 = QLabel("x")
    self.squat_edit = QLineEdit()
    self.squat_edit.setValidator(QIntValidator())
    units_label2 = QLabel(self.units)
    hbox2 = QHBoxLayout()
    hbox2.addWidget(self.squat_reps_edit)
    hbox2.addWidget(x_label2)
    hbox2.addWidget(self.squat_edit)
    hbox2.addWidget(units_label2)

    vertical_press_label = QLabel("Overhead Press")
    self.vertical_press_reps_edit = QLineEdit()
    self.vertical_press_reps_edit.setValidator(QIntValidator())
    x_label3 = QLabel("x")
    self.vertical_press_edit = QLineEdit()
    self.vertical_press_edit.setValidator(QIntValidator())
    units_label3 = QLabel(self.units)
    hbox3 = QHBoxLayout()
    hbox3.addWidget(self.vertical_press_reps_edit)
    hbox3.addWidget(x_label3)
    hbox3.addWidget(self.vertical_press_edit)
    hbox3.addWidget(units_label3)

    buttons_layout = QHBoxLayout()
    save_button = QPushButton("Save")
    save_button.clicked.connect(lambda: self.save_lifts_for_reps())
    cancel_button = QPushButton("Cancel")
    cancel_button.clicked.connect(lambda: self.close_update_lifts_for_reps())
    buttons_layout.addWidget(save_button)
    buttons_layout.addWidget(cancel_button)  
    
    form_layout.addRow(exercise_label, header_layout)
    form_layout.addRow(horizontal_press_label, hbox)
    form_layout.addRow(floor_pull_label, hbox1)
    form_layout.addRow(squat_label, hbox2)
    form_layout.addRow(vertical_press_label, hbox3)
    
    main_layout = QVBoxLayout()
    main_layout.addLayout(form_layout)
    main_layout.addLayout(buttons_layout)
    
    return main_layout

  def save_lifts_for_reps(self):
    try:
      fetched_lifts_for_reps = json.loads(self.db_wrapper.fetch_local_column(self.table_name, "lifts_for_reps"))
      exercises = list(fetched_lifts_for_reps.keys())
      horizontal_press_weight = str(float(self.horizontal_press_edit.text()))
      floor_pull_weight = str(float(self.floor_pull_edit.text()))
      squat_weight = str(float(self.squat_edit.text()))
      vertical_press_weight = str(float(self.vertical_press_edit.text()))

      horizontal_press_reps = str(float(self.horizontal_press_reps_edit.text())) 
      floor_pull_reps = str(float(self.floor_pull_reps_edit.text()))
      squat_reps = str(float(self.squat_reps_edit.text()))
      vertical_press_reps = str(float(self.vertical_press_reps_edit.text()))
    
      new_lifts_for_reps = {exercises[0]: [horizontal_press_reps, horizontal_press_weight],
                            exercises[1]: [floor_pull_reps, floor_pull_weight],
                            exercises[2]: [squat_reps, squat_weight],
                            exercises[3]: [vertical_press_reps, vertical_press_weight]}
      diff = self.lift_difference(new_lifts_for_reps, fetched_lifts_for_reps, lifts_reps=True)
      self.db_wrapper.update_table_column(self.table_name, "lift_history", diff)
      self.history_signal.emit(True)
      self.db_wrapper.update_table_column(self.table_name, "lifts_for_reps", new_lifts_for_reps) 
      self.change_lifts_for_reps_signal.emit(True)
      self.set_line_edit_values()
      self.close()
    except ValueError:
      pass
  
  def close_update_lifts_for_reps(self):
    self.close()
    self.set_line_edit_values()

  def set_line_edit_values(self):
    lift_values = list(json.loads(self.db_wrapper.fetch_local_column(self.table_name, "lifts_for_reps")).values())
    reps = [lift[0] for lift in lift_values]
    weight = [lift[1] for lift in lift_values]
    
    reps_line_edit = [self.horizontal_press_reps_edit,
                      self.floor_pull_reps_edit,
                      self.squat_reps_edit,
                      self.vertical_press_reps_edit]

    weight_line_edit = [self.horizontal_press_edit,
                        self.floor_pull_edit,
                        self.squat_edit,
                        self.vertical_press_edit]

    for i, line_edit in enumerate(reps_line_edit):
      line_edit.setText(reps[i])

    for i, line_edit in enumerate(weight_line_edit):
      line_edit.setText(weight[i])

  def sort_exercises(self, exercise):
    if exercise in ["Bench Press", "Incline Bench Press"]: return 4
    elif exercise in ["Deadlift", "Sumo Deadlift"]: return 3
    elif exercise in ["Back Squat", "Front Squat"]: return 2
    elif exercise in ["Overhead Press", "Push Press"]: return 1 

  # returns sorted dictionary containing updated lifts
  def lift_difference(self, new_lifts, old_lifts, one_RM=False, lifts_reps=False):
    difference = None
    if one_RM:
      db_lifts = set(": ".join([exercise, weight]) for exercise, weight in old_lifts.items())
      new_lifts = set(": ".join([exercise, weight]) for exercise, weight in new_lifts.items() if not weight == '0.0')
      diff = list(new_lifts.difference(db_lifts)) # local lifts that are not in db
      difference = {exercise.split(": ")[0]:exercise.split(": ")[1] for exercise in diff}
    elif lifts_reps:
      db_lifts = set(":".join([exercise, "x".join(values)]) for exercise, values in old_lifts.items())
      new_lifts = set(":".join([exercise, "x".join(values)]) for exercise, values in new_lifts.items() if not values[1] == '0.0')
      diff = list(new_lifts.difference(db_lifts))
      difference = {exercise.split(":")[0]:exercise.split(":")[1].split("x") for exercise in diff}
    return {key: value for key, value in sorted(difference.items(), key=lambda exercise: self.sort_exercises(exercise[0]))}
