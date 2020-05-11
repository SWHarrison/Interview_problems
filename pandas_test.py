import pandas as pd
raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
            'age': [20, 19, 22, 21],
            'favorite_color': ['blue', 'blue', 'yellow', "green"],
            'grade': [88, 92, 95, 70]}

df = pd.DataFrame(raw_data)

allowed_colors = ['blue','green']
current_df = pd.DataFrame()
for color in allowed_colors:
    to_add = df[df['favorite_color'] == color]
    current_df = pd.concat([current_df,to_add])

print(current_df[current_df['grade'] >=60])

#print(df[df['favorite_color'] in allowed_colors])
#print(df[((df['favorite_color'] == 'blue') | (df['favorite_color'] == 'yellow')) & (df['grade']>=90)])
