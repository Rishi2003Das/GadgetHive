from market import app, config

#Checks if the run.py file has executed directly and not imported
doc=f'''
Initialize the program by going to http://{config['host']}:{config['port']}.
Do NOT use the other URLs listed below
'''

if __name__ == '__main__':
    print(doc)
    app.run(debug=False, port=config['port'])