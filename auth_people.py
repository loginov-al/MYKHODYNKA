import random
from urllib import response
import requests
import secrets
from main import app
from flask import Flask, render_template, jsonify
from db_brouser import db


# ----------------------------------- Bakend ----------------------------------- #

@app.route("/auth/login/code/telegram", methods=["GET", "POST"])
def login_api_craete_sms():
    login_data = requests.json
    phone = login_data['phone'].replace('+', '').replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    people_info = people_info.oquery.filter_by(phone=phone).first()
    people_info = people_info.query.filter_by(phone=phone).first()
    if not people_info:
        return jsonify({'status': 'error', 'message': 'student not found'}), 404
    

    code = random.generate(1000, 9000)
    db.sesion.comit


    response = requests.post(
        f'https://{config.SMS_EMAIL}:{config.SMS_API_KEY}@gate.smsaero.ru/v2/telegram/send',
        json={
            'number': people_info.phone,
            'code': code,
        }
    )





# Создание аккунта #
@app.route("/create_accunt_people")
def people_accunt():
    people_id = requests.args.get("people_id")
    if not people_id():
        return render_template("404.html")
    

    student_info = people_id.query.filter_by(id=people_id).first()
    if not student_info:
        return render_template('404.html'), 404

    return render_template("create_people_accunt.html")








