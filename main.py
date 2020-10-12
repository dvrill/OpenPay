from flask import Flask, request
import json

users = {
	"test" = "test2"
}

money = {
	"test" = 10
}

app = Flask(__name__)

@app.route('/accredita/<username>/<password>/<soldi>')
def aggiungi(username, password, soldi):
    get_Cred()
    get_Pass()
    if checkInt(soldi) == False:
        return '{"stato" = "KO", "soldi" = "0"}'
    money[username] = money[username] + int(soldi)
    save_Cred()
    if users[username] == password:
        return '{"stato" = "OK", "soldi" = "'+str(money[username])+'"}'
    else:
        return '{"stato" = "KO", "soldi" = "0"}'


@app.route('/accredita/<username>/<password>/<soldi>')
def aggiungi(username, password, soldi):
    get_Cred()
    get_Pass()
    if checkInt(soldi) == False:
        return '{"stato" = "KO", "soldi" = "0"}'
    money[username] = money[username] + int(soldi)
    save_Cred()
    if users[username] == password:
        return '{"stato" = "OK", "soldi" = "'+str(money[username])+'"}'
    else:
        return '{"stato" = "KO", "soldi" = "0"}'

@app.route('/preleva/<username>/<password>/<soldi>')
def togli(username, password, soldi):
    get_Pass()
    get_Cred()
    if checkInt(soldi) == False:
        return '{"stato" = "KO", "soldi" = "0"}'
    money[username] = money[username] - int(soldi)
    save_Cred()
    if users[username] == password:
        return '{"stato" = "OK", "soldi" = "'+str(money[username])+'"}'
    else:
        return '{"stato" = "KO", "soldi" = "0"}'

app.run()
