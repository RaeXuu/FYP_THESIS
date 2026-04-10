from graphviz import Digraph

dot = Digraph(comment='CNN Architecture')
dot.attr(rankdir='LR') # 设置从左到右

# 定义节点
dot.node('A', 'Input\n64x32x1')
dot.node('B', 'Conv 1\n64x32x32')
dot.node('C', 'Conv 2\n32x16x64')
dot.node('D', 'Conv 3\n16x8x128')
dot.node('E', 'Conv 4\n8x4x256')
dot.node('F', 'FC Layer\n1x1x256')
dot.node('G', 'Output\n(2 classes)')

# 定义连接
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG'])

# 保存并显示
dot.render('cnn_structure', format='png', view=True)