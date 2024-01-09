
import pandas

data = pandas.read_csv('squirrel_data.csv')
print(data.columns)

print(
    data['Primary Fur Color']
)
gray_squirrels = data[data['Primary Fur Color'] == "Gray"]
print(gray_squirrels)
print(len(gray_squirrels))
cinnamon_squirrels = data[data['Primary Fur Color'] == "Cinnamon"]
print(cinnamon_squirrels)
print(len(cinnamon_squirrels))
black_squirrels = data[data['Primary Fur Color'] == "Black"]
print(black_squirrels)
print(len(black_squirrels))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray_squirrels), len(cinnamon_squirrels), len(black_squirrels)]
}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')

# count = []
# for col in df:
#     count.append(col)
