files = input("What is your filename?").lower().strip()

if files.endswith(".jpeg"):
    print("image/jpeg")
elif files.endswith(".jpg"):
    print("image/jpg")
elif files.endswith(".gif"):
    print("image/gif")
elif files.endswith(".png"):
    print("image/png")
elif files.endswith(".pdf"):
    print("application/pdf")
elif files.endswith(".txt"):
    print("application/txt")
elif files.endswith(".zip"):
    print("application/zip")
else:
    print("other files")
