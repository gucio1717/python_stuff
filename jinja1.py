from jinja2 import Template

template = Template("""                                                     
{% set rps = [
    {'number': 72, 'type': 'RPALI1S', 'application': 'PGW'},
    {'number': 73, 'type': 'RPALI1S', 'application': 'PGW'},
    {'number': 74, 'type': 'GARP2A', 'application': 'PGW'}
]
%}

{% set inetr =  {'garp2a': 'CAAZ 111 222' } %}
{% set rgconr = {'garp2a': 'CAAZ 111 333' } %}


{% set pgw_sw = {'GARP2A': 
                    [
                        {'suname':'INETR',  'suid': inetr.garp2a },
                        {'suname':'RGCONR', 'suid': rgconr.garp2a }
                    ]
}%}


{%- for rp in rps %}                       
      {%- for key, value in rp.items() %}
          EXRUI:RP={{rp.number}}, pgw_sw[{{rp.type}}] ;
          RP {{rp.number}} {{ key }}, {{value}}
      {%- endfor %}                                        
{%- endfor %}                                                               

{%- for rp in rps %}
      {% set rptype = rp.type %}
      {%- for suid in  pgw_sw[rp.type] %}
          EXRUI:RP={{rp.number}}, suid="{{suid.suid}}" ;
          RP {{rp.number}} {{ key }}, {{value}}
      {%- endfor %}                                        
{%- endfor %}                                                               


soft for garp2: {{ pgw_sw.GARP2A[0].items() }}
""")

print(template.render())

