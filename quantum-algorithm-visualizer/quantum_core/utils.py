import matplotlib.pyplot as plt

def render_circuit(qc):
    fig = qc.draw(output='mpl')
    return fig
