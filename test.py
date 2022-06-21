import pandas as pd

f = open(r'E:\code\Bert-Pytorch-TextClassification-master\THUCNews\data\test.txt', encoding='utf-8')
# f = open('E:\code\Bert-Pytorch-TextClassification-master\THUCNews\data\dev.txt', encoding='utf-8')
data = f.readlines()
f.close()
# print(type(data))
# print(data)
labels = [int(x[-2]) for x in data]
print(len(labels))
print(labels)
lis = []
for i in range(0, 10):
    a = labels.count(i)
    lis.append(a)
print(lis)
# labels_unique = list(set(labels))
# labels_unique = dict(zip(labels_unique, range(len(labels_unique))))
# print(labels_unique)
# # print(labels_unique['时尚'])
# contexts = [x.split("\t")[1] for x in data]
# # print(len(contexts))
# f1 = open(r'Cnews/data/dev.txt', 'w', encoding='utf-8')
# for label, context in zip(labels, contexts):
#     label_index = labels_unique[f'{label}']
#     text = context.strip() + '\t' + str(label_index)+ '\n'
#     # print(text)
#     f1.write(text)
# f1.close()