#! python3
# pyw 扩展名意味着 Python运行该程序时，不会显示终端窗
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: python3 mcb.pyw save <keyword> - Saves clipboard to keyword.
# python3 mcb.pyw <keyword> - Loads keyword to clipboard.
# python3 mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print('save')
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('list')
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        print('deleted')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
