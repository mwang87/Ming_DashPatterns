max_int = max([peak[1] for peak in ms1_peaks])
# Drawing the spectrum object
mzs = [peak[0] for peak in ms1_peaks]
ints = [peak[1]/max_int for peak in ms1_peaks]
neg_ints = [intensity * -1 for intensity in ints]

# Hover data
hover_labels = ["{:.4f} m/z, {:.2f} int".format(mzs[i], ints[i]) for i in range(len(mzs))]

ms1_fig = go.Figure(
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
