data = [
    ('Tamim', [
         (2010, 742),
         (2011, 548),
         (2012, 486),
         (2013, 564),
         (2014, 589),
         (2015, 784),
         (2016, 652),
     ]),
    ('Imrul',[
         (2010, 426),
         (2011, 365),
         (2012, 558),
         (2013, 428),
         (2014, 261),
         (2015, 362),
         (2016, 257),
     ]),
    ('Sabbir',
     [
         (2010, 447),
         (2011, 385),
         (2012, 578),
         (2013, 448),
         (2014, 466),
         (2015, 589),
         (2016, 687),
     ]
     ),
    ('Shakib',
     [
         (2010, 624),
         (2011, 507),
         (2012, 445),
         (2013, 523),
         (2014, 548),
         (2015, 743),
         (2016, 611),
     ]
     ),
    ('Mushfiq',
     [
         (2010, 589),
         (2011, 512),
         (2012, 450),
         (2013, 528),
         (2014, 553),
         (2015, 748),
         (2016, 616),
     ]
     )
]

from userapp.models import Cricketer
for e in data:
    c, created = Cricketer.objects.get_or_create(name=e[0])
    for i in e[1]:
        r, r_created = c.runsbyyear_set.get_or_create(year=i[0], run=i[1])
