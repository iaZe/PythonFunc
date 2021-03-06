import tempfile
import win32api
import win32print

win32print.SetDefaultPrinter = ('nome imp')

arquivofile = tempfile.mktemp (".txt")

arquivo = open(arquivofile, "w")
arquivo.write('OpenCode Technology')
arquivo.close()
try:
    win32api.ShellExecute (0, "print", arquivofile, None, ".", 0)
    win32print.StartPagePrinter(printer)
    win32print.WritePrinter(printer, arquivofile)
    win32print.EndPagePrinter(printer)
finally:
    win32print.EndDocPrinter(printer)
