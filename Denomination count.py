def countCurrency(amount):
    notes=[2000, 500, 300, 100, 50, 20, 10, 5, 1]
    notesCount={}
    for note in notes:
        if amount>=note:
            notesCount[note]=amount//note
            amount=amount%note
    print("Currency Count ->")
    for key,val in notesCount.items():
        print(f"{key}:{val}")
amount=868
countCurrency(amount)