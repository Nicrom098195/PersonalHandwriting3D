# PersonalHandwriting3D  
A program that can read, save, and use someone's handwriting with just a 3D printer and a pen.

## What is this?  
**PersonalHandwriting3D** is a Python software designed to learn your handwriting and use it with a 3D printer adapted as a pen plotter.

## How can I use it?  
Easy! Just clone the repository by running:  
```bash
git clone https://github.com/Nicrom098195/PersonalHandwriting3D.git
```  
in your terminal, or download the ZIP file. Then run the **main.py** file to generate a G-code file named **out.gcode**.  
If you want to quickly change the text, just edit the **text.txt** file with a text editor.

## How can I customize my text?  
Again, it's easy! You can provide arguments to the **main.py** file in your terminal. Here’s an example command with all the options:  

```bash
python3 main.py -in text.txt -out out.gcode -size 10 -space 1 --show
```  

or  

```bash
python3 main.py -text "This is a test" -out out.gcode -size 10 -space 1 --show
```  

### Note:  
If you use the **-in** or **-txt** arguments, you must also use the **-out** argument.  

### Explanation of Arguments:  
- **-in** `<filename>`: Specifies the input file containing plain text (e.g., a `.txt` file, not `.pdf` or `.doc`).  
- **-txt** `<text>`: An alternative to **-in**. Provides the program with the text directly, without reading a file.  
- **-out** `<filename>`: Specifies the output file path. The default is **out.gcode**.  
- **-size** `<number>`: Sets the text size in millimeters. Default is **10**.  
- **-space** `<number>`: Defines letter spacing. If set to `0` or omitted, spacing will be automatically calculated based on the letter.  
- **-linesp** `<number>`: Defines line spacing. If set to `0` or omitted, spacing will be automatically calculated based on the font size.  
- **--show**: Displays the result as dots.  
- **--showl**: Displays the full lines in the result.  
  > By default, nothing will be displayed.

## How can I use my own handwriting?  
Using your handwriting is as simple as drinking a glass of water.  

1. Run the **config.py** file using:  
   ```bash
   python config.py
   ```  
2. A white window will appear, prompting you to draw a letter.  
   - Don’t worry about the size; it will be adjusted automatically later.  
   - The program may ask for the same letter multiple times to collect variants for smoother text.  

3. After 1 second of inactivity, the window will close and prompt you to draw another letter.  

4. When you finish drawing all required letters, the program will save your handwriting in the **font.json** file.  

You can modify letter settings at the beginning of the **config.py** and **writer.py** files.

## License  
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Nicrom098195/PersonalHandwriting3D/blob/main/LICENSE "LICENSE") file for details.  