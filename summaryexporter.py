import pandas as pd


def export_to_html(str_content, filename):
    """
    Export the DataFrame to an HTML file with a specific format.
    
    Parameters:
        df (DataFrame): The DataFrame to export.
        filename (str): The name of the output HTML file.
    """
    
    
    htmltemplate = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            h1 {font-size: 1.5em;}
            h2 {font-size: 1.0em;}

            
            #IdSectionName p {
                margin-bottom: 0.4em;  
                margin-top: 0.4em;
                font-size: 1.2em;
                text-indent: 1em;
                margin-left: 10px;
                text-align: center;
                color: grey; /* Color for section names */
                font-weight: bold; /* Making paragraphs boldface */
                font-family: Arial; /* Specific font for paragraphs */
            }

            
            #IdExercise p {
                padding: 3px; 
                border: 1px solid red;
                margin-bottom: 0.4em;  
                margin-top: 0.4em;
                font-size: 0.8em;
                text-indent: 1em;
                margin-left: 10px;
                font-weight: bold; /* Making paragraphs boldface */
                # font-family: "Times New Roman", Times, serif; /* Specific font for paragraphs */
            }
        </style>
        <title>Readme</title>
    </head>
    <body>
        <Marker: Here_is_body>
    </body>
    </html>
    """
    
    
    html_content = htmltemplate.replace("<Marker: Here_is_body>", str_content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)




df = pd.read_csv('ExStewartList_copy.csv',sep=';', header=0, encoding='utf-8')
print(df)

nr_of_sections = len(df[df['SectionRef'].str.startswith('Section ')])
nr_of_exercises = len(df) - nr_of_sections

mycnt = 0
str_content = ""
for n in range(len(df)):
    row = df.iloc[n]
    secRef = row['SectionRef']
    secName = row['SectionName']
    
    if("Section" in secRef):
        # htmlrow = f'<div id="IdSectionName"><p align="center">{secRef}: {secName}</p></div>'
        htmlrow = f'<div id="IdSectionName"><p>{secRef}: {secName}</p></div>'
    
    else:
        mycnt += 1
        htmlcnt = f'<span style="color: rgb(66, 63, 63); font-size: 0.7em;">[{mycnt}/{nr_of_exercises}]</span>'
        htmlrow = f'<div id="IdExercise"><p>{secRef} {htmlcnt}: {secName}</p></div>'
    
    str_content += htmlrow + "\n"


export_to_html(str_content, "htmlstuff.html")