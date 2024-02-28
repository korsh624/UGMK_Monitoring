from flask import Flask, render_template, request,redirect
from mysql.connector import connect
import datetime
import dbmodel
app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template('index.html')

@app.route('/')
def admin():
    spd = 0
    sboy = 0
    avaria = 0
    drugoe = 0
    polfabrikat=0
    narushenie=0
    peregruz =0
    iznos =0
    netmaterialov=0
    vihod=0
    tehno =0
    mehanicheskie=0
    org=0
    smej =0
    trud=0

    conn = connect(

        user='gb_ugmk',

        password='XyqbS49JX-pP',

        host='mysql94.1gb.ru',

        database='gb_ugmk',
        ssl_disabled=True)
    cur = conn.cursor()
    cur.execute('SELECT * FROM monitor')

    bdinfo = cur.fetchall()
    bdinfo = list(reversed(bdinfo))

    # print(bdinfo)

    Alltime = datetime.datetime(2022, 12, 22, 22, 22, 22) - datetime.datetime(2022, 12, 22, 22, 22, 22)

    for i in range(len(bdinfo)):
        if "Снижение скорости на оборудовании" in bdinfo[i]:
                spd=spd+1
        elif "Сбой настроек в оборудовании" in bdinfo[i]:
                sboy=sboy+1
        elif "Отсутствие полуфабриката" in bdinfo[i]:
               polfabrikat=polfabrikat+1
        elif "Аварийная остановка" in bdinfo[i]:
                avaria=avaria+1
        elif "Нарушение правил эксплуатации"in bdinfo[i]:
                narushenie=narushenie+1
        elif "Перегрузка отдельных механизмов"in bdinfo[i]:
                peregruz=peregruz+1
        elif "Износ отдельных деталей и узлов"in bdinfo[i]:
                iznos=iznos+1
        elif "Выход из строя отдельных механизмов"in bdinfo[i]:
                vihod=vihod+1
        elif "Несвоевременная подача материалов на рабочее место"in bdinfo[i]:
                netmaterialov=netmaterialov+1
        elif "Технологический простой"in bdinfo[i]:
                tehno=tehno+1
        elif "Механический или плановый простой"in bdinfo[i]:
                mehanicheskie=mehanicheskie+1
        elif "Организационный простой"in bdinfo[i]:
                org=org+1
        elif "Трудовой простой"in bdinfo[i]:
                trud=trud+1
        elif "Смежный простой"in bdinfo[i]:
                smej=smej+1
        else:
                drugoe=drugoe+1

    # print(spd,sboy,polfabrikat,avaria,drugoe,narushenie,peregruz,iznos,vihod,netmaterialov,tehno,mehanicheskie,org,trud,smej)

    for i in range(len(bdinfo)):
        year = bdinfo[i][1][0] + bdinfo[i][1][1] + bdinfo[i][1][2] + bdinfo[i][1][3]
        month = bdinfo[i][1][5] + bdinfo[i][1][6]
        day = bdinfo[i][1][8] + bdinfo[i][1][9]
        hour = bdinfo[i][1][11] + bdinfo[i][1][12]
        minute = bdinfo[i][1][14] + bdinfo[i][1][15]
        ms = bdinfo[i][1][17] + bdinfo[i][1][18]

        yeart = bdinfo[i][2][0] + bdinfo[i][2][1] + bdinfo[i][1][2] + bdinfo[i][1][3]
        montht = bdinfo[i][2][5] + bdinfo[i][2][6]
        dayt = bdinfo[i][2][8] + bdinfo[i][2][9]
        hourt = bdinfo[i][2][11] + bdinfo[i][2][12]
        minutet = bdinfo[i][2][14] + bdinfo[i][2][15]
        mst = bdinfo[i][2][17] + bdinfo[i][2][18]

        Dt = datetime.datetime(int(yeart), int(montht), int(dayt), int(hourt), int(minutet),int(mst)) - datetime.datetime(int(year), int(month), int(day), int(hour), int(minute),int(ms))
        Alltime = Alltime + Dt
        i+1
        # print(year,month,day,hour,minute)
        # print(yeart,montht,dayt,hourt,minutet)
        # print(Alltime)

    conn.close()
    return render_template('admin.html',bdinfo=bdinfo,Alltime=Alltime,spd=spd,sboy=sboy,polfabrikat=polfabrikat,
                           avaria=avaria,drugoe=drugoe,narushenie=narushenie,peregruz=peregruz,
                           iznos=iznos,vihod=vihod,netmaterialov=netmaterialov,tehno=tehno,mehanicheskie=mehanicheskie,
                           org=org,trud=trud,smej=smej)
@app.route('/testadmin')
def testadmin():
    return render_template('testadmin.html')


if __name__=="__main__":
    app.run(debug=True)

