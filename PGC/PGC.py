##PGC-SYSTEMS###

#Imports
import tkinter as tk
from tkinter import ttk
import sqlite3
import random
from os.path import isfile

#SQL
def createPGCPlayerTable():
    sqlCommand = """
    CREATE TABLE playerTable
    (
    PlayerID INTEGER,
    Name TEXT,
    Phone INTEGER,
    EMail TEXT,
    Handicap INTEGER,
    AgeStatus TEXT,
    SeasonTicket TEXT
    )"""
    PGCDatabaseSQL.execute(sqlCommand)
    PGCDatabase.commit()
def createPGCGameTable():
    sqlCommand = """
    CREATE TABLE gameTable
    (
    GameID INTEGER,
    Date TEXT,
    Time TEXT,
    Type TEXT
    )"""
    PGCDatabaseSQL.execute(sqlCommand)
    PGCDatabase.commit()
def createPGCChargesTable():
    sqlCommand = """
    CREATE TABLE chargesTable
    (
    ChargeCode INTEGER,
    Days TEXT,
    StartTime TEXT,
    EndTime TEXT,
    Adult TEXT,
    Senior TEXT,
    Junior TEXT
    )"""
    PGCDatabaseSQL.execute(sqlCommand)
    PGCDatabase.commit()
def createPGCGamePlayersTable():
    sqlCommand = """
    CREATE TABLE gamePlayersTable
    (
    PlayerID INTEGER,
    GameID INTEGER,
    GameType TEXT,
    ChargeCode TEXT,
    Score INTEGER
    )"""
    PGCDatabaseSQL.execute(sqlCommand)
    PGCDatabase.commit()
PGCDatabaseExists = isfile("PGC.db")
PGCDatabase = sqlite3.connect("PGC.db")
PGCDatabaseSQL = PGCDatabase.cursor()
if PGCDatabaseExists == False:
    createPGCPlayerTable()
    createPGCGameTable()
    createPGCChargesTable()
    createPGCGamePlayersTable()

#Variables

funFacts =  ["Every odd number contains an E in it's spelling.",
            "More man power goes into League of Legends every two-three weeks than were used in the construction of the great pyramids.",
            "Earth is the intergalactic equivalent of an uncontacted tribe.",
            "Mammoths were still alive when the Pyramids of Giza were still being built.",
            "Mars is the only planet that we know of which is exclusively inhabited by robots",
            "A million seconds is 11 days. A billion seconds is 31 years.",
            "A speck of dust is the halfway point in size between the Earth, and a subatomic particle.",
            "It would take 84 years to sleep in every bed in the hotels at disney world if you slept in a new bed each night.",
            "When you get a kidney transplant, they usually leave your original kidneys in your body and put the third one in your pelvis.",
            "If you add up the total amount of hours that World of Warcraft players have played, it totals at 6.8 million years.",
            "1 teaspoon of honey is the lifework of 12 worker bees.",
            "Every 2 minutes, we take more photos than humanity took in the 1800s.",
            "When you blush, the lining of your stomach does as well.",
            "Sometimes when you have an unusually runny nose, it isn't mucus you're feeling, it's cerebral fluids.",
            "Some people only dream in black and white. About 12 percent of the population.",
            "Henry VIII exploded in his coffin while his grave was being dug. The mess was cleared by stray dogs.",
            "Only one in every thousand sea turtles make it to adulthood.",
            "Corpses can get goosebumps.",
            "There's over 3 kilograms of Bacteria in the human body"]
    
#WindowCreate
def mainMenu():
    randomNum = random.randint(0,len(funFacts) - 1)   
    dataLabel = tk.Label(text = ("Fun fact: " + funFacts[randomNum]), bg = "#4a692f", fg = "White")
    dataLabel.place(x = 0, y = 80)
def createWindow():
    global PGCLogo
    screen.geometry("1150x690")
    screen.title("Portsmouth Golf Centre")
    mainFrame = tk.Frame(width = 1150, height = 690, bg = "#4a692f")
    mainFrame.pack()
    menuBar = tk.Menu(screen)
    menuFile = tk.Menu(menuBar, tearoff = 0)
    menuBar.add_cascade(label = "File", menu = menuFile)
    menuFile.add_command(label = "Player table", command = printPlayersTable)
    menuFile.add_command(label = "Game table", command = printGamesTable)
    menuFile.add_command(label = "Charge-Code table", command = printChargesTable)
    menuFile.add_command(label = "Game-Player table", command = printGamePlayersTable)
    menuFile.add_command(label = "Main menu", command = mainMenuRefresh)
    menuFile.add_command(label = "Exit", command = exitProgram)

    menuPrint = tk.Menu(menuBar, tearoff = 0)
    menuBar.add_cascade(label = "Print", menu = menuPrint)
    menuPrint.add_command(label = "Player Report", command = selectPlayerReport)
    menuPrint.add_command(label = "Game Receipt", command = selectGameReceipt)
    menuPrint.add_command(label = "Revenue Report", command = printRevenueReport)
    
    screen.config(menu = menuBar)
    PGCLogo = tk.PhotoImage(file = "PGCLogo.png")
    canvasPGCLogo = tk.Canvas(screen, width = 250, height = 70, bg = "#4a692f", highlightbackground = "#4a692f")
    canvasPGCLogo.place(x = 0, y = 0)
    canvasPGCLogo.create_image(15, 7, image = PGCLogo, anchor = "nw")
    orangeFrame = tk.Frame(bg = "#f39019",
                       width = "1150",
                       height = "10")
    orangeFrame.place(x = 0, y = 70)
    
def clearWindow():
    for widgets in screen.winfo_children():
        widgets.destroy()
    createWindow()

def mainMenuRefresh():
    clearWindow()
    mainMenu()

#PlayerTable
def addPlayerData():
    global counter
    global dataEntry
    global dataLabel
    global newData
    dataLabelText = ["Player name",
                    "Player phone number",
                    "Player E-Mail",
                    "Player handicap",
                    "Player age status",
                    "Player season ticket status"]
    if counter == 0:
        newData = []
        newID = random.randint(1000,9999)
        newData.append(newID)
        dataLabel.config(text = dataLabelText[counter])
    if counter > 0:
        newDataEntry = dataEntry.get()
        newData.append(newDataEntry)
        dataEntry.delete(0,"end")
    if counter != 6:
        dataLabel.config(text = dataLabelText[counter])
        counter += 1
    elif counter == 6:
        sqlCommand = "INSERT INTO playerTable Values(?,?,?,?,?,?,?)"
        PGCDatabaseSQL.execute(sqlCommand,newData)
        PGCDatabase.commit()
        clearWindow()
        printPlayersTable()
def deletePlayerData():
    global dataEntry
    global userData
    global userID
    command = ("""DELETE FROM playerTable
    WHERE PlayerID = """ + userID)
    PGCDatabaseSQL.execute(command)
    PGCDatabase.commit()
    clearWindow()
    printPlayersTable()
def editPlayerData():
    global deleteDataButton
    global dataEntry
    global editDataButton
    global editDataCombobox
    global editID
    global currentValue
    newData = dataEntry.get()
    if currentValue == "PlayerID":
        if len(newData) == 4:
            PGCDatabaseSQL.execute("UPDATE playerTable SET " + currentValue + " = " + "'" + newData + "' WHERE PlayerID = " + editID)
            PGCDatabaseSQL.execute("UPDATE gamePlayersTable SET " + currentValue + " = " + "'" + newData + "' WHERE PlayerID = " + editID)
            PGCDatabase.commit()
            clearWindow()
            printPlayersTable() 
    elif currentValue != "PlayerID":
        PGCDatabaseSQL.execute("UPDATE playerTable SET " + currentValue + " = " + "'" + newData + "' WHERE PlayerID = " + editID)
        PGCDatabase.commit()
        clearWindow()
        printPlayersTable() 
def insertDataPlayerTable():
    global insertDataButton
    global editDataButton
    global counter
    global dataEntry
    global dataLabel
    counter = 0
    editDataButton.config(state = "disabled")
    dataLabel = tk.Label(text = "", bg = "#4a692f", fg = "White")
    dataLabel.place(x = 155, y = 632)
    dataEntry = tk.Entry(bg = "#f39019", width = 25)
    dataEntry.place(x = 1, y = 632)
    insertDataButton.config(text = "Confirm", command = addPlayerData)
    deleteDataButton.config(text = "Cancel", command = cancelOperationPlayersTable)
    addPlayerData()  
def deleteDataPlayerTable():
    global deleteDataButton
    global editDataButton
    global userID
    #Dad-Code
    editDataButton.config(state = "disabled")
    userID = (textBox.get(textBox.curselection()))[0:4]
    PGCDatabaseSQL.execute("SELECT * FROM playerTable WHERE PlayerID = " + userID)
    userData = PGCDatabaseSQL.fetchall()
    dataLabel = tk.Label(text = "Are you want to delete " + userData[0][1] + " from the player table?", bg = "#4a692f", fg = "White")
    dataLabel.place(x = 1, y = 635)
    insertDataButton.config(text = "Confirm", command = deletePlayerData)
    deleteDataButton.config(text = "Cancel", command = cancelOperationPlayersTable)
def editDataPlayerTable():
    global deleteDataButton
    global dataEntry
    global editDataButton
    global editDataCombobox
    global editID
    global currentValue
    currentSelection = (textBox.get(textBox.curselection()))
    currentValue = editDataCombobox.get()
    if currentValue != "Select a Value to edit" and currentSelection[0:2] != "ID" and currentSelection[0:2] != "==":
        editID = currentSelection[0:4]
        dataLabel = tk.Label(text = "Enter the new " + currentValue + " value", bg = "#4a692f", fg = "White")
        dataLabel.place(x = 155, y = 632)
        dataEntry = tk.Entry(bg = "#f39019", width = 25)
        dataEntry.place(x = 1, y = 632)
        editDataButton.config(state = "disabled")
        insertDataButton.config(text = "Confirm", command = editPlayerData)
        deleteDataButton.config(text = "Cancel", command = cancelOperationPlayersTable)
def cancelOperationPlayersTable():
    clearWindow()
    printPlayersTable()
    editDataButton.config(state = "active")
def printPlayersTable():
    global textBox
    global insertDataButton
    global deleteDataButton
    global editDataButton
    global editDataCombobox
    clearWindow()
    textBox = tk.Listbox(width = "164", height = "30", background = "#f39019", font = ("Courier New",10), selectmode = "single")
    textBox.place(x = 0, y = 90)
    insertDataButton = tk.Button(text = "Insert new entry", bg = "#f39019", command = insertDataPlayerTable, height = 1, width = 12)
    insertDataButton.place(x = 1, y = 605)
    deleteDataButton = tk.Button(text = "Remove entry", bg = "#f39019", command = deleteDataPlayerTable, height = 1, width = 12)
    deleteDataButton.place(x = 95, y = 605)
    editDataButton = tk.Button(text = "Edit Entry", bg = "#f39019", command = editDataPlayerTable, height = 1, width = 12)
    editDataButton.place(x = 189, y = 605)
    editDataCombobox = ttk.Combobox(screen, state = "readonly")
    editDataCombobox["values"] = ("PlayerID","Name","Phone","EMail","Handicap","AgeStatus","SeasonTicket")
    editDataCombobox.place(x = 283, y = 605)
    editDataCombobox.set("Select a Value to edit")
    textBox.insert(1, "ID               Name               Phone               E-Mail                         Handicap               Age                Season-Ticket\n")
    textBox.insert(2, "==               ====               =====               ======                         ========               ===                =============\n")
    lineNumber = 2
    PGCDatabaseSQL.execute("SELECT * FROM playerTable")
    playerDataTable = PGCDatabaseSQL.fetchall()
    for x in range(len(playerDataTable)):
        lineNumber += 1
        printPlayerData = playerDataTable[x]
        playerDetails = ("%-16s %-18s +44%-16s %-30s %-22s %-18s %-25s" %(printPlayerData))
        textBox.insert(lineNumber, playerDetails)

#GameTable
def addGameData():
    global counter
    global dataEntry
    global dataLabel
    global newData
    dataLabelText = ["Date",
                     "Time",
                     "Type"]
    if counter == 0:
        newData = []
        newID = random.randint(1000,9999)
        newData.append(newID)
        dataLabel.config(text = dataLabelText[counter])
    if counter > 0:
        newDataEntry = dataEntry.get()
        newData.append(newDataEntry)
        dataEntry.delete(0,"end")
    if counter != 3:
        dataLabel.config(text = dataLabelText[counter])
        counter += 1
    elif counter == 3:
        sqlCommand = "INSERT INTO gameTable Values(?,?,?,?)"
        PGCDatabaseSQL.execute(sqlCommand,newData)
        PGCDatabase.commit()
        clearWindow()
        printGamesTable()
def deleteGameData():
    global dataEntry
    global userData
    global GameID
    command = ("""DELETE FROM gameTable
    WHERE GameID = """ + gameID)
    PGCDatabaseSQL.execute(command)
    PGCDatabase.commit()
    clearWindow()
    printGamesTable()
def editGameData():
    global deleteDataButton
    global dataEntry
    global editDataButton
    global editDataCombobox
    global editID
    global currentValue
    newData = dataEntry.get()
    if currentValue == "GameID":
        if len(newData) == 4:
            PGCDatabaseSQL.execute("UPDATE gameTable SET " + currentValue + " = " + "'" + newData + "' WHERE GameID = " + editID)
            PGCDatabaseSQL.execute("UPDATE gamePlayersTable SET " + currentValue + " = " + "'" + newData + "' WHERE GameID = " + editID)
    elif currentValue != "GameID":
        PGCDatabaseSQL.execute("UPDATE gameTable SET " + currentValue + " = " + "'" + newData + "' WHERE GameID = " + editID)
        PGCDatabaseSQL.execute("UPDATE gameTable SET " + currentValue + " = " + "'" + newData + "' WHERE GameID = " + editID)
        PGCDatabase.commit()
        clearWindow()
        printGamesTable() 
def insertDataGameTable():
    global insertDataButton
    global editDataButton
    global counter
    global dataEntry
    global dataLabel
    counter = 0
    editDataButton.config(state = "disabled")
    dataLabel = tk.Label(text = "", bg = "#4a692f", fg = "White")
    dataLabel.place(x = 155, y = 632)
    dataEntry = tk.Entry(bg = "#f39019", width = 25)
    dataEntry.place(x = 1, y = 632)
    insertDataButton.config(text = "Confirm", command = addGameData)
    deleteDataButton.config(text = "Cancel", command = cancelOperationGamesTable)
    addGameData()
def deleteDataGameTable():
    global deleteDataButton
    global editDataButton
    global gameID
    global dataLabel
    editDataButton.config(state = "disabled")
    gameID = (textBox.get(textBox.curselection()))[0:4]
    PGCDatabaseSQL.execute("SELECT * FROM gameTable WHERE GameID = " + gameID)
    gameData = PGCDatabaseSQL.fetchall()
    dataLabel = tk.Label(text = "Are you want to delete " + gameData[0][1] + " from the game table?", bg = "#4a692f", fg = "White")
    dataLabel.place(x = 1, y = 635)
    insertDataButton.config(text = "Confirm", command = deleteGameData)
    deleteDataButton.config(text = "Cancel", command = cancelOperationGamesTable)
def editDataGameTable():
    global deleteDataButton
    global dataEntry
    global editDataButton
    global editDataCombobox
    global editID
    global currentValue
    currentSelection = (textBox.get(textBox.curselection()))
    currentValue = editDataCombobox.get()
    if currentValue != "Select a Value to edit" and currentSelection[0:2] != "ID" and currentSelection[0:2] != "==":
        editID = currentSelection[0:4]
        dataLabel = tk.Label(text = "Enter the new " + currentValue + " value", bg = "#4a692f", fg = "White")
        dataLabel.place(x = 155, y = 632)
        dataEntry = tk.Entry(bg = "#f39019", width = 25)
        dataEntry.place(x = 1, y = 632)
        editDataButton.config(state = "disabled")
        insertDataButton.config(text = "Confirm", command = editGameData)
        deleteDataButton.config(text = "Cancel", command = cancelOperationGamesTable)
def cancelOperationGamesTable():
    clearWindow()
    printGamesTable()
    editDataButton.config(state = "active")
def printGamesTable():
    global textBox
    global insertDataButton
    global deleteDataButton
    global editDataButton
    global editDataCombobox
    clearWindow()
    textBox = tk.Listbox(width = "164", height = "30", background = "#f39019", font = ("Courier new",10), selectmode = "single")
    textBox.place(x = 0, y = 90)
    insertDataButton = tk.Button(text = "Insert new entry", bg = "#f39019", command = insertDataGameTable, height = 1, width = 12)
    insertDataButton.place(x = 1, y = 605)
    deleteDataButton = tk.Button(text = "Remove entry", bg = "#f39019", command = deleteDataGameTable, height = 1, width = 12)
    deleteDataButton.place(x = 95, y = 605)
    editDataButton = tk.Button(text = "Edit Entry", bg = "#f39019", command = editDataGameTable, height = 1, width = 12)
    editDataButton.place(x = 189, y = 605)
    editDataCombobox = ttk.Combobox(screen, state = "readonly")
    editDataCombobox["values"] = ("GameID","Date","Time","Type")
    editDataCombobox.place(x = 283, y = 605)
    editDataCombobox.set("Select a Value to edit")
    textBox.insert(1,"ID                                         Date                                      Time                                     Type")
    textBox.insert(2,"==                                         ====                                      ====                                     ====")
    lineNumber = 2
    PGCDatabaseSQL.execute("SELECT * FROM gameTable")
    gameDataTable = PGCDatabaseSQL.fetchall()
    for x in range(len(gameDataTable)):
        lineNumber += 1
        printGameData = gameDataTable[x]
        gameDetails = ("%-42s %-41s %-40s %-42s" %(printGameData))
        textBox.insert(lineNumber, gameDetails)

#ChargesTable
def addChargesData():
    global counter
    global dataEntry
    global dataLabel
    global newData
    dataLabelText = ["Days",
                     "Start-Time",
                     "End-Time",
                     "Adult",
                     "Senior",
                     "Junior"]
    if counter == 0:
        newData = []
        PGCDatabaseSQL.execute("SELECT * FROM chargesTable")
        chargesData = PGCDatabaseSQL.fetchall()
        newCodeNum = len(chargesData) + 1
        newData.append(newCodeNum)
        dataLabel.config(text = dataLabelText[counter])
    if counter > 0:
        newDataEntry = dataEntry.get()
        newData.append(newDataEntry)
        dataEntry.delete(0,"end")
    if counter != 6:
        dataLabel.config(text = dataLabelText[counter])
        counter += 1
    elif counter == 6:
        sqlCommand = "INSERT INTO chargesTable Values(?,?,?,?,?,?,?)"
        PGCDatabaseSQL.execute(sqlCommand,newData)
        PGCDatabase.commit()
        clearWindow()
        printChargesTable()
def deleteChargesData():
    global ChargeID
    command = ("""DELETE FROM chargesTable
    WHERE ChargeCode = """ + ChargeID)
    PGCDatabaseSQL.execute(command)
    PGCDatabase.commit()
    clearWindow()
    printChargesTable()
def editChargesData():
    global deleteDataButton
    global dataEntry
    global editDataButton
    global editDataCombobox
    global editID
    global currentValue
    newData = dataEntry.get()
    PGCDatabaseSQL.execute("UPDATE chargesTable SET " + currentValue + " = " + "'" + newData + "' WHERE ChargeCode = " + editID)
    PGCDatabaseSQL.execute("UPDATE chargesTable SET " + currentValue + " = " + "'" + newData + "' WHERE ChargeCode = " + editID)
    PGCDatabase.commit()
    clearWindow()
    printChargesTable() 
def insertDataChargesTable():
    global insertDataButton
    global editDataButton
    global counter
    global dataEntry
    global dataLabel
    counter = 0
    editDataButton.config(state = "disabled")
    dataLabel = tk.Label(text = "", bg = "#4a692f", fg = "White")
    dataLabel.place(x = 155, y = 632)
    dataEntry = tk.Entry(bg = "#f39019", width = 25)
    dataEntry.place(x = 1, y = 632)
    insertDataButton.config(text = "Confirm", command = addChargesData)
    deleteDataButton.config(text = "Cancel", command = cancelOperationChargesTable)
    addChargesData()
def deleteDataChargesTable():
    global deleteDataButton
    global editDataButton
    global ChargeID
    PGCDatabaseSQL.execute("SELECT * FROM chargesTable")
    chargesData = PGCDatabaseSQL.fetchall()
    codeLength = len(str(chargesData[len(chargesData) - 1][0]))
    editDataButton.config(state = "disabled")
    ChargeID = (textBox.get(textBox.curselection()))[0:codeLength]
    PGCDatabaseSQL.execute("SELECT * FROM chargesTable WHERE ChargeCode = " + ChargeID)
    chargeData = PGCDatabaseSQL.fetchall()
    dataLabel = tk.Label(text = "Are you want to delete " + " from the charges table?", bg = "#4a692f", fg = "White")
    dataLabel.place(x = 1, y = 635)
    insertDataButton.config(text = "Confirm", command = deleteChargesData)
    deleteDataButton.config(text = "Cancel", command = cancelOperationChargesTable)
def editDataChargeTable():
    global deleteDataButton
    global dataEntry
    global editDataButton
    global editDataCombobox
    global editID
    global currentValue
    currentSelection = (textBox.get(textBox.curselection()))
    currentValue = editDataCombobox.get()
    if currentValue != "Select a Value to edit" and currentSelection[0:2] != "Ch" and currentSelection[0:2] != "==":
        PGCDatabaseSQL.execute("SELECT * FROM chargesTable")
        chargesData = PGCDatabaseSQL.fetchall()
        codeLength = len(str(chargesData[len(chargesData) - 1][0]))
        editID = currentSelection[0:codeLength]
        dataLabel = tk.Label(text = "Enter the new " + currentValue + " value", bg = "#4a692f", fg = "White")
        dataLabel.place(x = 155, y = 632)
        dataEntry = tk.Entry(bg = "#f39019", width = 25)
        dataEntry.place(x = 1, y = 632)
        editDataButton.config(state = "disabled")
        insertDataButton.config(text = "Confirm", command = editChargesData)
        deleteDataButton.config(text = "Cancel", command = cancelOperationChargesTable)
def cancelOperationChargesTable():
    clearWindow()
    printChargesTable()
    editDataButton.config(state = "active")
def printChargesTable():
    global textBox
    global insertDataButton
    global deleteDataButton
    global editDataButton
    global editDataCombobox
    clearWindow()
    textBox = tk.Listbox(width = "164", height = "30", background = "#f39019", font = ("Courier new",10), selectmode = "single")
    textBox.place(x = 0, y = 90)
    insertDataButton = tk.Button(text = "Insert new entry", bg = "#f39019", command = insertDataChargesTable, height = 1, width = 12)
    insertDataButton.place(x = 1, y = 605)
    deleteDataButton = tk.Button(text = "Remove entry", bg = "#f39019", command = deleteDataChargesTable, height = 1, width = 12)
    deleteDataButton.place(x = 95, y = 605)
    editDataButton = tk.Button(text = "Edit Entry", bg = "#f39019", command = editDataChargeTable, height = 1, width = 12)
    editDataButton.place(x = 189, y = 605)
    editDataCombobox = ttk.Combobox(screen, state = "readonly")
    editDataCombobox["values"] = ("ChargeCode","Days","StartTime","EndTime","Adult","Senior","Junior")
    editDataCombobox.place(x = 283, y = 605)
    editDataCombobox.set("Select a Value to edit")
    textBox.insert(1,"Charge-Code               Days               Start-Time               End-Time               Adult               Senior               Junior")
    textBox.insert(2,"===========               ====               ==========               ========               =====               ======               ======")
    lineNumber = 2
    PGCDatabaseSQL.execute("SELECT * FROM chargesTable")
    chargeCodeDataTable = PGCDatabaseSQL.fetchall()
    for x in range(len(chargeCodeDataTable)):
        lineNumber += 1
        printChargeCodeData = chargeCodeDataTable[x]
        chargeCodeDetails = ("%-25s %-18s %-24s %-22s £%-18s £%-19s £%-25s" %(printChargeCodeData))
        textBox.insert(lineNumber, chargeCodeDetails)

#GamePlayersTable
def insertDataGamePlayerTable():
    global textBox
    global newData
    global lineNumber
    global confirmButton
    global newEntry
    newScore = newEntry.get()
    newData.append(newScore)
    PGCDatabaseSQL.execute("INSERT INTO gamePlayersTable Values (?,?,?,?,?)",newData)
    PGCDatabase.commit()
    clearWindow()
    printGamePlayersTable()
def insertScoreDataGamePlayersTable():
    global textBox
    global newData
    global lineNumber
    global confirmButton
    global newEntry
    currentSelection = (textBox.get(textBox.curselection()))
    if str(currentSelection)[0:2] != "==" and str(currentSelection)[0:11] != "Charge-Code":
        confirmButton.config(command = insertDataGamePlayerTable)
        newEntry = tk.Entry(bg = "#f39019", width = 25)
        newEntry.place(x = 370,y = 622)
        dataLabel = tk.Label(text = "Enter the score of the game", bg = "#4a692f", fg = "White")
        dataLabel.place(x = 450, y = 622)
        newData.append(currentSelection)
        textBox.delete(0, lineNumber)
        textBox.insert(1,"Current-Data")
        textBox.insert(2,"============")
        lineNumber = 2
        for x in range(len(newData)):
            textBox.insert(lineNumber, newData[x])
            lineNumber += 1
def instertChargeDataGamePlayersTable():
    global textBox
    global newData
    global lineNumber
    global confirmButton
    currentSelection = (textBox.get(textBox.curselection()))
    if str(currentSelection)[0:2] != "==" and str(currentSelection)[0:7] != "Game-ID":
        PGCDatabaseSQL.execute("SELECT * FROM gameTable WHERE GameID = '" + str(currentSelection) + "'")
        confirmButton.config(command = insertScoreDataGamePlayersTable)
        newType = PGCDatabaseSQL.fetchall()
        newType = newType[0][3]
        newID = currentSelection
        newData.append(newID)
        newData.append(newType)
        textBox.delete(0, lineNumber)
        PGCDatabaseSQL.execute("SELECT * FROM chargesTable")
        gamePlayersDataTable = PGCDatabaseSQL.fetchall()
        textBox.insert(1,"Charge-Code")
        textBox.insert(2,"===========")
        lineNumber = 2
        for x in range(len(gamePlayersDataTable)):
            playerDetails = ()
            textBox.insert(lineNumber, gamePlayersDataTable[x][0])
            lineNumber += 1
def insertGameDataGamePlayersTable():
    global textBox
    global newData
    global lineNumber
    global confirmButton
    currentSelection = (textBox.get(textBox.curselection()))
    if str(currentSelection)[0:2] != "==" and str(currentSelection)[0:11] != "Player-Name":
        PGCDatabaseSQL.execute("SELECT * FROM playerTable WHERE Name = '" + str(currentSelection) + "'")
        confirmButton.config(command = instertChargeDataGamePlayersTable)
        newID = PGCDatabaseSQL.fetchall()
        newID = newID[0][0]
        newData.append(newID)
        textBox.delete(0, lineNumber)
        PGCDatabaseSQL.execute("SELECT * FROM gameTable")
        gamePlayersDataTable = PGCDatabaseSQL.fetchall()
        textBox.insert(1,"Game-ID")
        textBox.insert(2,"=======")
        lineNumber = 2
        for x in range(len(gamePlayersDataTable)):
            playerDetails = ()
            textBox.insert(lineNumber, gamePlayersDataTable[x][0])
            lineNumber += 1
def deleteGamePlayersData():
    global playerID
    global gameID
    command = ("""DELETE FROM gamePlayersTable WHERE playerID = """ + playerID + """ AND gameID = """ + gameID)
    PGCDatabaseSQL.execute(command)
    PGCDatabase.commit()
    clearWindow()
    printGamePlayersTable()
def editGamePlayersData():
    global textBox
    global currentSelection
    global currentPlayerID
    global currentGameID
    global newEntry
    global currentValue
    if currentValue != "Score":
        currentSelection = (textBox.get(textBox.curselection()))
        newData = str(currentSelection)
    else:
        newData = newEntry.get()
    PGCDatabaseSQL.execute("UPDATE gamePlayersTable SET " + currentValue + " = " + "'" + newData + "' WHERE playerID = " + currentPlayerID + " AND gameID = " + currentGameID)
    PGCDatabase.commit()
    clearWindow()
    printGamePlayersTable()
def insertPlayerDataGamePlayersTable():
    global lineNumber
    global textBox
    global newData
    global confirmButton
    clearWindow()
    newData = []
    textBox = tk.Listbox(width = 90, height = 31, bg = "#f39019", font = ("Courier new",10))
    textBox.place(x = 180, y = 90)
    confirmButton = tk.Button(text = "Confirm", bg = "#f39019", height = 1, width = 12, command = insertGameDataGamePlayersTable)
    confirmButton.place(x = 181, y = 622)
    cancelButton = tk.Button(text = "Cancel", bg = "#f39019", height = 1, width = 12, command = cancelOperationGamePlayersTable)
    cancelButton.place(x = 276, y = 622)
    PGCDatabaseSQL.execute("SELECT * FROM playerTable")
    gamePlayersDataTable = PGCDatabaseSQL.fetchall()
    textBox.insert(1,"Player-Name")
    textBox.insert(2,"===========")
    lineNumber = 2
    for x in range(len(gamePlayersDataTable)):
        playerDetails = ()
        textBox.insert(lineNumber, gamePlayersDataTable[x][1])
        lineNumber += 1
def deleteDataGamePlayersTable():
    global deleteDataButton
    global editDataButton
    global playerID
    global gameID
    PGCDatabaseSQL.execute("SELECT * FROM gamePlayersTable")
    gamePlayersData = PGCDatabaseSQL.fetchall()
    editDataButton.config(state = "disabled")
    playerID = (textBox.get(textBox.curselection()))[0:4]
    gameID = (textBox.get(textBox.curselection()))[33:38]
    dataLabel = tk.Label(text = "Are you want to delete " + " from the game players table?", bg = "#4a692f", fg = "White")
    dataLabel.place(x = 1, y = 635)
    insertDataButton.config(text = "Confirm", command = deleteGamePlayersData)
    deleteDataButton.config(text = "Cancel", command = cancelOperationChargesTable)
def editDataGamePlayersTable():
    global textBox
    global currentSelection
    global currentPlayerID
    global currentGameID
    global newEntry
    global currentValue 
    currentValue = editDataCombobox.get()
    currentSelection = (textBox.get(textBox.curselection()))
    currentPlayerID = currentSelection[0:4]
    currentGameID = currentSelection[33:38]
    clearWindow()
    textBox = tk.Listbox(width = 90, height = 31, bg = "#f39019", font = ("Courier new",10))
    textBox.place(x = 180, y = 90)
    confirmButton = tk.Button(text = "Confirm", bg = "#f39019", height = 1, width = 12, command = editGamePlayersData)
    confirmButton.place(x = 181, y = 622)
    cancelButton = tk.Button(text = "Cancel", bg = "#f39019", height = 1, width = 12, command = cancelOperationGamePlayersTable)
    cancelButton.place(x = 276, y = 622)
    if currentValue != "Score":
        if currentValue == "PlayerID":
            PGCDatabaseSQL.execute("SELECT * FROM playerTable")
        elif currentValue == "GameID":
            PGCDatabaseSQL.execute("SELECT GameID FROM gameTable")
        elif currentValue == "ChargeCode":
            PGCDatabaseSQL.execute("SELECT * FROM chargesTable")
        gamePlayersDataTable = PGCDatabaseSQL.fetchall()
        textBox.insert(1, currentValue)
        lineGap = ("")
        for x in range(len(currentValue)):
            lineGap += "="
        textBox.insert(2,lineGap)
        lineNumber = 2
        for x in range(len(gamePlayersDataTable)):
            textBox.insert(lineNumber, gamePlayersDataTable[x][0])
            lineNumber += 1
    if currentValue == "Score":
        PGCDatabaseSQL.execute("SELECT * FROM gamePlayersTable")
        gamePlayersDataTable = PGCDatabaseSQL.fetchall()
        textBox.insert(1, "Current-Data")
        textBox.insert(2, "============")
        lineNumber = 2
        for x in range(len(gamePlayersDataTable[0]) - 1):
            textBox.insert(lineNumber, gamePlayersDataTable[0][x])
            lineNumber += 1
        newEntry = tk.Entry(bg = "#f39019", width = 25)
        newEntry.place(x = 370,y = 622)
        dataLabel = tk.Label(text = "Enter the new score of the game", bg = "#4a692f", fg = "White")
        dataLabel.place(x = 450, y = 622)
def cancelOperationGamePlayersTable():
    clearWindow()
    printGamePlayersTable()
    editDataButton.config(state = "active")
def printGamePlayersTable():
    global textBox
    global insertDataButton
    global deleteDataButton
    global editDataButton
    global editDataCombobox
    clearWindow()
    textBox = tk.Listbox(width = "164", height = "30", background = "#f39019", font = ("Courier new",10), selectmode = "single")
    textBox.place(x = 0, y = 90)
    insertDataButton = tk.Button(text = "Insert new entry", bg = "#f39019", command = insertPlayerDataGamePlayersTable, height = 1, width = 12)
    insertDataButton.place(x = 1, y = 605)
    deleteDataButton = tk.Button(text = "Remove entry", bg = "#f39019", command = deleteDataGamePlayersTable, height = 1, width = 12)
    deleteDataButton.place(x = 95, y = 605)
    editDataButton = tk.Button(text = "Edit Entry", bg = "#f39019", command = editDataGamePlayersTable, height = 1, width = 12)
    editDataButton.place(x = 189, y = 605)
    editDataCombobox = ttk.Combobox(screen, state = "readonly")
    editDataCombobox["values"] = ("PlayerID","GameID","ChargeCode","Score")
    editDataCombobox.place(x = 283, y = 605)
    editDataCombobox.set("Select a Value to edit")
    textBox.insert(1,"Player-ID                         Game-ID                         Game-Type                         Charge-Code                        Score")
    textBox.insert(2,"=========                         =======                         =========                         ===========                        =====")
    lineNumber = 2
    PGCDatabaseSQL.execute("SELECT * FROM gamePlayersTable")
    gamePlayersDataTable = PGCDatabaseSQL.fetchall()
    for x in range(len(gamePlayersDataTable)):
        lineNumber += 1
        printGamePlayersCodeData = gamePlayersDataTable[x]
        gamePlayersDetails = ("%-33s %-31s %-33s %-34s %-18s" %(printGamePlayersCodeData))
        textBox.insert(lineNumber, gamePlayersDetails)

#PlayerReport

def printPlayerReport():
    global textBox
    currentSelection = (textBox.get(textBox.curselection()))
    if str(currentSelection)[0:2] != "==" and str(currentSelection)[0:11] != "Player-Name":
        currentID = currentSelection[0:4]
        PGCDatabaseSQL.execute("SELECT * FROM playerTable WHERE PlayerID = " + currentID)
        playerData = PGCDatabaseSQL.fetchall()
        PGCDatabaseSQL.execute("SELECT * FROM gamePlayersTable WHERE PlayerID = " + currentID)
        gamePlayerData = PGCDatabaseSQL.fetchall()
        totalSpent = 0
        for x in range(len(gamePlayerData)):
            PGCDatabaseSQL.execute("SELECT " + playerData[0][5] + " FROM chargesTable WHERE ChargeCode = " + gamePlayerData[x][3])
            chargeCodeData = PGCDatabaseSQL.fetchall()
            if playerData[0][6] == "NST":
                totalSpent += int(chargeCodeData[0][0])
            if playerData[0][6] == "FT":
                totalSpent += int(chargeCodeData[0][0]) / 2
        if playerData[0][6] == "MT":
            if playerData[0][5] == "Adult":
                totalSpent += 659
            if playerData[0][5] == "Junior":
                totalSpent += 99
            if playerData[0][5] == "Senior":
                totalSpent += 469
        if playerData[0][6] == "FT":
            if playerData[0][5] == "Adult":
                totalSpent += 369
            if playerData[0][5] == "Junior":
                totalSpent += 239
            if playerData[0][5] == "Senior":
                totalSpent += 39
                
        playerList = []
        playerGameList = []
        for x in range(len(gamePlayerData)):
            PGCDatabaseSQL.execute("SELECT PlayerID FROM gamePlayersTable WHERE gameID = " + str(gamePlayerData[x][1]))
            temp = PGCDatabaseSQL.fetchall()
            for y in range(len(temp)):
                playerNotInList = True
                for z in range(len(playerList)):
                    if temp[y] == playerList[z]:
                        playerNotInList = False
                if playerNotInList == True and int(temp[y][0]) != int(currentID):
                    playerList.append(temp[y])
                playerGameList.append(temp[y])
        playerListFrequency = []
        for x in range(len(playerList)):
            playerListFrequency.append(0)
            for y in range(len(playerGameList)):
                if playerList[x] == playerGameList[y]:
                    playerListFrequency[x] += 1
        largestPlayerNum = [0]
        for x in range(len(playerListFrequency)):
            if playerListFrequency[x] > largestPlayerNum[0]:
                largestPlayerNum[0] = playerListFrequency[x]
                playerIncrament = x
                
        PGCDatabaseSQL.execute("SELECT Name FROM playerTable WHERE PlayerID = " + str(playerList[playerIncrament][0]))
        favouritePlayer = PGCDatabaseSQL.fetchall()
        favouritePlayer = favouritePlayer[0][0]
        totalHoles = 0
        totalScore = 0
        scoreList = []
        for x in range(len(gamePlayerData)):
            totalScore += gamePlayerData[x][4]
            totalHoles += int(gamePlayerData[x][2])
            scoreList.append(gamePlayerData[x][4])
        averageScore = totalScore / len(gamePlayerData)
        if averageScore > 69:
            parCount = " (" + str(int(averageScore - 69)) + " over par)"
        if averageScore == 69:
            parCount = " (par)"
        if averageScore < 69:
            parCount = " (" + str(int(69 - averageScore)) + " under par)"
        
        clearWindow()
        textBox = tk.Listbox(width = 90, height = 31, bg = "#f39019", font = ("Courier new",10))
        textBox.place(x = 180, y = 90)
        textBox.insert(1,"Portsmouth Golf Centre Player report")
        textBox.insert(2,"====================================")
        textBox.insert(3,"Player Name: " + playerData[0][1])
        textBox.insert(4,"Total games played: " + str(len(gamePlayerData)))
        textBox.insert(5,"Total holes played: " + str(totalHoles))
        textBox.insert(6,"Average score: " + str(int(averageScore)) + str(parCount))
        textBox.insert(7,"Total spent: £" + str(totalSpent))
        textBox.insert(8,"Favourite partner: " + str(favouritePlayer))
        newReportButton = tk.Button(text = "New Report", bg = "#f39019", height = 1, width = 12, command = selectPlayerReport)
        newReportButton.place(x = 181, y = 622)

def selectPlayerReport():
    global textBox
    printPlayersTable()
    editDataCombobox.destroy()
    editDataButton.destroy()
    deleteDataButton.destroy()
    insertDataButton.config(text = "Confirm", command = printPlayerReport)
    dataLabel = tk.Label(text = "Select the Player you wish to print a report on", bg = "#4a692f", fg = "White")
    dataLabel.place(x = 100, y = 607)

#GameReceipt
def printGamesReceipt():
    global textBox
    currentSelection = (textBox.get(textBox.curselection()))
    if str(currentSelection)[0:2] != "==" and str(currentSelection)[0:2] != "ID":
        currentID = currentSelection[0:4]
        PGCDatabaseSQL.execute("SELECT * FROM gamePlayersTable WHERE GameID = " + currentID)
        gamePlayerData = PGCDatabaseSQL.fetchall()
        totalMoneySpent = 0
        moneyList = []
        playerNameList = []
        for x in range(len(gamePlayerData)):
            PGCDatabaseSQL.execute("SELECT Name FROM PlayerTable WHERE PlayerID = " + str(gamePlayerData[x][0]))
            currentPlayerName = PGCDatabaseSQL.fetchall()
            playerNameList.append(currentPlayerName[0][0])
            PGCDatabaseSQL.execute("SELECT AgeStatus FROM PlayerTable WHERE PlayerID = " + str(gamePlayerData[x][0]))
            ageStatus = PGCDatabaseSQL.fetchall()
            PGCDatabaseSQL.execute("SELECT " + ageStatus[0][0] + " FROM chargesTable WHERE ChargeCode = " + gamePlayerData[x][3])
            price = PGCDatabaseSQL.fetchall()
            PGCDatabaseSQL.execute("SELECT seasonTicket FROM PlayerTable where PlayerID = " + str(gamePlayerData[x][0]))
            seasonTicketStatus = PGCDatabaseSQL.fetchall()

            if seasonTicketStatus[0][0] == "NST":
                totalMoneySpent += int(price[0][0])
                moneyList.append(price[0][0])
            if seasonTicketStatus[0][0] == "FT":
                totalMoneySpent += ((int(price[0][0])) / 2)
                moneyList.append((int(price[0][0])) / 2)
            if seasonTicketStatus[0][0] == "MT":
                newVal = 0
                moneyList.append(newVal)
            
        clearWindow()
        textBox = tk.Listbox(width = 90, height = 31, bg = "#f39019", font = ("Courier new",10))
        textBox.place(x = 180, y = 90)
        textBox.insert(1,"Portsmouth Golf Centre Game Receipt")
        textBox.insert(2,"===================================")
        lineNumber = 2
        for x in range(len(playerNameList)):
            lineNumber += 1
            textBox.insert(lineNumber, playerNameList[x] + "-")
            lineNumber += 1
            textBox.insert(lineNumber, "Green fee: £" + str(moneyList[x]))
            lineNumber += 1
            textBox.insert(lineNumber, "Score: " + str(gamePlayerData[x][4]))
            lineNumber += 1
            textBox.insert(lineNumber,"")
        PGCDatabaseSQL.execute("SELECT * FROM GameTable WHERE GameID = " + currentID)
        gameData = PGCDatabaseSQL.fetchall()
        textBox.insert(lineNumber,"===================================")
        lineNumber += 1
        textBox.insert(lineNumber, "Game type: " + gameData[0][3])
        lineNumber += 1
        textBox.insert(lineNumber, "Game time: " + gameData[0][2])
        lineNumber += 1
        textBox.insert(lineNumber, "Game date: " + gameData[0][1])
        lineNumber += 1
        textBox.insert(lineNumber, "Total price: £" + str(totalMoneySpent))
        newReceiptButton = tk.Button(text = "New Receipt", bg = "#f39019", height = 1, width = 12, command = selectGameReceipt)
        newReceiptButton.place(x = 181, y = 622)
        
    
def selectGameReceipt():
    global textBox
    printGamesTable()
    editDataCombobox.destroy()
    editDataButton.destroy()
    deleteDataButton.destroy()
    insertDataButton.config(text = "Confirm", command = printGamesReceipt)
    dataLabel = tk.Label(text = "Select the Game you wish to print a receipt on", bg = "#4a692f", fg = "White")
    dataLabel.place(x = 100, y = 607)

#RevenueReport
def printRevenueReport():
    PGCDatabaseSQL.execute("SELECT * FROM gamePlayersTable")
    gamePlayerData = PGCDatabaseSQL.fetchall()
    PGCDatabaseSQL.execute("SELECT * FROM PlayerTable")
    playerData = PGCDatabaseSQL.fetchall()
    PGCDatabaseSQL.execute("SELECT * FROM GameTable")
    gameData = PGCDatabaseSQL.fetchall()
    totalRevenue = 0
    for x in range(len(gamePlayerData) - 1):
        PGCDatabaseSQL.execute("SELECT AgeStatus FROM PlayerTable WHERE PlayerID = " + str(gamePlayerData[x][0]))
        ageStatus = PGCDatabaseSQL.fetchall()
        PGCDatabaseSQL.execute("SELECT SeasonTicket FROM PlayerTable WHERE PlayerID = " + str(gamePlayerData[x][0]))
        seasonTicketStatus = PGCDatabaseSQL.fetchall()
        PGCDatabaseSQL.execute("SELECT " + ageStatus[0][0] + " FROM chargesTable WHERE ChargeCode = " + str(gamePlayerData[x][3]))
        currentMoney = PGCDatabaseSQL.fetchall()
        if seasonTicketStatus[0][0] == "NST":
            totalRevenue += int(currentMoney[0][0])
        if seasonTicketStatus[0][0] == "FT":
            totalRevenue += (int(currentMoney[0][0]) / 2)
    totalHoles = 0

    seasonTicketCount = 0
    maxiTicketCount = 0
    flexiTicketCount = 0
    for x in range(len(playerData)):
        if playerData[x][6] == "MT":
            maxiTicketCount += 1
            if playerData[x][5] == "Adult":
                totalRevenue += 659
            if playerData[x][5] == "Junior":
                totalRevenue += 99
            if playerData[x][5] == "Senior":
                totalRevenue += 469
        if playerData[x][6] == "FT":
            flexiTicketCount += 1
            if playerData[x][5] == "Adult":
                totalRevenue += 369
            if playerData[x][5] == "Junior":
                totalRevenue += 239
            if playerData[x][5] == "Senior":
                totalRevenue += 39
    seasonTicketCount = (maxiTicketCount + flexiTicketCount)
    
    for x in range(len(gameData)):
        totalHoles += int(gameData[x][3])
    clearWindow()
    textBox = tk.Listbox(width = 90, height = 31, bg = "#f39019", font = ("Courier new",10))
    textBox.place(x = 180, y = 90)
    textBox.insert(1,"Portsmouth Golf Centre Revenue Report")
    textBox.insert(2,"=====================================")
    textBox.insert(3,"Total tickets sold: " + str(len(gamePlayerData)))
    textBox.insert(4,"Total customers: " + str(len(playerData)))
    textBox.insert(5,"Total games played: " + str(len(gameData)))
    textBox.insert(6,"Total holes played: " + str(totalHoles))
    textBox.insert(7,"Maxi tickets sold: " + str(maxiTicketCount))
    textBox.insert(8,"Flexi tickets sold: " + str(flexiTicketCount))
    textBox.insert(9,"Total season tickets sold: " + str(seasonTicketCount))
    textBox.insert(10,"------------------------------------")
    textBox.insert(11,"Total money made: £" + str(totalRevenue))
    
#Program
def exitProgram():
    PGCDatabase.close()
    exit()

screen = tk.Tk()
screen.iconbitmap("golfBall.ico")
screen.resizable(0, 0)

createWindow()
mainMenu()

screen.mainloop()
currentSelection = input("")
if currentSelection == "RESET":
    screen = tk.Tk()
    screen.iconbitmap("golfBall.ico")
    screen.resizable(0, 0)
    createWindow()
    mainMenu
