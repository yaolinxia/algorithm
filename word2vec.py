import tensorflow as tf

# 训练
def train(text):
    with open(text, encoding='utf-8') as f:
        inputs = f.readlines()
        # 再进行分词，等预处理操作
    return inputs

# 模型
def model(inputs, vocab_size):
    # 1.输入层
    # inputs = tf.placeholder(tf.int32, shape=[None], name='inputs')
    labels = tf.placeholder(tf.int32, shape=[None, None], name='labels')
    # 2.嵌入层
    embedding_size = 100  # 嵌入维度
    embedding = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1, 1))  # 嵌入层权重矩阵
    embed = tf.nn.embedding_lookup(embedding, inputs)  # 实现lookup
    # 3.Softmax
    smw = tf.Variable(tf.truncated_normal([vocab_size, embedding_size], stddev=0.1))
    smb = tf.Variable(tf.zeros(vocab_size))
    # 4.损失函数
    loss = tf.nn.sampled_softmax_loss(smw, smb, labels, embed, vocab_size)
    cost = tf.reduce_mean(loss)
    optimizer = tf.train.AdamOptimizer().minimize(cost)

if __name__ == '__main__':
    vocab_size = 1000
    inputs = train(path="####")
    model(inputs, vocab_size)

