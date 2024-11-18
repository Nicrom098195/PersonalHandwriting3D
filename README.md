# PersonalHandwriting3D
 A program that can read, save and use someone's handwriting with just a 3d printer and a pen

## What is this?
PersonalHandwriting3D is a python software designed to learn your handwriting and use it with a 3D printer, adapted as a Pen Plotter.

## How can I use it?

Easy! Just clone the repository by running `git clone https://github.com/Nicrom098195/PersonalHandwriting3D.git` in your terminal or downloading the Zip file, and run the **main.py** file to get a gCode in the **out.gcode** file.
If you want to rapidly change the text, just edit the **text.txt** file with a text editor.

## How can I customize my text?

Again, it's easy! You can give the **main.py** file some arguments in your terminal. An example command, with all the options, is:

`python3 main.py -in text.txt -out out.gcode -size 10 -space 1 --show`

`python3 main.py -text "This is a test" -out out.gcode -size 10 -space 1 --showl`

Note: if you pass the **-in** argument or the **-txt** argument, you have to pass the **-out** argument too

Now, what does the above command mean?

- The **-in** argument with a filename after it specifies the input file, the file where you have the plain text (ex. a **.txt** file, not a .pdf or a .doc) to print.

- The **-txt** argument is an alternative to the -in argument, giving the program directly the text to write, without opening a file.

- The **-out** argument specifies the output file path. The default is **out.gcode**.

- The **-size** argument defines the text's size in mm. The default value is 10.

- The **-space** argument defines the letter spacing. By default or by setting it to 0, the spacing will be automatcally calculated based on the letter.

- The **--show** and **--showl** arguments just show the result on the screen, with the only difference being the first one to just show dots and not the full lines. By default, it won't show anything.

## How can i use my own handwriting?

Using your handwriting is as easy as drinking a cup of water. Just run the **config.py** file by doing `python config.py`. A white window will appear, asking you to draw a letter. Don't worry about the size, it will be automatically adjusted later. It can ask to draw a letter multiple times, just so it can use more variants and make a smoother text. After 1 second not writing, the window will close and another one will open, asking another letter or, like I said before, the same one. After drawing every letter, it will stop asking and save your handwriting in the **font.json** file.

You can change the letter settings at the beginning of the **config.py** file.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Nicrom098195/PersonalHandwriting3D/blob/main/LICENSE "LICENSE") file for details.