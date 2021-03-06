# This will create a way to copy the URL to the clipboard. 

dbc.Button("Copy Link", block=True, color="info", id="copy_link_button", n_clicks=0)

html.Div(
      [
          dcc.Link(id="query_link", href="#", target="_blank"),
      ],
      style={
            "display" :"none"
      }
  )


@dash_app.callback([
                Output('query_link', 'href'),
              ],
                [
                    Input('usi1', 'value'),
                    Input('library_select', 'value'),
                    Input('analog_select', 'value'),
                    Input('delta_mass_below', 'value'),
                    Input('delta_mass_above', 'value'),
                    Input('pm_tolerance', 'value'),
                    Input('fragment_tolerance', 'value'),
                    Input('cosine_threshold', 'value')
                ])
def draw_url(usi1, library_select, analog_select, delta_mass_below, delta_mass_above, pm_tolerance, fragment_tolerance, cosine_threshold):
    params = {}
    params["usi1"] = usi1
    params["library_select"] = library_select
    params["analog_select"] = analog_select
    params["delta_mass_below"] = delta_mass_below
    params["delta_mass_above"] = delta_mass_above
    params["pm_tolerance"] = pm_tolerance
    params["fragment_tolerance"] = fragment_tolerance
    params["cosine_threshold"] = cosine_threshold

    url_params = urllib.parse.urlencode(params)

    return [request.host_url + "fastsearch/?" + url_params]
  
dash_app.clientside_callback(
    """
    function(n_clicks, button_id, text_to_copy) {
        original_text = "Copy Link"
        if (n_clicks > 0) {
            const el = document.createElement('textarea');
            el.value = text_to_copy;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);

            setTimeout(function(id_to_update, text_to_update){ 
                return function(){
                    document.getElementById(id_to_update).textContent = text_to_update
                }}(button_id, original_text), 1000);

            document.getElementById(button_id).textContent = "Copied!"
            return 'Copied!';
        } else {
            return original_text;
        }
    }
    """,
    Output('copy_link_button', 'children'),
    [
        Input('copy_link_button', 'n_clicks'),
        Input('copy_link_button', 'id'),
    ],
    [
        State('query_link', 'href'),
    ]
)
