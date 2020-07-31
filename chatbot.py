import pymysql
from utils import wit_response
import datetime
from datetime import datetime, timedelta, date

connenction = pymysql.connect(host = "localhost", user = "root", password = "", db="triennale_lezioni")
s =connenction.cursor()

def intent_get_aula(entities):
    data = None
    orario_inizio = None
    text_day = None
    #Controllo se nella risposta è presente una datetime e la inserisco su data. In caso negativo assegno il datetime corrente a data
    try:   
        data_string_raw = entities["wit$datetime:datetime"][0]["value"]
        data = datetime.strptime(data_string_raw,'%Y-%m-%dT%H:%M:%S.%f%z')
        text_day = entities["wit$datetime:datetime"][0]["body"]
    except:
        data = datetime.today()
        text_day = "Oggi"
    #Controllo se nella risposta è presente l'entità corso cosi da paterlo inserire in sql. In caso negativo non lo vado a considerare    
    try:
        corso = "'" + entities["corso:corso"][0]["value"] +"'"
        sql = "SELECT aula, corso, orario_inizio from lezioni WHERE orario_inizio >= %s AND data = %s AND corso REGEXP "+corso+"ORDER BY orario_inizio"
    except:
        sql = "SELECT aula, corso, orario_inizio from lezioni WHERE orario_inizio >= %s AND data = %s ORDER BY orario_inizio"
    #Eseguo la query che prende orario_inizio e data. Poi controllo se l'ora del datetime == 0 e stampo tutte le lezione. In caso contrario significa che l'utente ha specificato un orario e allora stampo solo il primo risultato della query    
    try:
        orario_inizio = data.strftime("%H:%M")
        s.execute(sql, (orario_inizio, data.strftime("%Y-%m-%d"), ))
        res = s.fetchall()  
        if(len(res) > 0):
            if(data.strftime("%H") == "00"):
                print(text_day+ " hai lezione di: ")
                for i in range (0, len(res)):
                    print(res[i][1]+" nell'aula "+res[i][0]+" alle "+str(res[i][2]))
            else:
                print(text_day + " hai lezione di: " + res[0][1] +" nell'aula " + res[0][0] + " alle " +str(res[0][2]))      
        else:
            print("Non ci sono lezioni")   
    except:
        print("Errore connessione")   

def intent_get_corso(entities):
    data = None
    orario_inizio = None
    text_day = None
    sql = None
    #Controllo se nella risposta è presente una datetime e la inserisco su data. In caso negativo assegno il datetime corrente a data
    try:
        data_string_raw = entities["wit$datetime:datetime"][0]["value"]
        data = datetime.strptime(data_string_raw,'%Y-%m-%dT%H:%M:%S.%f%z')
        text_day = entities["wit$datetime:datetime"][0]["body"]
    except:
        data = datetime.today()
        text_day = "Oggi"
    #if data.hour == "00" then lo studente non ha specificato un orario qundi restituisco tutti i corsi di quel giorno altrimenti solamente l'orario specificato   
    try:
        orario_inizio = data.strftime("%H:%M")
        if(data.strftime("%H") == "00"):
            sql = "SELECT corso from lezioni WHERE orario_inizio >= %s AND data = %s ORDER BY orario_inizio"
        else:
            sql = "SELECT corso from lezioni WHERE orario_inizio = %s AND data = %s ORDER BY orario_inizio"    
        s.execute(sql, (orario_inizio, data.strftime("%Y-%m-%d"), ))
        res = s.fetchall()  
        if(len(res) > 0):
            if(data.strftime("%H") == "00"):
                print(text_day+ " hai lezione di: ")
                for i in range (0, len(res)):
                    print(res[i][0])
            else:
                print(text_day + " hai lezione di: " + res[0][0])      
        else:
            print("Non ci sono lezioni")   
    except:
        print("Errore connessione")


def intent_get_orario(entities):
    data = None
    text_day = None
    clean_entities = None
    #Pulisco le entities dal datetime -ora- dato che wit lo rileva come datetime. ES. a che ora ho lezione domani. Inserisco la data specificata dall'utente altrimenti la data corrente
    try:
        for i in range (0, len(entities["wit$datetime:datetime"])):
            if(entities["wit$datetime:datetime"][i]["body"] != "ora"):
                clean_entities = entities["wit$datetime:datetime"][i]
                       
        if(len(clean_entities) >= 1):
            data_string_raw = clean_entities["value"]
            data = datetime.strptime(data_string_raw,'%Y-%m-%dT%H:%M:%S.%f%z')
            text_day = clean_entities["body"]
        else:
            generate_exception()    
    except:
        data = datetime.today()
        text_day = "Oggi"
    #Controllo l'esistenza dell'entità corso e costruisco la query conseguente. Stessa cosa nel momento in cui non sia presente    
    try:
        corso = "'" + entities["corso:corso"][0]["value"] +"'"
        sql = "SELECT  corso, orario_inizio from lezioni WHERE data = %s AND corso REGEXP "+corso+" ORDER BY orario_inizio"  
        #stampo i risulati della query          
        try:
            s.execute(sql, (data.strftime("%Y-%m-%d")))
            res = s.fetchall()
            if(len(res) > 0):
                print(text_day+ " hai lezione di: ")
                for i in range (0, len(res)):
                    print(res[i][0]+" alle "+str(res[i][1]))           
            else:
                print("Non ci sono lezioni")   
        except:
            print("Errore connessione")        
    except:
        sql = "SELECT corso, orario_inizio from lezioni WHERE data = %s ORDER BY orario_inizio"
        #verifico se sia presente l'entità iniziare o finire altrimenti stampo tutte le lezioni in base alla data
        try:
            entities["iniziare:iniziare"]
            try:
                s.execute(sql, (data.strftime("%Y-%m-%d")))
                res = s.fetchall()
                if(len(res)>0):
                    print(text_day + " le lezioni iniziano alle: "+str(res[0][1]))
                else:
                    print("Non ci sono lezioni")    
            except:
                print("Errore connessione")
        except:
            try:
                entities["finire:finire"]
                sql = "SELECT corso, orario_fine from lezioni WHERE data = %s ORDER BY orario_inizio"
                try:
                    s.execute(sql, (data.strftime("%Y-%m-%d")))
                    res = s.fetchall()
                    if(len(res)>0):
                        print(text_day + " le lezioni finiscono alle: "+str(res[len(res)-1][1]))
                    else:
                        print("Non ci sono lezioni")    
                except:
                    print("Errore connessione")
            except:
                try:
                    s.execute(sql, (data.strftime("%Y-%m-%d")))
                    res = s.fetchall()
                    if(len(res) > 0):
                        print(text_day+ " hai lezione di: ")
                        for i in range (0, len(res)):
                            print(res[i][0]+" alle "+str(res[i][1]))           
                    else:
                        print("Non ci sono lezioni")
                except:
                    print("Errore Connessione")        

def intent_get_quante_ore(entities):
    data = None
    text_day = None
    text_corso = None
    res = None
    #Controllo se nella risposta è presente una datetime e la inserisco su data. In caso negativo assegno il datetime corrente a data
    try:   
        data_string_raw = entities["wit$datetime:datetime"][0]["value"]
        data = datetime.strptime(data_string_raw,'%Y-%m-%dT%H:%M:%S.%f%z')
        text_day = entities["wit$datetime:datetime"][0]["body"]
    except:
        data = datetime.today()
        text_day = "Oggi"  
    #controllo se l'utente richiede le ore in una settimana oppure in un giorno specifico
    if("settimana" in text_day):
        #controllo se l'utente ha specificato le ore di un corso oppure le ore di tutti i corsi
        try:
            corso = "'" + entities["corso:corso"][0]["value"] +"'"
            sql = "SELECT corso, orario_inizio, orario_fine from lezioni WHERE data >= %s AND data <= %s AND corso REGEXP "+corso+"ORDER BY orario_inizio"
            text_corso = entities["corso:corso"][0]["value"]
        except:
            sql = "SELECT corso, orario_inizio, orario_fine from lezioni WHERE data >= %s AND data <= %s ORDER BY orario_inizio"
        end_data = data + timedelta(days = 7)
        s.execute(sql, (data.strftime("%Y-%m-%d"), end_data.strftime("%Y-%m-%d")))
        res = s.fetchall()
    else:
        try:
            corso = "'" + entities["corso:corso"][0]["value"] +"'"
            sql = "SELECT corso, orario_inizio, orario_fine from lezioni WHERE data = %s AND corso REGEXP "+corso+"ORDER BY orario_inizio"
            text_corso = entities["corso:corso"][0]["value"]
        except:
            sql = "SELECT corso, orario_inizio, orario_fine from lezioni WHERE data = %s ORDER BY orario_inizio"
        s.execute(sql, (data.strftime("%Y-%m-%d")))
        res = s.fetchall()
    tot_ore = conta_ore(res)
    if(tot_ore == timedelta(hours=0)):
        print("Non ci sono lezioni")
    else:    
        if(text_corso != None):
            print(text_day + " hai "+ str(tot_ore) + " ore di " + text_corso)
        else:
            print(text_day + " hai "+ str(tot_ore) + " ore di lezione")        

def conta_ore(res):
    tot_ore = timedelta(hours=0)
    for i in range(0, len(res)):
        tot_ore += (res[i][2] - res[i][1])
    return tot_ore    



def bot():
    while(True):
        user_request = input("Come posso esserti utile?:\n")
        intent, entities = wit_response(user_request)
        if(intent == "get_aula"):
            intent_get_aula(entities)
        elif(intent == "get_corso"):
            intent_get_corso(entities)
        elif(intent == "get_orario"):
            intent_get_orario(entities)
        elif(intent == "get_quante_ore"):
            intent_get_quante_ore(entities)

            

bot()