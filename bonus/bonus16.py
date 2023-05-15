import PySimpleGUI as sg

label_select_compress = sg.Text("Select files to compress:")
input_files_to_compress = sg.Input()
choose_files_compress_button = sg.FilesBrowse('Choose')

label_destination_compress = sg.Text("Select destination folder:")
input_destination_compress = sg.Input()
choose_destination_button = sg.FolderBrowse('Choose')

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[
    [label_select_compress, input_files_to_compress, choose_files_compress_button],
    [label_destination_compress, input_destination_compress, choose_destination_button],
    [compress_button]
])
window.read()
window.close()
