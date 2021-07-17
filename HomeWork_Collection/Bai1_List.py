from tkinter import *

list = []

window = Tk()
window.title("Bai1 List")


listLabel = Label(window, text="List của bạn:")
listLabel.grid(row=0, column=0)
resultLabel = Label(window, fg="green")
resultLabel.grid(row=0, column=1)


def CreateClicked():
    createLabel.configure(text="List đã được tạo", fg="green")


createButton = Button(window, text="Tạo list", command=CreateClicked)
createButton.grid(row=1, column=0, sticky="WE")
createLabel = Label(window, text="Chưa có list nào được tạo")
createLabel.grid(row=1, column=1)


def AddElemClick():
    list.append(elemText.get())
    elemText.delete(0, 'end')
    resultLabel.configure(text=list)


addElemButton = Button(window, text="Thêm phần tử", command=AddElemClick)
addElemButton.grid(row=2, column=0, sticky="WE")
elemText = Entry(window)
elemText.grid(row=2, column=1)


def countK():
    count = 0
    for elem in list:
        if elem == kText.get():
            count += 1
    kLabel.configure(text=str(count) + " lần")


countKButton = Button(
    window, text="Đếm số lần k xuất hiện", command=countK)
countKButton.grid(row=3, column=0, sticky="WE")
kText = Entry(window)
kText.grid(row=3, column=1)
kLabel = Label(window)
kLabel.grid(row=3, column=2)


def sumList():
    sum = 0
    for elem in list:
        try:
            number = int(elem)
            sum += number
        except:
            pass
    sumLabel.configure(text=sum)


sumButton = Button(window, text="Tổng các số nguyên", command=sumList)
sumButton.grid(row=4, column=0, sticky="WE")
sumLabel = Label(window)
sumLabel.grid(row=4, column=1)


def arrangeListAsc():
    list.sort()
    resultLabel.configure(text=list)


arrListAscButton = Button(
    window, text="Sắp xếp tăng dần", command=arrangeListAsc)
arrListAscButton.grid(row=5, column=0, sticky="WE")


def arrangeListDesc():
    list.sort(reverse=True)
    resultLabel.configure(text=list)


arrLisDescButton = Button(
    window, text="Sắp xếp giảm dần", command=arrangeListDesc)
arrLisDescButton.grid(row=5, column=1, sticky="WE")


def deleteList():
    list.clear()
    resultLabel.configure(text=list)


deleteButton = Button(
    window, text="Xóa list", command=deleteList)
deleteButton.grid(row=6, column=0, sticky="WE")

window.mainloop()
