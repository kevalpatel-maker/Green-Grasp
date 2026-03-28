import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def haz(a):
    if a<100:
        print(" CLEAN & SAFE ENVIRONMENT \n- Healthy air and water quality\n- No noticeable health risks\n- Ideal for productivity and outdoor activities")
    elif 100<=a<140:
        print(" MODERATE POLLUTION \n- Mild breathing issues\n- Slight decrease in concentration\n- Occasional discomfort during outdoor activities")
    else:
        print(" SEVERE POLLUTION ALERT \n- High risk of lung diseases and asthma\n- Severe drop in student concentration and productivity\n- Increased fatigue, headaches, and irritation\n- Long-term exposure may reduce life expectancy")

def act(a):
    if a<100:
        print(" KEEP IT UP! \n- Maintain current lifestyle\n- Encourage others to follow eco-friendly habits\n- Participate in sustainability initiatives")
    elif 100<=a<140:
        print(" PREVENTIVE MEASURES \n- Reduce unnecessary travel\n- Save electricity and water\n- Avoid single-use plastics\n- Spread awareness among peers")
    else:
        print(" URGENT ACTION REQUIRED \n- Avoid outdoor exposure completely\n- Use masks and air purifiers\n- Shift to online/indoor activities\n- Reduce vehicle usage drastically\n- Promote tree plantation drives")

def comp(a,b):
    
        aqiA=np.array([df[df["state"]==a]["Jan-Feb"].values[0],df[df["state"]==a]["Mar-Apr"].values[0],df[df["state"]==a]["May-Jun"].values[0],df[df["state"]==a]["Jul-Aug"].values[0],df[df["state"]==a]["Spt-Oct"].values[0],df[df["state"]==a]["Nov-Dec"].values[0]])
        aqiB=np.array([df[df["state"]==b]["Jan-Feb"].values[0],df[df["state"]==b]["Mar-Apr"].values[0],df[df["state"]==b]["May-Jun"].values[0],df[df["state"]==b]["Jul-Aug"].values[0],df[df["state"]==b]["Spt-Oct"].values[0],df[df["state"]==b]["Nov-Dec"].values[0]])
        m=np.array(['Jan-Feb','Mar-Apr','May-Jun','Jul-Aug','Spt-Oct','Nov-Dec'])
        print("Graph :")
        plt.bar(np.arange(len(aqiA))-0.2,aqiA,width=0.4,label=a,color='gold')
        plt.bar(np.arange(len(aqiB))+0.2,aqiB,width=0.4,label=b,color='silver')
        plt.xticks(np.arange(len(m)),m)
        plt.xlabel('Months')
        plt.ylabel('AQI')
        plt.title("Comparison of AQI between "+a+" and "+b)
        plt.legend()
        plt.show()
        
# Dataset
data={"state": [
        "Delhi", "Rajasthan", "Gujarat", "Maharashtra",
        "Uttar Pradesh", "Haryana", "Punjab", "West Bengal",
        "Assam", "Kerala", "Tamil Nadu"],
    "Jan-Feb": [145, 110, 107, 169, 161, 152, 154, 86, 97, 176, 107],
    "Mar-Apr": [130, 186, 99, 112, 140, 126, 165, 181, 93, 151, 137],
    "May-Jun": [213, 151, 111, 158, 170, 167, 188, 159, 142, 138, 125],
    "Jul-Aug": [181, 106, 117, 133, 173, 175, 167, 176, 121, 155, 97],
    "Spt-Oct": [122, 147, 101, 102, 127, 129, 132, 136, 90, 112, 78],
    "Nov-Dec": [145, 94, 121, 86, 130, 118, 142, 140, 102, 88, 54]}
df=pd.DataFrame(data)

#__Main__
print("|||–––––––––––GreenGrasp : Real-Time Environmental('AQI') Awareness & Impact Analyzer–––––––––––|||")
print("--------------------------------------------------------------------------------------------------------------------")
input("PRESS ENTER")
print("Select any State :")
for i, state in enumerate(data['state']):
    print(f"{i+1}. {state}")
ch=int(input("\nEnter your choice (1-11): "))
s_s=data['state'][ch-1]
while True:
    print("--------------------------------------------------------------------------------------------------------------------")
    print("1. Get Data\n2. Hazards and Measures\n3. Comparison between State\n4. Exit")
    op=int(input("Enter option: "))
    if op==1:
        print("--------------------------------------------------------------------------------------------------------------------")
        s_d=df[df["state"]==s_s]
        print("Dataset :\n", s_d)
        aqi=np.array([df[df["state"]==s_s]["Jan-Feb"].values[0],df[df["state"]==s_s]["Mar-Apr"].values[0],df[df["state"]==s_s]["May-Jun"].values[0],df[df["state"]==s_s]["Jul-Aug"].values[0],df[df["state"]==s_s]["Spt-Oct"].values[0],df[df["state"]==s_s]["Nov-Dec"].values[0]])
        m=np.array(['Jan-Feb','Mar-Apr','May-Jun','Jul-Aug','Spt-Oct','Nov-Dec'])
        print("Graph :")
        plt.plot(m,aqi,color='black',linestyle='dashed',linewidth=3,marker='o',markerfacecolor='red',markersize=10)
        plt.xlabel("Months")
        plt.ylabel("AQI")
        plt.title(s_s+' AQI Trend')
        plt.show()

    elif op==2:
        print("--------------------------------------------------------------------------------------------------------------------")
        s_d=df[df["state"]==s_s]
        summ=df[df["state"]==s_s]["Jan-Feb"].values[0]+df[df["state"]==s_s]["Mar-Apr"].values[0]+df[df["state"]==s_s]["May-Jun"].values[0]+df[df["state"]==s_s]["Jul-Aug"].values[0]+df[df["state"]==s_s]["Spt-Oct"].values[0]+df[df["state"]==s_s]["Nov-Dec"].values[0]
        gs=summ//6
        print("Hazards :")
        haz(gs)
        print("Measures :")
        act(gs)

    elif op==3:
        print("--------------------------------------------------------------------------------------------------------------------")
        print("Select a State :")
        for i, state in enumerate(data['state']):
            print(f"{i+1}. {state}")
        ch=int(input("\nEnter your choice (1-11): "))
        b_s=data['state'][ch-1]
        comp(s_s,b_s)
        
    elif op==4:
        print("--------------------------------------------------------------------------------------------------------------------")
        print("Program Completed Successfully")
        break

    else:
        print("Invalid option, try again.")

