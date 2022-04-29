from django.http import HttpResponse
from django.shortcuts import render
from .models import Canciones, Historial
from json import dumps
import sqlite3
# Create your views here.
def Dashboard(request):
    if request.method == 'GET':

        #u = Distancia.objects.all()

        #data = [[h_var,v_var]]
        h_var = 'Points per game'
        v_var = 'Time played in minutes'
        data = [[h_var,v_var]]
        # for i in range(0,11):
        #     data.append([randrange(101),randrange(101)])
        h_var_json = dumps(h_var)
        v_var_json = dumps(v_var)
        # datos_json = dumps(data)

        mydb = sqlite3.connect("db.sqlite3")
        cur = mydb.cursor()
        stringSQL = '''SELECT Puntos_por_partida, Tiempo_jugado FROM Graficacion_Historial ORDER BY Puntos_por_partida DESC'''
        rows = cur.execute(stringSQL)
        listasalida = []
        for i in rows:
            print(i)
            d = {}
            d['puntos'] = i[0]
            d['tiempo'] = i[1]
            data.append([i[0],i[1]]) #Necesita dos numeros
        datos_json = dumps(data)

        #Grafica 2

        #data = [[h_var,v_var]]
        h_var2 = ' ID Canciones'
        v_var2 = ' Puntos por partida'
        #v_var3 = 'Puntos'
        data2 = [[h_var2,v_var2]]
        # for i in range(0,11):
        #     data.append([randrange(101),randrange(101)])
        h_var_json2 = dumps(h_var2)
        v_var_json2 = dumps(v_var2)
        # datos_json = dumps(data)

        mydb2 = sqlite3.connect("db.sqlite3")
        cur2 = mydb2.cursor()
        stringSQL2 = '''SELECT Puntos_por_partida, ID_Canciones FROM Graficacion_Historial ORDER BY ID_Canciones ASC'''
        rows2 = cur2.execute(stringSQL2)
        listasalida2 = []
        for i in rows2:
            print(i)
            d = {}
            d['Nombre'] = i[0]
            d['id'] = i[1]
            
            data2.append([i[1],i[0]]) #Necesita dos numeros
        datos_json2 = dumps(data2)

        return render(request, 'users/Dashboard.html',{'values':datos_json, 'h_title':h_var_json,'v_title':v_var_json, 'values2':datos_json2, 'h_title2':h_var_json2,'v_title2':v_var_json2})
    else:
        return HttpResponse("Por favor utiliza GET")