test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> tol = 1e-5
          >>> abs(average_20th_century_rating - 8.280113636363636) < tol
          True
          >>> abs(average_21st_century_rating - 8.23108108108108) < tol
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
