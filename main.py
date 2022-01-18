'''
First round is done
Second round for data visualization start on 5 May 2021
'''

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
