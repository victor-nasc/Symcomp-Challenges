import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('textFile')

    args = parser.parse_args()

    fileName = args.textFile

    with open(fileName, "r") as f:
        text = f.read()

        html_content = """
        <html>
        <body>
        """

        for i, char in enumerate(text.split(" ")):
            if i % 3 == 0:
                html_content += f'<span style="color:red;">{char} </span>'
            if i % 3 == 1:
                html_content += f'<span style="color:green;">{char} </span>'
            if i % 3 == 2:
                html_content += f'<span style="color:blue;">{char} </span>'
        html_content += """
        </body>
        </html>
        """
    
    with open("saida.html", "w") as out_file:
        out_file.write(html_content)

if __name__ == "__main__":
    main()