# MundaneTasks

A bunch of scripts to do mundane but essential tasks

1. [Adding watermark text to multiple PDF files](#adding-watermark-text-to-multiple-pdf-files)

## Details

### Adding watermark text to multiple PDF files

The shell script (addWatermarkToPDFsInFolder.sh) iterates over the directory and executes the python file with the watermark string on all PDF files present in the directory.
The python file (pdf_watermark.py) uses PyPDF2 to add text watermark over the PDF file at 45 degrees. Multiple watermarks are added acorss the file.
