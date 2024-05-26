import qrcode as qr

link = input("Enter the link: ")
renameFile = input("Rename file: ")

img = qr.make(link)
img.save(renameFile + ".png")