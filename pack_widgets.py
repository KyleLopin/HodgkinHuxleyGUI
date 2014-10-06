__author__ = 'Kyle Vitautas Lopin'

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def pack_canvas(self, figure_bed, private_frame, anchor_option="CENTER"):
    canvas = FigureCanvasTkAgg(figure_bed, master=private_frame)
    canvas._tkcanvas.config(highlightthickness=0)
    canvas.draw()
    canvas.get_tk_widget().pack(anchor=anchor_option)
    return canvas


