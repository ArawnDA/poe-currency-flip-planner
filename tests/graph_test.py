import unittest
from src.graph import *


test_offers = [{
  'offers': [
    {'contact_ign': 'KnifeySpooneyClaw', 'conversion_rate': 0.0893, 'stock': 153}
  ],
  'want': 'Chaos',
  'have': 'Alteration',
  'league': 'Abyss'
}, {
  'offers': [
    {'contact_ign': '_ZEUS___', 'conversion_rate': 0.0909, 'stock': 10},
    {'contact_ign': 'MVP_Kefir', 'conversion_rate': 0.087, 'stock': 20}
  ],
  'want': 'Chaos',
  'have': 'Chromatic',
  'league': 'Abyss'
}, {
  'offers': [
    {'contact_ign': 'wreddnuy', 'conversion_rate': 12.0, 'stock': 24},
    {'contact_ign': 'Corailthedog', 'conversion_rate': 11.0, 'stock': 2}
  ],
  'want': 'Alteration',
  'have': 'Chaos',
  'league': 'Abyss'
}, {
  'offers': [
    {'contact_ign': 'Azure_Dragon', 'conversion_rate': 1.0101, 'stock': 4261},
    {'contact_ign': 'Marcvz_GreenAgain', 'conversion_rate': 0.7143, 'stock': 222}
  ],
    'want': 'Alteration',
    'have': 'Chromatic',
    'league': 'Abyss'
}, {
  'offers': [
    {'contact_ign': 'The_Dank_Fire_God', 'conversion_rate': 11.5, 'stock': 106},
    {'contact_ign': 'MinerinoAbysss', 'conversion_rate': 11.1, 'stock': 322}
  ],
  'want': 'Chromatic',
  'have': 'Chaos',
  'league': 'Abyss'
}, {
  'offers': [
    {'contact_ign': 'Ashkeri', 'conversion_rate': 0.7143, 'stock': 449},
    {'contact_ign': 'Shioua_ouah', 'conversion_rate': 0.6897, 'stock': 1576}
  ],
  'want': 'Chromatic',
  'have': 'Alteration',
  'league': 'Abyss'
}]

expected_graph = {
  'Chaos': {
    'Alteration': [
      {'contact_ign': 'wreddnuy', 'conversion_rate': 12.0, 'stock': 24},
      {'contact_ign': 'Corailthedog', 'conversion_rate': 11.0, 'stock': 2}
    ],
    'Chromatic': [
      {'contact_ign': 'The_Dank_Fire_God', 'conversion_rate': 11.5, 'stock': 106},
      {'contact_ign': 'MinerinoAbysss', 'conversion_rate': 11.1, 'stock': 322}
    ]
  },
  'Alteration': {
    'Chaos': [
      {'contact_ign': 'KnifeySpooneyClaw', 'conversion_rate': 0.0893, 'stock': 153}
    ],
    'Chromatic': [
      {'contact_ign': 'Ashkeri', 'conversion_rate': 0.7143, 'stock': 449},
      {'contact_ign': 'Shioua_ouah', 'conversion_rate': 0.6897, 'stock': 1576}
    ]
  },
  'Chromatic': {
    'Chaos': [
      {'contact_ign': '_ZEUS___', 'conversion_rate': 0.0909, 'stock': 10},
      {'contact_ign': 'MVP_Kefir', 'conversion_rate': 0.087, 'stock': 20}
    ],
    'Alteration': [
      {'contact_ign': 'Azure_Dragon', 'conversion_rate': 1.0101, 'stock': 4261},
      {'contact_ign': 'Marcvz_GreenAgain', 'conversion_rate': 0.7143, 'stock': 222}
    ]
  }
}

expected_graph_small = {
  'Chaos': {
    'Alteration': [
      {'contact_ign': 'wreddnuy', 'conversion_rate': 12.0, 'stock': 24}
    ]
  },
  'Alteration': {
    'Chromatic': [
      {'contact_ign': 'Ashkeri', 'conversion_rate': 0.7143, 'stock': 449},
      {'contact_ign': 'Shioua_ouah', 'conversion_rate': 0.6897, 'stock': 1576}
    ]
  },
  'Chromatic': {
    'Chaos': [
      {'contact_ign': '_ZEUS___', 'conversion_rate': 0.0909, 'stock': 10},
      {'contact_ign': 'MVP_Kefir', 'conversion_rate': 0.087, 'stock': 20}
    ]
  }
}

expected_paths_small_same_currency = [
  [
    {'contact_ign': 'wreddnuy', 'conversion_rate': 12.0, 'stock': 24, 'have': 'Chaos', 'want': 'Alteration'},
    {'contact_ign': 'Shioua_ouah', 'conversion_rate': 0.6897, 'stock': 1576, 'have': 'Alteration', 'want': 'Chromatic'},
    {'contact_ign': 'MVP_Kefir', 'conversion_rate': 0.087, 'stock': 20, 'have': 'Chromatic', 'want': 'Chaos'}
  ], [
    {'contact_ign': 'wreddnuy', 'conversion_rate': 12.0, 'stock': 24, 'have': 'Chaos', 'want': 'Alteration'},
    {'contact_ign': 'Shioua_ouah', 'conversion_rate': 0.6897, 'stock': 1576, 'have': 'Alteration', 'want': 'Chromatic'},
    {'contact_ign': '_ZEUS___', 'conversion_rate': 0.0909, 'stock': 10, 'have': 'Chromatic', 'want': 'Chaos'}
  ], [
    {'contact_ign': 'wreddnuy', 'conversion_rate': 12.0, 'stock': 24, 'have': 'Chaos', 'want': 'Alteration'},
    {'contact_ign': 'Ashkeri', 'conversion_rate': 0.7143, 'stock': 449, 'have': 'Alteration', 'want': 'Chromatic'},
    {'contact_ign': 'MVP_Kefir', 'conversion_rate': 0.087, 'stock': 20, 'have': 'Chromatic', 'want': 'Chaos'}
  ], [
    {'contact_ign': 'wreddnuy', 'conversion_rate': 12.0, 'stock': 24, 'have': 'Chaos', 'want': 'Alteration'},
    {'contact_ign': 'Ashkeri', 'conversion_rate': 0.7143, 'stock': 449, 'have': 'Alteration', 'want': 'Chromatic'},
    {'contact_ign': '_ZEUS___', 'conversion_rate': 0.0909, 'stock': 10, 'have': 'Chromatic', 'want': 'Chaos'}
  ]
]

expected_paths_small_different_currency = [
  [
    {'contact_ign': 'wreddnuy', 'conversion_rate': 12.0, 'stock': 24, 'have': 'Chaos', 'want': 'Alteration'},
    {'contact_ign': 'Shioua_ouah', 'conversion_rate': 0.6897, 'stock': 1576, 'have': 'Alteration', 'want': 'Chromatic'}
  ], [
    {'contact_ign': 'wreddnuy', 'conversion_rate': 12.0, 'stock': 24, 'have': 'Chaos', 'want': 'Alteration'},
    {'contact_ign': 'Ashkeri', 'conversion_rate': 0.7143, 'stock': 449, 'have': 'Alteration', 'want': 'Chromatic'}
  ]
]

class GraphTest(unittest.TestCase):
  def test_build_graph(self):
    graph = build_graph(test_offers)
    self.assertDictEqual(graph, expected_graph)

  def test_find_paths(self):
    graph = build_graph(test_offers)
    paths_small_same_currency = find_paths(expected_graph_small, 'Chaos', 'Chaos')
    self.assertListEqual(expected_paths_small_same_currency, paths_small_same_currency)
    paths_small_different_currency = find_paths(expected_graph_small, 'Chaos', 'Chromatic')
    self.assertListEqual(expected_paths_small_different_currency, paths_small_different_currency)