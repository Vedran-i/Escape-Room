import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QInputDialog
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

class AdventureGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Escape Room")
        self.setGeometry(600, 200, 950, 550)

        # Game variables
        self.Have_Key = False
        self.Safe_check = False
        self.name = ""
        self.current_room = "start"
        self.taken = False
        self.opened = False
        self.com2_check = False
        self.com2cleared = False
        self.com1_cleared = False
        self.painting_checked = False
        self.disk = False
        self.coat_check = False
        self.cabinet_check = False
        self.currency = 0

        # Layout
        self.layout = QVBoxLayout()

        # Widgets
        self.message_label = QLabel("Welcome!\nYou are a secret agent and you have infiltrated an office building.\nYour goal is to leave the building with as much money as possible. Good luck.\n\nEnter your name to start the game.")
        self.message_label.setFont(QFont("Calibri", 19))  # Larger font for the message
        self.layout.addWidget(self.message_label)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter your name here...")
        self.input_field.setFont(QFont("Arial", 14))  # Larger font for input
        self.input_field.returnPressed.connect(self.start_game)
        self.layout.addWidget(self.input_field)

        self.button_1 = QPushButton("Option 1")
        self.button_2 = QPushButton("Option 2")
        self.button_3 = QPushButton("Option 3")
        self.button_4 = QPushButton("Option 4")
        self.button_5 = QPushButton("Option 5")

        # Set larger font for buttons
        self.button_1.setFont(QFont("Arial", 14))
        self.button_2.setFont(QFont("Arial", 14))
        self.button_3.setFont(QFont("Arial", 14))
        self.button_4.setFont(QFont("Arial", 14))
        self.button_5.setFont(QFont("Arial", 14))

        self.button_1.clicked.connect(lambda: self.handle_choice(1))
        self.button_2.clicked.connect(lambda: self.handle_choice(2))
        self.button_3.clicked.connect(lambda: self.handle_choice(3))
        self.button_4.clicked.connect(lambda: self.handle_choice(4))
        self.button_5.clicked.connect(lambda: self.handle_choice(5))

        self.layout.addWidget(self.button_1)
        self.layout.addWidget(self.button_2)
        self.layout.addWidget(self.button_3)
        self.layout.addWidget(self.button_4)
        self.layout.addWidget(self.button_5)


        # Initially hide buttons
        self.toggle_buttons(False)

        self.setLayout(self.layout)

    def toggle_buttons(self, show):
        """Show or hide buttons."""
        self.button_1.setVisible(show)
        self.button_2.setVisible(show)
        self.button_3.setVisible(show)
        self.button_4.setVisible(show)
        self.button_5.setVisible(show)

    def start_game(self):
        # Start game by entering player's name
        self.name = self.input_field.text().strip()
        if self.name:
            self.message_label.setText(f"Hello {self.name}! Welcome to the game.")
            self.input_field.hide()
            self.toggle_buttons(True)
            self.room_1()
        else:
            self.message_label.setText("Please enter a valid name to start the game.")

    def room_1(self):

        self.current_room = "room_1"
        self.message_label.setText("You are in a room 1. What do you do?\n\n 📚  🗃️  🚪")
        self.button_1.setText("1. Check bookcase")
        self.button_2.setText("2. Check desk")
        self.button_3.setText("3. Go to Door")
        self.button_4.setText("")
        self.button_5.setText("")

    def room_2(self):

        self.current_room = "room_2"
        self.message_label.setText("You are now in room 2. What do you do?\n\n 🖨️   🗄️   🗑️")
        self.button_1.setText("1. Check printer")
        self.button_2.setText("2. Check cabinet")
        self.button_3.setText("3. Check trash can")
        self.button_4.setText("4. Go to next room")
        self.button_5.setText("4. Go to previous room")


    def room_3(self):

        self.current_room = "room_3"
        self.message_label.setText("You are now in room 3. What do you do?\n\n 📦    🗺️  ")
        self.button_1.setText("1. Check box")
        self.button_2.setText("2. Check map")
        self.button_3.setText("3. Go to next room")
        self.button_4.setText("4. Go to previous room")
        self.button_5.setText("")

    def room_4(self):

        self.current_room = "room_4"
        self.message_label.setText("You are in room 4. There's a vent on the ceiling... Maybe you can reach it somehow?\n\n   🔳\n\n 🧱 🪑     💻   🖼️  ")
        self.button_1.setText("1. Check bricks")
        self.button_2.setText("2. Check computer")
        self.button_3.setText("3. Check painting")
        self.button_4.setText("3. Go to next room")
        self.button_5.setText("4. Go to previous room")

    def room_5(self):

        self.current_room = "room_5"
        self.message_label.setText("You are in room 5. What do you do?\n\n 💻    📅️")
        self.button_1.setText("1. Check computer")
        self.button_2.setText("2. Check calendar")
        self.button_3.setText("3. Go to next room")
        self.button_4.setText("4. Go to previous room")
        self.button_5.setText("")

    def room_6(self):

        self.current_room = "room_6"
        self.message_label.setText("You are now in the last room. What do you do?\n\n 📃  🗄️   🧥    🚪")
        self.button_1.setText("1. Check paper")
        self.button_2.setText("2. Check safe")
        self.button_3.setText("3. Check coat")
        self.button_4.setText("4. Go to exit")
        self.button_5.setText("5. Go to previous room")



    def end_game(self, success):

        if success:
            self.message_label.setText(
                f"You left the building with ${self.currency},000! 😎\nThank you for playing, {self.name}!"
            )
        else:
            self.message_label.setText(
                f"You left the building with ${self.currency},000!\nThank you for playing, {self.name}!"
            )
        self.toggle_buttons(False)

    def handle_choice(self, choice):
        """Handle the player's choices in the current room."""
        if self.current_room == "room_1":
            if choice == 1:
                self.message_label.setText("There's just books here... 📚")
            elif choice == 2:
                if self.taken:
                    self.message_label.setText("There's nothing here.")
                else:
                    self.message_label.setText("You found a key! 🔑")
                    self.Have_Key = True
                    self.taken = True
            elif choice == 3:
                if not self.Have_Key:
                    self.message_label.setText("The door is locked.")
                else:
                    self.message_label.setText("You used the key and unlocked the door.")
                    QTimer.singleShot(2200, self.room_2)  # 2-second delay before moving to room 2





        if self.current_room == "room_2":
            if choice == 1:
                self.message_label.setText("You checked the printer and found clue #1:\n'It has two of the same consonants next to each other'")
            elif choice == 2:
                if self.cabinet_check:
                    self.message_label.setText("The cabinet is empty")
                else:
                    self.message_label.setText("You found $10,000!💵💵💵")
                    self.currency +=10
                    self.cabinet_check = True

            elif choice == 3:
                self.message_label.setText(
                    '<span style="font-size:25px;">'
                    'You checked the trashcan and found a newspaper.<br><br>'
                    '<span style="font-size:18px;">'
                    '<b>S</b>tock prices across major indices experienced fluctuations on Monday, with tech sectors showing resilience.<br>'
                    '<b>E</b>lectric vehicle manufacturers reported increased sales figures, signaling strong demand in green energy transition.<br>'
                    '<b>C</b>onsumer confidence, however, showed a slight dip as inflation concerns persisted.<br>'
                    '<b>R</b>etail businesses prepared for the holiday season by ramping up discounts and promotions to attract shoppers.<br>'
                    '<b>E</b>uropean markets remained cautiously optimistic amid global economic uncertainty, with a focus on energy.<br>'
                    '<b>T</b>rade agreements between key nations are also being closely watched as they could shape the economic landscape.'
                    '</span>'
                )



            elif choice == 4:
                self.message_label.setText("You walk into the next room...")
                QTimer.singleShot(2000, self.room_3)  # 2-second delay before moving between rooms
            elif choice == 5:
                self.message_label.setText("You return to the previous room...")
                QTimer.singleShot(2000, self.room_1)



        if self.current_room == "room_3":
            if choice == 1:
                self.message_label.setText("You opened the box and found clue #2:\n'The last letter is 'R'")
            elif choice == 2:
                if self.taken:
                    self.message_label.setText("You checked the map.\nFrance is circled for some reason... ")
            elif choice == 3:
                self.message_label.setText("You walk into the next room...")
                QTimer.singleShot(2000, self.room_4)
            elif choice == 4:
                self.message_label.setText("You return to the previous room...")
                QTimer.singleShot(2000, self.room_2)



        if self.current_room == "room_4":
            if choice == 1:
                self.message_label.setText("You found some bricks in the corner. What do you want to do with them?")
                code, ok = QInputDialog.getText(
                    self, "What do you do?", "(Action + Object):"
                )
                if ok and code.lower() == "stack bricks" or "build tower" or "stack + bricks" or "build + tower" or "put + bricks" or "put bricks" or "build bricks" or "build + bricks":
                    self.message_label.setText("You stacked the bricks on the chair and climbed to reach the vent.\nYou found clue #3:\n'The 'A' comes before 'E'")


            elif choice == 2:

                if self.disk:

                    if self.com1_cleared:
                        self.message_label.setText("You already cleared the computer.")

                    else:
                        self.message_label.setText("You booted up the computer with the disk. 💾")
                        code, ok = QInputDialog.getText(
                            self, "Password", "Enter Password (All caps):"
                        )
                        if ok and code == "SECRET":
                            self.com1_cleared = True
                            self.message_label.setText("You transferred $30,000 to your account!📈")
                            self.currency += 30



                        else:
                            self.message_label.setText("Wrong password!")


                else:
                    self.message_label.setText("It's a computer but you can't seem to boot it...")



            elif choice == 3:
                if self.painting_checked:
                    self.message_label.setText("You looked closer and found clue #5 on the frame:\n'It can be found in the shed.'")

                else:
                    self.message_label.setText("It's a nice painting. Not much else... 🏜️")
                    self.painting_checked = True


            elif choice == 4:
                self.message_label.setText("You walk into the next room...")
                QTimer.singleShot(2000, self.room_5)
            elif choice == 5:
                self.message_label.setText("You return to the previous room...")
                QTimer.singleShot(2000, self.room_3)


        if self.current_room == "room_5":
            if choice == 1:
                self.message_label.setText("You booted up the computer.")

                if self.com2cleared:
                    self.message_label.setText("You already cleared the computer.")
                else:
                    code, ok = QInputDialog.getText(
                        self, "Password", "Password (All caps):"
                    )
                    if ok and code == "HAMMER":
                        self.message_label.setText("You transferred $10,000 to your account!📈")
                        self.currency += 10

                        self.com2_check = True
                        self.com2cleared = True

                    else:
                        self.message_label.setText("Wrong password!")

            elif choice == 2:
                if self.taken:
                    self.message_label.setText("You checked the calendar and found clue #4:\n'It contains a 'H'.'")
            elif choice == 3:
                self.message_label.setText("You walk into the next room...")
                QTimer.singleShot(2000, self.room_6)
            elif choice == 4:
                self.message_label.setText("You return to the previous room...")
                QTimer.singleShot(2000, self.room_4)



        elif self.current_room == "room_6":
            if choice == 1:
                self.message_label.setText(
                    "There's something hand-written: 'Ww2 end + pie'📜."
                )
            elif choice == 2:
                if self.opened:
                    self.message_label.setText("You already cleared the safe.")
                else:
                    code, ok = QInputDialog.getText(
                        self, "Safe Code", "Enter a code (7 digits):"
                    )
                    if ok and code == "1945314":
                        self.message_label.setText("You found $50,000!💵💵💵")
                        self.currency += 50

                        self.Safe_check = True
                        self.opened = True
                    else:
                        self.message_label.setText("Wrong code!")

            elif choice == 3:
                if self.coat_check:
                    self.message_label.setText("Nothing here.")
                else:
                    self.message_label.setText("You checked the coat and found a disk! 💾")
                    self.disk = True
                    self.coat_check = True


            elif choice == 4:
                if not self.Safe_check:
                    self.end_game(False)
                else:
                    self.end_game(True)
            elif choice == 5:
                self.message_label.setText("You return to the previous room...")
                QTimer.singleShot(2000, self.room_5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = AdventureGame()
    game.show()
    sys.exit(app.exec_())
