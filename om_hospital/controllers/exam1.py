start_loop = True
do_register = True
line_break = "-"*20

menu_list = ['list', 'search', 'register', 'delete', 'quit']

book_list = []

print("My Library \n", line_break)
while (start_loop):
    for menu in menu_list:
        print("# ",menu)
    print(line_break, "\n")

    req = input("Please select a menu : ")
    if req in menu_list:
        if req == menu_list[0]:
            if book_list:
                for book in book_list:
                    print(f"[{book_list.index(book) + 1}] {book}")
            else:
                print("This is no book registered in the list yet. \n")

        elif req == menu_list[1]:
            search_term = input("Enter the search term: ")
            found_books = list(filter(lambda book: search_term.lower() in book.lower(), book_list))

            if found_books:
                for found_book in found_books:
                    print(f"[{book_list.index(found_book) + 1}] {found_book}")
            else:
                print("No matching books found.")

        elif req == menu_list[2]:
            while(do_register):
                add_book = input("Enter the book name to register : ")
                if not add_book:
                    do_register = False
                    start_loop = True
                if add_book and add_book not in book_list:
                    book_list.append(add_book)
                else:
                    print("Already existed")
            do_register = True

        elif req == menu_list[3]:
            req_book = input("Enter the book name or index want to delete : ")
            confirm_msg = input("Please confirm to delete [%s] (y) : "%req_book)
            if confirm_msg == 'y':
                try :
                    index = int(req_book)-1
                    if 0<= index< len(book_list):
                        removed = book_list.pop(index)
                        print("%s has been deleted successfully."%removed)
                    else:
                        print("Invalid Index. No matching books found")
                except ValueError:
                    if req_book in book_list:
                        book_list.remove(req_book)
                        print("%s has been deleted successfully."%req_book)
                    else:
                        print("%s was wrong input."%req_book)
            elif confirm_msg == 'n':
                print("cancelled")

        elif req == menu_list[4]:
            start_loop=False
