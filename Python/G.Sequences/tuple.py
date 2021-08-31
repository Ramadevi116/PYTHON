# tuple:
Baby_toys=("Ball","kite","train","bat","setting kits","teddy bear")
# indexing:
len1=len(Baby_toys)
for i in range(len1):
    print(Baby_toys[i])
print(Baby_toys[2])
print(Baby_toys[4])

# slicing:
print(Baby_toys[2:5])
print(Baby_toys[1:3])

# Concatenation:
print(Baby_toys+("car","drums"))

# repetition:
print(Baby_toys*2)

'''o/p:
# indexing:
kite
train
bat
setting kits
teddy bear

train
setting kits
# slicing:
('train', 'bat', 'setting kits')
('kite', 'train')
# Concatenation:
('Ball', 'kite', 'train', 'bat', 'setting kits', 'teddy bear', 'car', 'drums')
# repetition:
('Ball', 'kite', 'train', 'bat', 'setting kits', 'teddy bear', 'Ball', 'kite', 'train', 'bat', 'setting kits', 'teddy bear')
'''

