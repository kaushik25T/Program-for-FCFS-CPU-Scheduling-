def waiting_time(tat,bt):
    test=[]
    result3=[]
    x=0
    for i in bt:
        test.append(bt[i])
    for i in tat:
        result3.append(i-test[x])
        x=x+1
    return result3
def turn_around_time(ct,at):
    result2=[]
    x=0
    for i in ct:
        result2.append(i-at[x])
        x=x+1
    return result2
def complition_time(p,p_a,p_b,a_t):
    process=p
    arrival_time=a_t
    process_arrival_time=p_a
    process_burst_time=p_b
    x=0
    complition_time=0
    result1=[]
    
    for i in process:
        if (arrival_time[x]==process_arrival_time[i] and complition_time >= arrival_time[x]):
            complition_time+=process_burst_time[i]
            result1.append(complition_time)
            x=x+1
        else:
            complition_time=complition_time+1
            process.insert(x+1,i)
    return(result1)
import pandas as pd 
process=['p1','p2','p3','p4']
arrival_time=[0,1,5,6]
process_arrival_time={'p1':0,'p2':1,'p3':5,'p4':6}
process_burst_time={'p1':2,'p2':2,'p3':3,'p4':4}
result1=complition_time(process,process_arrival_time,process_burst_time,arrival_time)
result2=turn_around_time(result1,arrival_time)
result3=waiting_time(result2,process_burst_time)
df= pd.DataFrame({'Process':['p1','p2','p2','p4'],'Complition_Time':result1 , 'Turn_Around_Time':result2 , 'Waiting_Time':result3})
df.set_index('Process' , inplace=True)
print(df)
