import os
import streamlit as st
import subprocess
import re
import sys

file_path, file_dir = '', ''


def convert_to(folder, source, timeout=None):
    try:
        args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]
        print('after args')
        process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
        print('process data --> ' + process.stdout.decode('latin-1', errors='replace'))
        filename = re.search('-> (.*?) using filter', process.stdout.decode('latin-1', errors='replace'))

        if filename is None:
            print('ERROR!')
            raise Exception
        else:
            print('else, ' + filename.group(1))
            return filename.group(1)
    except Exception as e:
        print(e)


def libreoffice_exec():
    print('system type --> ' + sys.platform)
    # TODO: Provide support for more platforms
    if sys.platform == 'win32':
        return 'C:\Program Files\LibreOffice\program\swriter.exe'
    return 'libreoffice'


def main():
    try:
        file = st.file_uploader(label='Upload doc files here', type='.docx')
        if file:
            cpfile = open(file.name, 'ab')
            cpfile.write(file.read())
            cpfile.close()
            convert_to(os.getcwd(), file.name)
            rffile = open(file.name[:file.name.rfind('.')+1]+'pdf', 'rb')
            pdf_data = rffile.read()
            file_download = st.download_button(label='pdf file', data=pdf_data, file_name=file.name[:file.name.rfind('.')+1]+'pdf')
    except Exception as e:

        print(e)

main()
