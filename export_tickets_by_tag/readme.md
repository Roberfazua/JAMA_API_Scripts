# Export_tickets_by_tag

<h2>IMPUTS</h2>

- TAG -> Jama is case sensitive, but with some error handling the script handle it
- TAGSFILE -> If you already have a tag json list you want to compare and search



<h2>This scripts export:</h2>

- Project list (json)
- Tags in project "Porche ebike" (id_project = 55) (json)
- Tickets related with this IMPUT tag (json and csv)



<h2>HOW TO</h2>

1. Update the env.py with your own credentials
2. Create venv for use with your virtual enviroment
3. install requirements.txt
4. Launch main.py with imput parameters requirements
   4.1 --help

   ```python
   > python.exe .\main.py --h
    usage: main.py [-h] --tag TAG [--tagsfile TAGSFILE]
    
    Jama API Data Export Utility
    
    options:
      -h, --help           show this help message and exit
      --tag TAG            Tag name to search for
      --tagsfile TAGSFILE  Path to Tags.json file (optional, will use latest if not provided)
   ```
   
   4.2 --tag
   
    ```python
    > python.exe .\main.py --tag Regression
    Jama API Data Export Utility
    250709 - 105957 - Tags.json
    Found 1 match(es) for tag 'Regression':
    1: ID=133, Name='Regression', Project=55
    Export complete!
    ```
   
   4.3 --tagsfile
   
    ```python
    > python.exe .\main.py --tag regression --tagsfile .\debug_tags.json
    Jama API Data Export Utility
    250709 - 124017 - Tags.json
    Found 1 match(es) for tag 'regression':
    1: ID=133, Name='Regression', Project=55
    Export complete!
    ```
