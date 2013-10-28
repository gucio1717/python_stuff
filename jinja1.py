from jinja2 import Template

template = Template("""                                                     
{% set rps = [
    {'number': 72, 'type': 'GARP2A', 'application': 'TRH'},
    {'number': 73, 'type': 'RPG3',   'application': 'TRH'},
    {'number': 74, 'type': 'GARP2A', 'application': 'PGW'}
]
%}

{% set inetr =    {'garp2a': 'CAAZ 111 222', 'rpali1s': 'ali asdasd asdasd', 'rpg3': 'rpg3 asdasd asdasd' } %}
{% set rgconr =   {'garp2a': 'CAAZ 111 333', 'rpali1s': 'ali ffgswer aqweq' } %}
{% set rhlapdr =  {'garp2a': 'garp2 111 222', 'rpg3': 'rpg3 asdasd asdasd' } %}

{% set rp_apps = {'PGW':

                    {'GARP2A': 
                        [
                            {'suname':'INETR',  'suid': inetr.garp2a,  'em': '1', 'eqm': '2' },
                            {'suname':'RGCONR', 'suid': rgconr.garp2a, 'em': '4', 'eqm': '3' }
                        ],
                     'RPALI1S':
                        [
                            {'suname':'INETR',  'suid': inetr.rpali1s,  'em': '1', 'eqm': '2'  },
                            {'suname':'RGCONR', 'suid': rgconr.rpali1s, 'em': '1', 'eqm': '2' }
                        ]
    
                    },
                'TRH':
                    {'GARP2A': 
                        [
                            {'suname':'INETR',   'suid': inetr.garp2a,   'em': '1', 'eqm': '2' },
                            {'suname':'RHLAPDR', 'suid': rhlapdr.garp2a, 'em': '1', 'eqm': '2' }
                        ],
                     'RPG3':
                        [
                            {'suname':'INETR',   'suid': inetr.rpg3   },
                            {'suname':'RHLAPDR', 'suid': rhlapdr.rpg3,  'em': '1', 'eqm': 'RHLAPD-1' }
                        ]
                
                    }
                }
%}



{%- for rp in rps %}
        RP={{rp.number}}
      {%- for rp_module in rp_apps[rp.application][rp.type] %}
          EXRUI:RP={{rp.number}}, suid="{{rp_module.suid}}" ;
          {% if rp_module.em %}
              EXEMI:RP={{rp.number}}, suid="{{rp_module.suid}}", em={{rp_module.em}}, eqm={{rp_module.eqm}}
          {% endif %}
      {%- endfor %}                                        
{%- endfor %}                                                               


{# {#soft for garp2: {{ pgw_sw.GARP2A[0].items() }} #} 
""")

print(template.render())

