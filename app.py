from flask import Flask, render_template, flash, request, url_for, redirect,session
from dbconnection import executeQuery
from dbconnection import updateQuery
from datetime import timedelta
from datetime import datetime
from dbconnection import insertDailyData
app = Flask(__name__)
app.config['SECRET_KEY']='sample'

@app.route("/")
def initial():
    #qry = "SELECT tag as name,sum(value) as 'value',sum(target) as 'target' FROM invest_data  group by tag"
    qry = "select name,target_perc_reached as value,target from tr_targets"
    axisemi=executeQuery(qry)
    ae=[]
    avg_axisemi=0
    insertDailyData()
    for i in axisemi:
        avg_axisemi = i[1]
        ae.append([i[0].upper(),i[1]])
    avg_axisemi=round(avg_axisemi/len(axisemi))
    print("------------------------Printing values-------------------------")
    print(axisemi)
    print("------------------------Printing values-------------------------")


    return render_template("index.html",ae=axisemi)

@app.route("/initialbackup")
def initialbackup():
    res,short,lng,axisemi=executeQuery()
    cur=[]
    sh=[]
    ln=[]
    ae=[]
    avg_long=avg_short=avg_axisemi=0
    for i in res:
        cur.append([i[0].upper(),round(((i[1])/i[2])*100)])
    print(cur)
    insertDailyData()
    for i in short:
        avg_short+=((i[1])/i[2])*100
        sh.append([i[0].upper(),round(((i[1])/i[2])*100)])
    avg_short=round(avg_short/len(short))
    for i in lng:
        avg_long+=((i[1])/i[2])*100
        ln.append([i[0].upper(),round(((i[1])/i[2])*100)])
    avg_long=round(avg_long/len(lng))
    for i in axisemi:
        avg_axisemi+=((i[1])/i[2])*100
        ae.append([i[0].upper(),round(((i[1])/i[2])*100)])
    avg_axisemi=round(avg_axisemi/len(axisemi))
    print("------------------------Printing values-------------------------")
    print(axisemi)
    print("------------------------Printing values-------------------------")
    return render_template("index.html",ae=axisemi)

@app.route("/targets")
def gettargets():
    print("reached targets page")
    updateTargets()
    return render_template("targets.html")

def updateScripts():
    qry = "select name,tag,sum(value)/count(value) as avg_value,sum(quantity) as units from tr_trades group by name,tag"
    avgList = executeQuery(qry)
    for avgItem in avgList:
        qry = "update script_details set avg_value = "+str(avgItem[2])+", units="+str(avgItem[3])+" where name = '"+avgItem[0]+"' and tags='"+avgItem[1]+"'"
        print("Updating script details qry:"+qry)



def updateTargets():
    #Get all the targets whose status is open and next target is crossed and final target is > today.
    qry = "select name,qty,target,final_target_date,recurrance,target_type,description,startdate,status from targets where status = 'OPEN' AND (next_target_date < now() or next_target_date is null) and final_target_date > now()"
    targetList = executeQuery(qry)
    for targetItem in targetList:
        insertValues = []
        for itemValue in targetItem:
            insertValues.append(itemValue)
        #TODO Calculate target date using reccurance 
        insertValues[3] = '2020-10-24'
        insertValues[7] = (insertValues[7]).strftime('%Y-%m-%d')
        qry = "INSERT INTO tr_targets(name,qty,target,target_date,recurrance,target_type,description,startdate,status) VALUES %r;" % (tuple(insertValues),)
        print(qry)
        updateQuery(qry)
        #TODO Calculate target date using reccurance 
        insertValues[3] = '2020-10-24'
        qry = "update targets set next_target_date = '"+insertValues[3]+"' where name = '"+insertValues[0]+"'"
        print("Updating next target date qry:"+qry)
        updateQuery(qry)
    
    #Updating existing target status.
    #Get the list of open targets find the change and update in tr_targets.
    qry = "select distinct name from tr_targets where status = 'OPEN'"
    targetList = executeQuery(qry)
    for targetItem in targetList:
        #TODO recheck the below calculation for change value.
        qry = "select (sum(current_value*units) - sum(avg_value*units)) as change_value from script_details where tags = '"+targetItem[0]+"' group by tags" 
        print(qry)
        changeValueList = executeQuery(qry)
        for changeValue in changeValueList:
            print("change values")
            print(changeValue)
            print("change value for "+targetItem[0]+":"+str(changeValue[0]))
            qry = "update tr_targets set amt_changed = "+str(changeValue[0])+",target_perc_reached = ("+str(changeValue[0])+"/target)*100 where name = '"+targetItem[0]+"'"
            #TODO update table 
            print("updating change in tr_target:"+qry)
            updateQuery(qry)


    #No need to run everytime place somewhere
    updateScripts()

if __name__ == "__main__":
    #app.secret_key="dwqwfewfwqdqw"
    app.run(host="0.0.0.0", port="8222")
