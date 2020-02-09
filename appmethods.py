# Custom application methods used by dock.py

# Application(s): sqlizer
# Summary: Take a list, formats using 1 of 2 options and copies to clipboard.
# Option 1 = SSMS [,,,] & Option 2 = SQL Browser [('','','')]
def formatcopy(inputlist: 'str', formatoption: 'int') -> str:
    import pyperclip

    listified = inputlist.split(sep = '\n')
    list_nospace = [i for i in listified if i != '']

    if formatoption == 1:
        listresult1 = ("('" + "','".join(list_nospace) + "')")
        pyperclip.copy(listresult1)
    if formatoption == 2:
        listresult2 = (",".join(list_nospace))
        pyperclip.copy(listresult2)
    return