import matplotlib.pyplot as plt    
import numpy as np    
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', 'r', 'b']      
with open('yh.txt', 'r') as f:  
    lines = f.readlines()  
labels = []  
data = []  
for line in lines:  
    parts = line.strip().split()    
    labels.append(parts[0])    
    data_row = [int(i) for i in parts[2:]]  
    if data_row:  
        data.append(max(data_row)) 
    else:  
        data.append(0) 
fig, ax = plt.subplots(figsize=(10,8))  
bars1 = ax.bar(labels, data, align='center', alpha=0.7, color=colors)  
ax.set_xticks(np.arange(len(labels))) 
ax.set_xticklabels(labels) 
ax.set_yticks(np.arange(0,520,20)) 
for bar in bars1:  
    height = bar.get_height()  
    ax.text(bar.get_x() + bar.get_width() / 2, height,  
            str(height),                
            va='bottom',              
            ha='center',               
            fontsize=10)               
plt.show()