from flask import Flask
from read import explorer


app=Flask(__name__)


@app.route('/')
def expl():
	try:
		data=explorer()
		print(data)
		return(str(data))
	except Exception as error:
		print("ERROR")
		return(str(error))


if __name__ == '__main__':
	app.run('0.0.0.0', port=2222, debug=True)