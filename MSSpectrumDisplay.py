import plotly.graph_objects as go

def _render_spectrum_plot(ms_peaks):
    max_int = max([peak[1] for peak in ms_peaks])
    # Drawing the spectrum object
    mzs = [peak[0] for peak in ms_peaks]
    ints = [peak[1]/max_int for peak in ms_peaks]
    neg_ints = [intensity * -1 for intensity in ints]

    # Hover data
    hover_labels = ["{:.4f} m/z, {:.2f} int".format(mzs[i], ints[i]) for i in range(len(mzs))]

    ms_fig = go.Figure(
        data=go.Scatter(x=mzs, y=ints, 
            mode='markers',
            marker=dict(size=0.00001),
            error_y=dict(
                symmetric=False,
                arrayminus=[0]*len(neg_ints),
                array=neg_ints,
                width=0
            ),
            text=hover_labels,
            textposition="top right"
        )
    )

    return ms_fig
