import tensorflow as tf

# x:输入， y:标签
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
# 样本数量
nums = 10
# 权重值,
# w = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)
w = tf.Variable(tf.zeros([nums, 1]))
b = tf.Variable(tf.zeros([nums, 1]))
# 定义函数
f = tf.matmul(x, tf.reshape(w, [-1, 1]))+b
h = tf.sigmoid(f)

# 定义损失函数
cost0 = y * tf.log(h)
cost1 = (1 - y) * tf.log(1 - h)
cost = (cost0 + cost1) / -nums
loss = tf.reduce_sum(cost)

# 梯度计算，模型训练
optimizer = tf.train.GradientDescentOptimizer(0.001)
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# 输入具体值
x = tf.placeholder(tf.float32, [None, 10, 10, 1], name='train_x')
y = tf.placeholder(tf.float32, [None, 10, 10, 1], name='train_x')

feed_dict = {x: x, y: y}
for step in range(1000):
    sess.run(train, {x: x, y: y})
    if step % 10 == 0:
        print(step, sess.run(w), sess.run(b))


#def loaddata
def loaddata(filename):
    file = open(filename)
    x = []
    y = []
    for line in file.readlines():
        line = line.strip().split()
        x.append([float(line[0]), float(line[1])])
        y.append(float(line[-1]))
    #将列表格式变成为矩阵的格式
    xmat = np.mat(x)
    ymat = np.mat(y)
    file.close()
    return xmat, ymat


#implement
xmat, ymat = loaddata('ytb_lr.txt')
print('xmat:', xmat, xmat.shape)
print('ymat:', ymat, ymat.shape)