# Mushaf_Colour_Scheme
A series of scripts to generate a Mushaf in the Uthmani script, in custom colours. The intent of this is too potentially add an aestheic drive to read more Quran (as opposed to being decoration. Hence, after using this script, it's vital that you utilise your Mushaf for the intended purpose - i.e. reading from it)

The SVG files are converted from the original Adobe Illustrator files provided by the King Fahd Complex for the Printing of the Holy Quran. This is the 1441 edition. 

## How to use?
1) Extract all the zip files in SVGS into a single folder
2) find and install any dependancies
3) Open the colour.py file in a text editor - Change the source & output folder to suit wherever you've put everything
4) Change the background, text and accent colours to whatever you want, and run the colours script with:
```
python colour.py
```
5) Change the source and output folders for the ps1 script, and run:
```
./svg_pdf.ps1
```
Make sure you've got the right inkscape paths for the ```inkscape.com``` file - the script will use inkscape to convert all the svg's into PDF files - this process is very energy intensive and takes ages

6) use the pdf_merger.py to merge all the pdf's to one. Again, edit the script to have the correct file paths
7) use bookify.py to turn it into a book (with pages going from right to left for obvious reasons) → this doesn't require editing the script, and instead runs via:
```
python bookify.py "C:\Path\to\PDF"
```

And now, after all that processing, you have your Mushaf. 
